import os
import requests
from lxml import html

etree = html.etree

gkg_save_path_prefix = "/Volumes/I'm mobile HD/V1GKG/"
events_save_path_prefix = "/Volumes/I'm mobile HD/V1events/"

domain = "http://data.gdeltproject.org/"
gkg_src = "gkg/index.html"
events_src = "events/index.html"


def download_func(src, kind, save_path_prefix):
    response = requests.get(domain + src).text
    html_source_code = etree.HTML(response)
    selector = html_source_code.xpath("/html/body/ul/li/a")
    total_num = len(selector)
    count = 0
    downloaded = 0

    for i in selector:
        count += 1
        if i.xpath('./text()'):
            file_name = i.xpath('./text()')[0]
            download_link = domain + kind + '/' + file_name
            save_path = save_path_prefix + file_name
            if not os.path.exists(save_path):
                r = requests.get(download_link)
                print("Downloading " + download_link)
                with open(save_path, 'wb') as f:
                    f.write(r.content)
            else:
                print("file " + save_path + " exists, skipping it")
            downloaded += 1
        else:
            print("this element has no download link")
    print('total num is', total_num, ', and the count is ', count, ', downloaded is ', downloaded)


if __name__ == "__main__":
    download_func(gkg_src, "gkg", gkg_save_path_prefix)
    download_func(events_src, 'events', events_save_path_prefix)
