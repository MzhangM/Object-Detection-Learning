import xml.etree.ElementTree as ET
import os
import shutil

classes = ['person', 'vest', 'helmet', 'board', 'wood',
           'rebar', 'brick', 'scaffold', 'handcart', 'cutter',
           'electric box', 'hopper', 'hook', 'fence', 'slogan']

output_dir = './dataset/train/labels'
input_dir = r"E:\BaiduNetdiskDownload\SODA\VOCv1\VOC2007\Annotations"

for file in os.listdir(input_dir):
    if file.endswith('.xml'):
        file_path = os.path.join(input_dir, file)
        tree = ET.parse(file_path)
        root = tree.getroot()

        size = root.find('size')
        width = int(size.find('width').text)
        height = int(size.find('height').text)

        # 创建yolo格式文件
        out_file = open(os.path.join(output_dir, file.replace('xml', 'txt')), 'w')

        # 遍历每个对象并写入yolo格式文件
        for obj in root.iter('object'):
            cls = obj.find('name').text
            if cls not in classes:
                continue
            cls_id = classes.index(cls)
            xmlbox = obj.find('bndbox')
            b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text),
                 int(xmlbox.find('ymax').text))

            bbx_w = (b[2] - b[0]) / float(width)
            bbx_h = (b[3] - b[1]) / float(height)
            bbx_x = (b[0] + b[2]) / 2.0 / float(width)
            bbx_y = (b[1] + b[3]) / 2.0 / float(height)

            out_file.write(
                str(cls_id) + ' ' + str(bbx_x) + ' ' + str(bbx_y) + ' ' + str(bbx_w) + ' ' + str(bbx_h) + '\n')
