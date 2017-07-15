PDF_yeah

A pythonic way to extract text from pdf files.
Requires requests and pdfplumber. Currently works on Python 3.5.

Usage
If the PDF file is small, you may be able to create one object containing all
text in the pdf file:
  >>> pdf_pages = pdf_yeah.extract_text('https://www.nostarch.com/download/Automate_the_Boring_Stuff_sample_ch17.pdf')
  >>> pdf_full_text = [page for page in pdf_pages]

Otherwise it's better to iterate through the generator like so:
  >>> import pdf_yeah
  >>> pdf_pages = pdf_yeah.extract_text('https://abc.xyz/investor/pdf/20160331_alphabet_10Q.pdf')
  >>> pg1 = next(pdf_pages)
  >>> print('\n'.join(pg1[:9]))