import os
from contextlib import closing

import pandas as pd
import requests

save_path_prefix = 'C:\\Users\\jay\\Downloads'


def download(links=None, saving_fold=None):
    for link in links:
        file_name = link.split('/')[-1]
        save_path = saving_fold + file_name
        if not os.path.exists(save_path):
            with closing(requests.get(link)) as r:
                with open(save_path, 'wb') as f:
                    f.write(r.content)
                    print("Downloading " + link)
        else:
            print("file " + save_path + " exists, skipping it")
    print('Have downloaded all file')


if __name__ == '__main__':
    events = pd.read_csv('V2events.csv')
    mentions = pd.read_csv('V2mentions.csv')
    gkg = pd.read_csv('V2gkgs.csv')

    download(events['link'], save_path_prefix + '\\V2events\\')
    download(mentions['link'], save_path_prefix + '\\V2mentions\\')
    download(gkg['link'], save_path_prefix + '\\V2gkgs\\')
