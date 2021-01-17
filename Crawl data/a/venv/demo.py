import requests
import csv
import json
import time
from random import randint
import random
headers = {
    # 'User-Agent': 'Mozilla/5.0',
    'User-Agent': 'Chrome/87.0.4280.88',
    'Referer': 'https://shopee.vn/'
}
i=0
a=0
options=0
options_count=0
with open('C:\\Users\\LAPTOPSIEUBEN\\Desktop\\ao.csv', mode='a',newline='',encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # way to write to csv file
    writer.writerow(['Name',
                     'price',
                     'sold',
                     'discount',
                     'liked-count',
                     'ads_keyword',
                     'cmt_count',
                     'stock',
                     'view_count',
                     'price_before_discount',
                     'price_min',
                     'price_max',
                     'price_min_before_discount',
                     'price_max_before_discount',
                     'rating_star',
                     'rating_count',
                     'rating_count_total',
                     'rcount_with_image',
                     'rcount_with_context',
                     'options',
                     'options_count',
                     'image',
                     'itemid',
                     'shopid',
                     'catid',
                     'shop_location',
                     'video_info_list_duration',])
    while(i<8050):
        a = ("https://shopee.vn/api/v2/search_items/?by=relevancy&keyword=%C3%A1o%20nam&limit=50&newest=",str(i),"&order=desc&page_type=search&version=2")
        url = "".join(a)
        r = requests.get(url, headers=headers).json()
        for item in r['items']:
            if item['video_info_list']:
                a = item['video_info_list'][0]['duration']
            else:
                a = 0
            if item['tier_variations']:
                options = item['tier_variations'][0]['options']
                options_count = len(item['tier_variations'][0]['options'])
            else:
                options = 0
                a = 0
            writer.writerow([item['name'],
                             item['price']/100,
                             item['sold'],
                             item['discount'],
                             item['liked_count'],
                             item['ads_keyword'],
                             item['cmt_count'],
                             item['stock'],
                             item['view_count'],
                             item['price_before_discount'],
                             item['price_min'],
                             item['price_max'],
                             item['price_min_before_discount'],
                             item['price_max_before_discount'],
                             item['item_rating']['rating_star'],
                             item['item_rating']['rating_count'],
                             item['item_rating']['rating_count'][0],
                             item['item_rating']['rcount_with_image'],
                             item['item_rating']['rcount_with_context'],
                             options,
                             options_count,
                             item['image'],
                             item['itemid'],
                             item['shopid'],
                             item['catid'],
                             item['shop_location'],
                             a])
            print(i, "---",
                  item['name'],
                  item['name'],
                  item['price'] / 100,
                  item['sold'],
                  item['discount'],
                  item['liked_count'],
                  item['ads_keyword'],
                  item['cmt_count'],
                  item['stock'],
                  item['view_count'],
                  item['price_before_discount'],
                  item['price_min'],
                  item['price_max'],)
        i=i+50
        time.sleep(1)
file.close()