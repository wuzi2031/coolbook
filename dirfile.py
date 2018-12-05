import json
import os

def jsondir(path):
    tree = []
    sub_paths = os.listdir(path)
    full_sub_paths = [path+"/"+sub_path for sub_path in sub_paths]
    # print(full_sub_paths)
    for index, full_sub_path in enumerate(full_sub_paths):
        data = {}
        if os.path.isdir(full_sub_path):
            data['text'] = sub_paths[index]
            data['children'] =jsondir(full_sub_path)
        else:
            data['text'] = sub_paths[index]
        tree.append(data)
    return tree


if __name__ == '__main__':
    path = '/Users/zhimingwu/Desktop/sp'
    result = []
    re=jsondir(path)
    print(re)
