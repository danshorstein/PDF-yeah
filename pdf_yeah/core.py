# -*- coding: utf-8 -*-

"""
pdf_yeah.core
~~~~~~~~~~~~
This module implements the pdf_yeah core functionality.
:copyright: (c) 2017 by Daniel Shorstein.
:license: MIT, see LICENSE for more details.
"""


import io
import requests
import pdfplumber


def extract_text(path):
    """Returns a generator object with a list of rows for each page.

    :param path: can be a URL or system path to a pdf file.

    Usage::
        If the
        file is small, you may be able to create one object containing all
        text in the pdf file:
      >>> pdf_pages = pdf_yeah.extract_text('https://www.nostarch.com/download/Automate_the_Boring_Stuff_sample_ch17.pdf')
      >>> pdf_full_text = [page for page in pdf_pages]

        Otherwise it's better to iterate through the generator like so:
      >>> import pdf_yeah
      >>> pdf_pages = pdf_yeah.extract_text('https://abc.xyz/investor/pdf/20160331_alphabet_10Q.pdf')
      >>> pg1 = next(pdf_pages)
      >>> print('\n'.join(pg1[:9]))

      UNITED STATES
      SECURITIES AND EXCHANGE COMMISSION
      Washington, D.C. 20549
      ________________________________________________________________________________________
      FORM 10-Q
      ________________________________________________________________________________________
      (Mark One)
      QUARTERLY REPORT PURSUANT TO SECTION 13 OR 15(d) OF THE SECURITIES EXCHANGE ACT OF 1934
      For the quarterly period ended March 31, 2016

    """

    if path.startswith('http'):
        r = requests.get(path)
        fp = io.BytesIO(r.content)
        pdf = pdfplumber.load(fp)
        for page in pdf.pages:
            yield page.extract_text().split('\n')

    else:
        with open(path, 'rb') as fp:
            pdf = pdfplumber.load(fp)
            for page in pdf.pages:
                yield page.extract_text().split('\n')
