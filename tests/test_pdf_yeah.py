import os

from pdf_yeah import extract_text


def test_web_pdf():
    pdfloc = r'https://abc.xyz/investor/pdf/20160331_alphabet_10Q.pdf'
    pdf_pages = extract_text(pdfloc)

    pg1 = next(pdf_pages)

    assert 'QUARTERLY REPORT PURSUANT TO SECTION 13 OR 15(d) OF THE SECURITIES EXCHANGE ACT OF 1934' in pg1


def test_local_pdf():
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__)))
    pdfloc = os.path.join(base_path, '..', 'tests', r'20160331_alphabet_10Q.pdf')
    pdf_pages = extract_text(pdfloc)

    pg1 = next(pdf_pages)

    assert 'QUARTERLY REPORT PURSUANT TO SECTION 13 OR 15(d) OF THE SECURITIES EXCHANGE ACT OF 1934' in pg1
