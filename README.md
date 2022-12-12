This program uses `pdftotext` to read a PDF file, extracts
[Perma.cc](https//perma.cc/) links from it, then uses Perma's [public
API](https://perma.cc/docs/developer#developer-public-archives) to
look up the URLs originally archived. It exports a CSV file with the
Perma links and URLs.

Requirements
------------
You will need `pdftotext`, which is in various packages; try `brew
install poppler` on a Mac, or install `poppler-utils` in Linux.

[Install Poetry](https://python-poetry.org/docs/#installation), then run

    poetry install
    
At this point, running

    poetry run pdf-perma-urls yourfile.pdf
    
should produce `yourfile.csv`.
