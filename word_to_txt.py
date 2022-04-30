import os
from docx import Document
import re

basepath = os.path.abspath(__file__)
folder = os.path.dirname(basepath)
input_docx_folder = folder + "/input/docx/"
output_txt_folder = folder + "/output/txt/"

for filename in os.listdir(input_docx_folder):
    input_docx_file = os.path.join(input_docx_folder, filename)
    output_txt_file = os.path.join(output_txt_folder, filename.replace('.docx', '.txt'))
    print(input_docx_file)
    document = Document(input_docx_file)
    result = ""
    for paragraph in document.paragraphs:
        content = paragraph.text.strip()
        print(content)
        ret = re.match("(\d+\.)(.+)", content)
        if ret:
            print(ret.group(1))
            print(ret.group(2))
            result += str(ret.group(1)) + " " + str(ret.group(2))
        else:
            result += content
        result += "\n"
        print("#############")

    file = open(output_txt_file,'w')
    file.write(result)

