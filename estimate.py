# Write your code here :-)
import os, sys
from docxtpl import DocxTemplate

os.chdir(sys.path[0])
doc = DocxTemplate('budget_template.docx')
context = {
'clientName': 'John',
'clientAddress': '26 Baxendale',
'siteAddress': 'WestWorld',
'houseNumber': '48'}

doc.render(context)
doc.save('Template_Rendered.docx')# Write your code here :-)
