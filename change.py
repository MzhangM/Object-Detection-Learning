import os
import shutil
import numpy as np


def split_dataset(data_dir, train_ratio=0.7, val_ratio=0.2, test_ratio=0.1):
    assert np.isclose(train_ratio + val_ratio + test_ratio, 1.0)

    # 获取所有图片文件的完整路径
    image_paths = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.endswith('.jpg')]
    # 确保每张图片都有一个对应的txt文件
    data_paths = [(img_path, img_path.replace('.jpg', '.txt')) for img_path in image_paths if
                  os.path.exists(img_path.replace('.jpg', '.txt'))]

    # 打乱数据顺序
    np.random.shuffle(data_paths)

    # 计算分割点
    total_files = len(data_paths)
    train_end = int(total_files * train_ratio)
    val_end = train_end + int(total_files * val_ratio)

    # 分割数据集
    train_files = data_paths[:train_end]
    val_files = data_paths[train_end:val_end]
    test_files = data_paths[val_end:]

    # 创建存储目录
    for folder in ['train', 'val', 'test']:
        os.makedirs(os.path.join(data_dir, folder), exist_ok=True)

    # 移动文件
    def move_files(files, folder):
        for img_path, txt_path in files:
            shutil.move(img_path, os.path.join(data_dir, folder, os.path.basename(img_path)))
            shutil.move(txt_path, os.path.join(data_dir, folder, os.path.basename(txt_path)))

    move_files(train_files, 'train')
    move_files(val_files, 'val')
    move_files(test_files, 'test')


# 使用函数
split_dataset('.././smallDataset/newSmallDataset')
