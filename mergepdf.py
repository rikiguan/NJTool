# -*- coding: gbk -*-
import os
from PyPDF2 import PdfReader, PdfWriter


def merge_pdfs(directory_path, output_filename):
    pdf_writer = PdfWriter()
    

    for filename in os.listdir(directory_path):
        if filename.endswith(".pdf"):
            file_path = os.path.join(directory_path, filename)
            print(f"合并文件: {filename}")
            

            pdf_reader = PdfReader(file_path)
            for page_num in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page_num])
    

    output_path =  output_filename
    with open(output_path, "wb") as output_pdf:
        pdf_writer.write(output_pdf)
    
    print(f"合并后pdf: {output_path}")


directory_path = "./headed"  
output_filename = "merged_output.pdf"  
merge_pdfs(directory_path, output_filename)
