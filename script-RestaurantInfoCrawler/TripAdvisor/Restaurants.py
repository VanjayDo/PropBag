import argparse
import json
import random
from time import sleep
import logging
import pandas as pd
import requests
from bs4 import BeautifulSoup

PROXY_POOL_URL = 'http://127.0.0.1:8000/?country=国外'  # get https proxies

USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
]


def get_header():
    return {
        'User-Agent': random.choice(USER_AGENTS),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Accept-Encoding': 'gzip, deflate',
    }


def setup_logger(log_file_path, mode='a'):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler(log_file_path, mode=mode)
    fh.setLevel(logging.INFO)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger


def get_proxy():
    if random.randint(0, 10) > 4:  # 50% to use proxy
        all_proxies = json.loads(requests.get(PROXY_POOL_URL).text)
        all_proxies = [i for i in all_proxies if i[2] > 4]
        # logger.info(f'Total proxy num: {len(all_proxies)}')
        picked = random.choice(all_proxies)
        return {'http': f'http://{picked[0]}:{picked[1]}'}
    else:
        sleep(2)  # if use local ip, then set delay
        return None


def request_url(url):
    while True:
        try:
            picked_proxy = get_proxy()
            header = get_header()
            response = requests.get(url, headers=header, timeout=(8, 10), proxies=picked_proxy)
        except:
            # logger.info('Proxy failed once, try again')
            continue
        if response.status_code == 200:
            break
        else:
            sleep(3)
        # logger.info('Request failed once, try again')
    return BeautifulSoup(response.text, 'lxml')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--url_temp', type=str,
                        help='url template, containing PLACEHOLD'
                             'like https://www.tripadvisor.ca/Restaurants-g155032-oaPLACEHOLD-Montreal_Quebec.html')
    parser.add_argument('--saving_path', type=str, help='saving path of csv file storing results')
    args = parser.parse_args()
    logger = setup_logger("spider_4_TripAdvisor_restaurants.log", mode='w')

    df = pd.DataFrame(columns=['name', 'link', 'tel', 'email', 'website', 'addr', 'rank', 'ratings', 'review_num'])
    first_page = args.url_temp.replace('PLACEHOLD', '0')
    soup = request_url(first_page)
    PAGE_NUM = int(soup.select('div[class="pageNumbers"] a[class="pageNum taLnk"]')[-1].text.replace(u'\n', u''))
    logger.info(f'Total {PAGE_NUM} pages')

    counter = 1
    for page_num in range(0, PAGE_NUM):
        logger.info(f'Processing the {page_num}th page...')
        current_page = args.url_temp.replace('PLACEHOLD', str(page_num * 30))
        soup = request_url(current_page)
        selector = soup.select('div[class="_1kXteagE"]')[0]
        for i in range(30):
            try:
                selected_restaurant = selector.select(f'div[data-test="{counter}_list_item"] div[class=wQjYiB7z] a')[0]
            except:
                # after finishing, will be confronted with this exception, break to save the info on the last page
                break
            counter += 1
            if counter % 10 == 0:
                logger.info(f'Finished {counter}')
            restaurant_name = selected_restaurant.text.split('. ')[-1]  # get name, split is to remove number like '1. '
            restaurant_link = 'http://www.tripadvisor.ca' + selected_restaurant['href']  # get link

            current_soup = request_url(restaurant_link)
            try:
                restaurant_rank = current_soup.select('span[class="_13OzAOXO _2VxaSjVD"] a[class="_15QfMZ2L"]')[0].text
            except:
                restaurant_rank = None
                logger.info(f'Got exception while processing "{restaurant_name}" restaurant_rank, '
                            f'link is {restaurant_link}')
            try:
                restaurant_addr = current_soup.select('span[class="_13OzAOXO _2VxaSjVD"] a[class="_15QfMZ2L"]')[1].text
            except:
                restaurant_addr = None
                logger.info(f'Got exception while processing "{restaurant_name}" restaurant_addr, '
                            f'link is {restaurant_link}')
            try:
                restaurant_tel = current_soup.select('span[class="_13OzAOXO _2VxaSjVD"] a[class="_3S6pHEQs"]')[0].text
            except:
                restaurant_tel = None
                logger.info(f'Got exception while processing "{restaurant_name}" restaurant_tel, '
                            f'link is {restaurant_link}')
            try:
                restaurant_ratings = current_soup.select(
                    'div[class="Ct2OcWS4"] span[class="r2Cf69qf"]')[0].text.replace(u'\xa0', u'')
            except:
                restaurant_ratings = None
                logger.info(
                    f'Got exception while processing "{restaurant_name}" restaurant_ratings, link is {restaurant_link}')
            try:
                restaurant_review_num = current_soup.select('a[class="_10Iv7dOs"]')[0].text.split(' reviews')[0]
            except:
                restaurant_review_num = None
                logger.info(f'Got exception while processing "{restaurant_name}" restaurant_review_num, '
                            f'link is {restaurant_link}')
            try:
                restaurant_website = current_soup.select(
                    'span[class="_13OzAOXO _2VxaSjVD"] a[class="_2wKz--mA _15QfMZ2L"]')[0]['href']
            except:
                restaurant_website = None
                logger.info(f'Got exception while processing "{restaurant_name}" restaurant_website, '
                            f'link is {restaurant_link}')
            try:
                restaurant_email = current_soup.select('span[class="ui_icon email _3ZW3afUk"]')[0].parent['href'] \
                    .split('?subject=?')[0].split('mailto:')[-1]
            except:
                restaurant_email = None
                logger.info(
                    f'Got exception while processing "{restaurant_name}" restaurant_email, link is {restaurant_link}')
            info_dict = {'name': restaurant_name, 'link': restaurant_link, 'tel': restaurant_tel,
                         'email': restaurant_email, 'website': restaurant_website, 'addr': restaurant_addr,
                         'rank': restaurant_rank, 'ratings': restaurant_ratings, 'review_num': restaurant_review_num}
            df = df.append(info_dict, ignore_index=True)
        df.to_csv(args.saving_path)  # save after each page finished
