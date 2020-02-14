# Reference site
# https://qiita.com/komiya-m/items/c37c9bc308d5294d3260

import os
import shutil
import random

def image_dir_train_test_sprit(original_dir, base_dir, train_size=0.8):
    '''
    Image data split to train data and test data

    parameter
    ------------
    original_dir: str
      original directory name
    base_dir: str
      base directory name
    train_size: float
      ratio of train data
    '''
    try:
        os.mkdir(base_dir)
    except FileExistsError:
        print(base_dir + 'is already created.')

    dir_lists = os.listdir(original_dir)
    dir_lists = [f for f in dir_lists if os.path.isdir(os.path.join(original_dir, f))]
    original_dir_path = [os.path.join(original_dir, p) for p in dir_lists]

    num_class = len(dir_lists)

    try:
        train_dir = os.path.join(base_dir, 'train')
        os.mkdir(train_dir)
    except FileExistsError:
        print(train_dir + 'is already created.')

    try:
        validation_dir = os.path.join(base_dir, 'test')
        os.mkdir(validation_dir)
    except FileExistsError:
        print(validation_dir + 'is already created.')

    train_dir_path_lists = []
    val_dir_path_lists = []
    for D in dir_lists:
        train_class_dir_path = os.path.join(train_dir, D)
        try:
            os.mkdir(train_class_dir_path)
        except FileExistsError:
            print(train_class_dir_path + 'is already created.')
        train_dir_path_lists += [train_class_dir_path]
        val_class_dir_path = os.path.join(validation_dir, D)
        try:
            os.mkdir(val_class_dir_path)
        except FileExistsError:
            print(val_class_dir_path + 'is already created.')
        val_dir_path_lists += [val_class_dir_path]


    for i,path in enumerate(original_dir_path):
        files_class = os.listdir(path)
        random.shuffle(files_class)
        num_bunkatu = int(len(files_class) * train_size)
        for fname in files_class[:num_bunkatu]:
            src = os.path.join(path, fname)
            dst = os.path.join(train_dir_path_lists[i], fname)
            shutil.copyfile(src, dst)
        for fname in files_class[num_bunkatu:]:
            src = os.path.join(path, fname)
            dst = os.path.join(val_dir_path_lists[i], fname)
            shutil.copyfile(src, dst)
        print(path + " copy is done")

    print("processing is done")

dataset_root_dir = './data/train'
dataset_split_dir = 'split_dir'
image_dir_train_test_sprit(dataset_root_dir, dataset_split_dir, train_size=0.8)
