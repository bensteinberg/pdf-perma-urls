This program uses `pdftotext` to read a PDF file, extracts
[Perma.cc](https//perma.cc/) links from it, then uses Perma's [public
API](https://perma.cc/docs/developer#developer-public-archives) to
look up the URLs originally archived. It exports a CSV file with the
Perma links and URLs.

After setting up a virtual environment (see below), running

    python main.py yourfile.pdf
    
should produce `yourfile.csv`.

Requirements
------------
You will need `pdftotext`, which is in various packages; try `brew
install poppler` on a Mac, or install `poppler-utils` in Linux.

There are various ways of setting up a Python virtualenv. Try
installing `python3-venv`, then run

    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt
