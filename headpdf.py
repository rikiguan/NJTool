# -*- coding: gbk -*-
import os
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from io import BytesIO

def add_header_to_pdf(input_pdf_path, font_path):
    # ��ȡ�ļ�����ȷ���������ȷ
    file_name = os.path.basename(input_pdf_path)
    
    # ע����������
    pdfmetrics.registerFont(TTFont('SimSun', font_path))
    
    # ��ȡԭʼPDF
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    for page_num in range(len(reader.pages)):
        # ��ԭʼPDF�ж�ȡҳ��
        page = reader.pages[page_num]
        
        # ����һ���ڴ��е�PDF�����ҳü
        packet = BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        
        # ��������Ϊ��������
        can.setFont('SimSun', 12)
        
        # ����ҳüλ�ú����ݣ��ļ�����ҳ��
        header_text = f"{file_name} - �� {page_num + 1} ҳ"
        can.drawString(100, 20, header_text)
        can.save()
        
        # ���´�����ҳüPDF��ԭҳ��ϲ�
        packet.seek(0)
        new_pdf = PdfReader(packet)
        page.merge_page(new_pdf.pages[0])
        
        # ����޸ĺ��ҳ�浽д����
        writer.add_page(page)

    # ��������ļ�
    output_pdf_path = f"./headed/headered_{file_name}"
    with open(output_pdf_path, "wb") as output_file:
        writer.write(output_file)

    print(f"���ļ�����Ϊ��{output_pdf_path}")

# ����һ����������������Ŀ¼�µ�����PDF�ļ�
def batch_process_pdfs(directory_path, font_path):
    for filename in os.listdir(directory_path):
        if filename.endswith(".pdf"):
            input_pdf_path = os.path.join(directory_path, filename)
            print(f"���ڴ���: {filename}")
            add_header_to_pdf(input_pdf_path, font_path)

# ʾ������
directory_path = "./pdf"  # �滻Ϊ���PDF�ļ�����Ŀ¼·��
font_path = "./simhei.ttf"  # �滻Ϊ�����ص���������·��
batch_process_pdfs(directory_path, font_path)
