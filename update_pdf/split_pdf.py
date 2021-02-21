from pikepdf import Pdf


def split_pdf(stream, opcode, data):
    pdf = stream
    if opcode == 0:
        new_pdf = Pdf.new()
        new_pdf.pages.append(pdf.pages[data["number"]])
        new_pdf.save(str(data["number"])+'.pdf')
    elif opcode == 1:
        new_pdf = Pdf.new()
        for n, page in enumerate(pdf.pages):
            if n >= data["start"]:
                new_pdf.pages.append(page)
            if n == data["end"]:
                break
        new_pdf.author()
        new_pdf.save('output.pdf')
    pdf.close()


