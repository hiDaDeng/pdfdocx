from pdfdocx import read_pdf,read_docx

p_text = read_pdf('data.pdf')
d_text = read_docx('data.docx')
print(p_text)
print(d_text)