import os
import shutil


def separate_files(directory):
    """将指定目录中的.jpg和.txt文件分别移动到新的子目录中"""
    # 创建用于存放jpg和txt文件的目录
    jpg_dir = os.path.join(directory, 'jpg_files')
    txt_dir = os.path.join(directory, 'txt_files')
    os.makedirs(jpg_dir, exist_ok=True)
    os.makedirs(txt_dir, exist_ok=True)

    # 遍历目录中的所有文件
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # 检查文件扩展名并移动到相应的新目录
        if filename.endswith('.jpg'):
            shutil.move(file_path, os.path.join(jpg_dir, filename))
        elif filename.endswith('.txt'):
            shutil.move(file_path, os.path.join(txt_dir, filename))


# 使用示例
directory_path = '.././smallDataset/newSmallDataset/val'
separate_files(directory_path)
