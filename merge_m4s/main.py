import json
import os


def get_name(num, address):
    file_address = c + "/"+str(num)+"/entry.json"
    json_text_io = open(file_address, encoding="utf-8")
    json_text = json_text_io.read()
    new_json = json.loads(json_text)
    _file_name = '[' + str(num) + ']_' + new_json["page_data"]["part"].replace(" ", "_")
    return _file_name


print("请输入范围：")
a = int(input("上界："))
b = int(input("下界："))
print("请输入文件夹位置")
c = str(input("文件夹位置:"))
if not os.path.exists(c+"/output"):
    os.mkdir(c+"/output")
for i in range(a, b+1):
    file_name = get_name(i, c)
    if not os.path.exists(c + "/output/"+file_name+".mp4"):
        os.system("ffmpeg -i " + c + "/"
                  + str(i) + "/80/audio.m4s -i "
                  + c + "/" + str(i) + "/80/video.m4s -codec copy "
                  + c + "/output/" + file_name + ".mp4")
