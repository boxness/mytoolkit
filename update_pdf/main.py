import split_pdf
from pikepdf import Pdf


if __name__ == '__main__':
    data = {}
    file_path = input("请输入文件路径: ")
    opcode = int(input("清输入操作码: "))
    if opcode == 0:
        # 提取单个页面
        data["number"] = int(input("请输入要获得的页: "))
    if opcode == 1:
        # 提取部分文件
        data["start"] = int(input("请输入起始页: "))
        try:
            data["end"] = int(input("请输入终点页: "))
        except Exception as invalid_input_error:
            data["end"] = None
    stream = Pdf.open(file_path)
    split_pdf.split_pdf(stream, opcode, data)



