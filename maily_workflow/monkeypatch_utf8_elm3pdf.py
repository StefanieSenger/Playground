# this file is very sloppy and dirty, but works

import eml2pdf.eml2pdf as e2p
import email
from pathlib import Path


# decode fallback
if hasattr(e2p, "decode_to_str"):
    _orig_decode = e2p.decode_to_str

    def _decode_fallback(bytes_content, content_charset):
        try:
            return _orig_decode(bytes_content, content_charset)
        except UnicodeDecodeError:
            # fallback: latin-1 preserves byte values and never raises
            return bytes(bytes_content).decode("latin-1", errors="replace")

    e2p.decode_to_str = _decode_fallback

_orig_process_eml = e2p.process_eml

def process_eml_patched(eml_path: Path, output_dir: Path,
                        page: str = 'a4', debug_html: bool = False,
                        unsafe: bool = False):
    """Replacement for e2p.process_eml that opens eml in binary safely."""
    logger = e2p.logger
    logger.info(f'Processing {eml_path}')

    # parse eml from binary file (avoid text-mode decoding errors)
    try:
        with open(eml_path, "rb") as fh:
            msg = email.message_from_binary_file(fh)
    except Exception as exc:
        logger.error(f"Failed to read/parse {eml_path}: {exc}")
        return

    try:
        email_header = e2p.Header(msg, eml_path)
        html_content, attachments = e2p.walk_eml(msg, eml_path)
        attachment_list = e2p.generate_attachment_list(attachments)

        if html_content:
            if isinstance(html_content, str):
                html_content = (
                    "<meta charset=\"UTF-8\">\n"
                    '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">\n'
                    f"{email_header.html}\n{attachment_list}\n<hr>\n{html_content}"
                )

            output_path = e2p.get_output_base_path(email_header.date,
                                                   email_header.subject,
                                                   output_dir)
            e2p.generate_pdf(html_content, output_path, eml_path,
                             debug_html=debug_html, page=page, unsafe=unsafe)
        else:
            logger.warning(f"No plain text or HTML content found in {eml_path}. Skipping...")
    except Exception as exc:
        logger.error(f"Error processing {eml_path}: {exc}")

e2p.process_eml = process_eml_patched


# monkey-patch decoding
original_decode = e2p.decode_to_str

def decode_to_str_patched(bytes_content, content_charset):
    try:
        return original_decode(bytes_content, content_charset)
    except UnicodeDecodeError:
        return bytes_content.decode("latin-1")
e2p.decode_to_str = decode_to_str_patched


# monkey-patch walk_eml
original_walk_eml = e2p.walk_eml

def walk_eml_patched(msg, eml_path):
    try:
        return original_walk_eml(msg, eml_path)
    except UnboundLocalError:
        # fallback: skip decoding this email part, return empty HTML and no attachments
        return ("", [])

e2p.walk_eml = walk_eml_patched


e2p.main()
