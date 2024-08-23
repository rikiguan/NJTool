# -*- coding: gbk -*-
import os
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from io import BytesIO

def add_header_to_pdf(input_pdf_path, font_path):
    # 获取文件名并确保其编码正确
    file_name = os.path.basename(input_pdf_path)
    
    # 注册中文字体
    pdfmetrics.registerFont(TTFont('SimSun', font_path))
    
    # 读取原始PDF
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    for page_num in range(len(reader.pages)):
        # 从原始PDF中读取页面
        page = reader.pages[page_num]
        
        # 创建一个内存中的PDF来添加页眉
        packet = BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        
        # 设置字体为中文字体
        can.setFont('SimSun', 12)
        
        # 设置页眉位置和内容：文件名和页码
        header_text = f"{file_name} - 第 {page_num + 1} 页"
        can.drawString(100, 20, header_text)
        can.save()
        
        # 将新创建的页眉PDF和原页面合并
        packet.seek(0)
        new_pdf = PdfReader(packet)
        page.merge_page(new_pdf.pages[0])
        
        # 添加修改后的页面到写入器
        writer.add_page(page)

    # 输出到新文件
    output_pdf_path = f"./headed/headered_{file_name}"
    with open(output_pdf_path, "wb") as output_file:
        writer.write(output_file)

    print(f"新文件保存为：{output_pdf_path}")

# 定义一个函数，批量处理目录下的所有PDF文件
def batch_process_pdfs(directory_path, font_path):
    for filename in os.listdir(directory_path):
        if filename.endswith(".pdf"):
            input_pdf_path = os.path.join(directory_path, filename)
            print(f"正在处理: {filename}")
            add_header_to_pdf(input_pdf_path, font_path)

# 示例调用
directory_path = "./pdf"  # 替换为你的PDF文件所在目录路径
font_path = "./simhei.ttf"  # 替换为你下载的中文字体路径
batch_process_pdfs(directory_path, font_path)
