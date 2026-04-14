# -*- coding: utf-8 -*-
import urllib.request
import datetime
import json

client_id = 'RqqpPopQZ0Z1eECHbMbT'
client_secret = 'oWHbdS9PTC'

def main():

    node = 'news'                                             # 크롤링할 대상
    srcText = input('검색어를 입력하세요: ')
    