for f in output_dir/*.pdf; do
    base=$(basename "$f" .pdf)
    pdftk "$f" cat 1 output "first_pages/${base}_p1.pdf"
done

pdftk first_pages/*_p1.pdf cat output joined_first_pages.pdf
