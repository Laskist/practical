import os
import pickle
from pathlib import Path
import json
import csv


def recurs(path: str):
    path = Path(path)
    my_list = []

    for i in Path.iterdir(path):
        if Path.is_file(i):
            res = {'Path': str(i), "File?": Path.is_file(i), 'Dir?': Path.is_dir(i), 'size': os.path.getsize(i)}
            my_list.append(res)
        else:
            res = {'Path': str(i), "File?": Path.is_file(i), 'Dir?': Path.is_dir(i), 'size': os.path.getsize(i)}
            my_list.append(res)
            recurs(i)
    with open('./data.json', 'a') as f:
        json.dump(my_list, f, indent=2, separators=(',', ':'))
    with open('./data.сsv', 'a', newline='', encoding='utf-8') as f_write:
        writer = csv.DictWriter(f_write, fieldnames=my_list[0], dialect='excel-tab')
        writer.writeheader()
        writer.writerows(my_list)
    with open('./data.pickle', 'wb') as f_w:
        pickle.dump(my_list, f_w)



