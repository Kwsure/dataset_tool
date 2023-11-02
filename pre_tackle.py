import os
from xml.dom.minidom import parse
from PIL import Image
import json

images = []
image_size = []
xml = []
CMP_path = "/home/kongws/dataset/CMP_facade_DB_base/base"
filenames = os.listdir(CMP_path)
for file in filenames:
    file_type = file.split(".")[-1]
    if file_type == "jpg":
        images.append(file)
        img = Image.open(CMP_path + "/" + file)
        w = img.width  # 图片的宽
        h = img.height
        image_size.append([w, h])
    elif file_type == "xml":
        xml.append(file)
    else:
        continue
with open("/home/kongws/dataset/allimages.txt", "w", encoding="utf-8") as f:
    f.write(json.dumps(images))
with open("/home/kongws/dataset/allimage_size.txt", "w", encoding="utf-8") as f:
    f.write(json.dumps(image_size))
# print(image_size[0])
# print(image_size[1])
# print(image_size[2])
# for file in xml:
#     with open(CMP_path + "/" + file, 'r+') as f:
#         content = f.read()
#         if(content[0:6] != '<root>'):
#             f.seek(0, 0)
#             f.write('<root>\n' + content)
#             f.write('</root>')

# 读取文件
windows = {}
balconys = {}
pillars = {}
doors = {}


def calcoor(width, height, x1, x2, y1, y2):
    res = [
        round(float(x1) * height),
        round(float(y1) * width),
        round(float(x2) * height),
        round(float(y2) * width),
    ]
    return res


# path = "cmp_b0003.xml"
# for i, element in enumerate(xml):
#     domtree = parse(CMP_path + "/" + element)
#     # 获取文档元素对象
#     print(element)
#     collection = domtree.documentElement
#     obj = collection.getElementsByTagName("object")
#     count = 0
#     window = []
#     balcony = []
#     pillar = []
#     door = []
#     for ob in obj:
#         labelname = ob.getElementsByTagName("labelname")[0].childNodes[0].nodeValue
#         # print(labelname)
#         point = ob.getElementsByTagName("points")[0]
#         x1 = point.getElementsByTagName("x")[0].childNodes[0].nodeValue
#         x2 = point.getElementsByTagName("x")[1].childNodes[0].nodeValue
#         y1 = point.getElementsByTagName("y")[0].childNodes[0].nodeValue
#         y2 = point.getElementsByTagName("y")[1].childNodes[0].nodeValue
#         coordi = calcoor(int(image_size[i][0]), int(image_size[i][1]), x1, x2, y1, y2)
#         coor = [coordi[1], coordi[0], coordi[3] - coordi[1], coordi[2] - coordi[0]]
#         # 这里有个坑，labelname是前后前后各带有一个分号的字符串
#         if labelname[1:-1] == "window":
#             window.append(coor)
#         elif labelname[1:-1] == "door":
#             door.append(coor)
#         elif labelname[1:-1] == "pillar":
#             pillar.append(coor)
#         elif labelname[1:-1] == "balcony":
#             balcony.append(coor)
#         else:
#             continue
#     windows[element] = window
#     doors[element] = door
#     pillars[element] = pillar
#     balconys[element] = balcony

# with open("/home/kongws/dataset/windows.txt", "w", encoding="utf-8") as f:
#     f.write(json.dumps(windows))
# with open("/home/kongws/dataset/doors.txt", "w", encoding="utf-8") as f:
#     f.write(json.dumps(doors))
# with open("/home/kongws/dataset/pillars.txt", "w", encoding="utf-8") as f:
#     f.write(json.dumps(pillars))
# with open("/home/kongws/dataset/balconys.txt", "w", encoding="utf-8") as f:
#     f.write(json.dumps(balconys))

# print("windows = " + str(windows[path]))
# print("doors = " + str(doors[path]))
# print("pillars = " + str(pillars[path]))
# print("balconys = " + str(balconys[path]))
