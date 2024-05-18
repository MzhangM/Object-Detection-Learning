import os


def count_all_files(directory):
    """递归计算指定目录及其所有子目录中的文件数量"""
    file_count = 0
    for root, dirs, files in os.walk(directory):
        file_count += len(files)
    return file_count


# 使用示例
directory_path = '.././dataset/JPEGImages/test/'
total_files = count_all_files(directory_path)
print(f'The directory and its subdirectories contain {total_files} files.')
