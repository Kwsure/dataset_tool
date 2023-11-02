import json

f = open("/home/kongws/dataset/cmp2coco.json", "w", encoding="utf-8")
categor = ["window", "door", "pillar", "balcony"]
# "images": [{"id": 1, "file_name": "cmp_b0001.jpg", "width": 543, "height": 1024, "date_captured": "2021-05-10 04:17:06.270466", "license": 1, "coco_url": "", "flickr_url": ""},
# f.write('"categories": [{"id": 1, "name": "window", "supercategory": "object"},')
# f.write('[{"id": 2, "name": "door", "supercategory": "object"},')
# f.write('[{"id": 3, "name": "balcony", "supercategory": "object"},')
# f.write('[{"id": 4, "name": "pillar", "supercategory": "object"}],')
res = {}
info = {}
info["description"] = "CMP_XML2COCO"
info["url"] = ""
info["version"] = "1.0"
info["year"] = "2023"
info["contributor"] = "Wenshuo.Kong"
info["date_created"] = "2023.10.28"
res["info"] = info

lisences = []
lisence = {}
lisence["id"] = 1
lisence["name"] = "Attribution-NonCommercial-ShareAlike License"
lisence["url"] = "http://creativecommons.org/licenses/by-nc-sa/2.0/"
lisences.append(lisence)
res["lisences"] = lisences

categories = []
for i in range(4):
    categorie = {}
    categorie["id"] = i + 1
    categorie["name"] = categor[i]
    categorie["supercategory"] = "object"
    categories.append(categorie)
res["categories"] = categories

images = []
imagesjson = []
with open("/home/kongws/dataset/allimages.txt", "r", encoding="utf-8") as f2:
    imagesjson = json.load(f2)
imagessize = []
with open("/home/kongws/dataset/allimage_size.txt", "r", encoding="utf-8") as f3:
    imagessize = json.load(f3)
for i in range(len(imagesjson)):
    image = {}
    image["id"] = i + 1
    image["file_name"] = imagesjson[i]
    image["width"] = imagessize[i][0]
    image["height"] = imagessize[i][1]
    image["date_captured"] = ""
    image["license"] = 1
    image["coco_url"] = ""
    image["flickr_url"] = ""
    images.append(image)
res["images"] = images

annotations = []
windows = {}
with open("/home/kongws/dataset/windows.txt", "r", encoding="utf-8") as f3:
    windows = json.load(f3)

doors = {}
with open("/home/kongws/dataset/doors.txt", "r", encoding="utf-8") as f4:
    doors = json.load(f4)


pillars = {}
with open("/home/kongws/dataset/pillars.txt", "r", encoding="utf-8") as f5:
    pillars = json.load(f5)

balconys = {}
with open("/home/kongws/dataset/balconys.txt", "r", encoding="utf-8") as f6:
    balconys = json.load(f6)
index = 0
for i, ele in enumerate(imagesjson):
    element = ele[:-3] + "xml"
    for j in range(len(windows[element])):
        annotation = {}
        index += 1
        annotation["id"] = index
        annotation["image_id"] = i + 1
        annotation["category_id"] = 1
        annotation["iscrowd"] = 0
        annotation["area"] = windows[element][j][2] * windows[element][j][3]
        annotation["bbox"] = windows[element][j]
        x1 = windows[element][j][0]
        y1 = windows[element][j][1]
        x2 = windows[element][j][0] + windows[element][j][2]
        y2 = y1
        x3 = x2
        y3 = y1 + windows[element][j][3]
        x4 = x1
        y4 = y3
        annotation["segmentation"] = []
        annotation["segmentation"].append([x1, y1, x2, y2, x3, y3, x4, y4])
        annotations.append(annotation)

    for j in range(len(doors[element])):
        annotation = {}
        index += 1
        annotation["id"] = index
        annotation["image_id"] = i + 1
        annotation["category_id"] = 2
        annotation["iscrowd"] = 0
        annotation["area"] = doors[element][j][2] * doors[element][j][3]
        annotation["bbox"] = doors[element][j]
        x1 = doors[element][j][0]
        y1 = doors[element][j][1]
        x2 = doors[element][j][0] + doors[element][j][2]
        y2 = y1
        x3 = x2
        y3 = y1 + doors[element][j][3]
        x4 = x1
        y4 = y3
        annotation["segmentation"] = []
        annotation["segmentation"].append([x1, y1, x2, y2, x3, y3, x4, y4])
        annotations.append(annotation)

    for j in range(len(pillars[element])):
        annotation = {}
        index += 1
        annotation["id"] = index
        annotation["image_id"] = i + 1
        annotation["category_id"] = 3
        annotation["iscrowd"] = 0
        annotation["area"] = pillars[element][j][2] * pillars[element][j][3]
        annotation["bbox"] = pillars[element][j]
        x1 = pillars[element][j][0]
        y1 = pillars[element][j][1]
        x2 = pillars[element][j][0] + pillars[element][j][2]
        y2 = y1
        x3 = x2
        y3 = y1 + pillars[element][j][3]
        x4 = x1
        y4 = y3
        annotation["segmentation"] = []
        annotation["segmentation"].append([x1, y1, x2, y2, x3, y3, x4, y4])
        annotations.append(annotation)

    for j in range(len(balconys[element])):
        annotation = {}
        index += 1
        annotation["id"] = index
        annotation["image_id"] = i + 1
        annotation["category_id"] = 4
        annotation["iscrowd"] = 0
        annotation["area"] = balconys[element][j][2] * balconys[element][j][3]
        annotation["bbox"] = balconys[element][j]
        x1 = balconys[element][j][0]
        y1 = balconys[element][j][1]
        x2 = balconys[element][j][0] + balconys[element][j][2]
        y2 = y1
        x3 = x2
        y3 = y1 + balconys[element][j][3]
        x4 = x1
        y4 = y3
        annotation["segmentation"] = []
        annotation["segmentation"].append([x1, y1, x2, y2, x3, y3, x4, y4])
        annotations.append(annotation)
res["annotations"] = annotations
f.write(json.dumps(res))
f.close()
