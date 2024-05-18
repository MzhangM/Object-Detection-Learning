import os
import shutil
import numpy as np


def split_dataset(data_dir, train_ratio=0.7, val_ratio=0.2, test_ratio=0.1):
    assert np.isclose(train_ratio + val_ratio + test_ratio, 1.0)

    # get all images path
    image_paths = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.endswith('.jpg')]
    # 确保每张图片都有一个对应的txt文件
    data_paths = [(img_path, img_path.replace('.jpg', '.txt')) for img_path in image_paths if
                  os.path.exists(img_path.replace('.jpg', '.txt'))]

    # disorder dataset
    np.random.shuffle(data_paths)

    # calculate the split point
    total_files = len(data_paths)
    train_end = int(total_files * train_ratio)
    val_end = train_end + int(total_files * val_ratio)

    # separate dataset
    train_files = data_paths[:train_end]
    val_files = data_paths[train_end:val_end]
    test_files = data_paths[val_end:]

    #  create a storage dir
    for folder in ['train', 'val', 'test']:
        os.makedirs(os.path.join(data_dir, folder), exist_ok=True)

    # move files
    def move_files(files, folder):
        for img_path, txt_path in files:
            shutil.move(img_path, os.path.join(data_dir, folder, os.path.basename(img_path)))
            shutil.move(txt_path, os.path.join(data_dir, folder, os.path.basename(txt_path)))

    move_files(train_files, 'train')
    move_files(val_files, 'val')
    move_files(test_files, 'test')


# 使用函数
split_dataset('.././smallDataset/newSmallDataset')
