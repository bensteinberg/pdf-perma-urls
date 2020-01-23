from setuptools import setup

setup(
    name='pdf-perma-urls',
    version='0.1',
    py_modules=['main'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        pdf-perma-urls=main:read_pdf
    ''',
)
