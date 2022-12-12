import click
import subprocess
import os
import csv
import re
from tqdm import tqdm
import requests


@click.command()
@click.argument('filename')
def read_pdf(filename):
    """
    This program reads Perma.cc URLs from a PDF document and reports
    what the captured URLs were. It requires that `pdftotext` be in your
    $PATH. It will not work on old-style Perma links.
    """
    text = subprocess.check_output(['pdftotext', filename, '-'])
    links = re.findall(r"https://perma.cc/....-....", str(text))
    archives = 'https://api.perma.cc/v1/public/archives/{}'
    (root, _) = os.path.splitext(filename)
    with open('{}.csv'.format(root), 'w', newline='') as f:
        w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        w.writerow(['permalink', 'url'])
        for link in tqdm(links):
            r = requests.get(archives.format(link[-9:]))
            if r.status_code == requests.codes.ok:
                detail = r.json()
                url = detail['url']
                user_upload = [c['user_upload'] for c in detail['captures'] if c['role'] == 'primary'][0]
                if user_upload:
                    print('ALERT! {} ({}) is a user upload! Not writing to CSV.'.format(link, url))
                else:
                    w.writerow([link, url])
            else:
                print('WARNING! {} not found.'.format(link))
                w.writerow([link, 'NOTFOUND'])
