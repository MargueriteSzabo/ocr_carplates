#imports
import pandas as pd
import numpy as np
import json


f = open('../data/train.json')
data = json.load(f)

def json_infos_loading(file):

    plate_infos = pd.DataFrame()
    plate_infos['x_0'] = ""
    plate_infos['x_1'] = ""
    plate_infos['y_0'] = ""
    plate_infos['y_1'] = ""
    plate_infos['text'] = ""
    plate_infos['file'] =  ""
    i = 0

    for plates in file:
        print(i)
        i +=1
        bbox = plates['nums'][0]['box']
        text = plates['nums'][0]['text']
        file = plates['file']


    x_0 = np.min([bbox[0][0], bbox[3][0]])
    y_0 = np.min([bbox[0][1], bbox[1][1]])
    x_1 = np.max([bbox[1][0], bbox[2][0]])
    y_1 = np.max([bbox[2][1], bbox[3][1]])

    if x_0 > x_1:
        x_1, x_0 = x_0, x_1
    if y_0 > y_1:
        y_1, y_0 = y_0, y_1

    new_row = pd.DataFrame({'x_0': x_0, 'x_1': x_1, 'y_0': y_0, 'y_1': y_1,
                            'text': text, 'file':file}, index=[0])
    plate_infos = pd.concat([plate_infos, new_row],ignore_index=True)

    plate_infos.to_csv('../data/plate_infos.csv')

    return plate_infos


if __name__ == '__main':
    json_infos_loading(data)
