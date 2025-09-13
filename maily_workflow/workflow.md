
requirements:
- eml2pdf
- pdftk

1. export .elm format, save in `input_dir`

2. run: `python monkeypatch_utf8_elm3pdf.py -n 1 -p a4 input_dir output_dir`
	- need to run a monkey-patched version of the original 
	(`eml2pdf -p a4 input_dir output_dir`) to go around issues with the encoding

3. run: `./extract_all_1st_pages_and_join_them.sh`

4. empty folders for next turn
