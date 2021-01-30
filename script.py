#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from requests.exceptions import ConnectionError
from requests.exceptions import HTTPError


URL = 'http://wttr.in'


def get_weather(city):
    url = '{}/{}'.format(URL, city)
    payload = {
        'lang': 'ru',
        'm': ''
    }
    try:
        response = requests.get(url, params=payload)
        response.raise_for_status()
    except (ConnectionError, HTTPError):
        print('Не удалось получитьь погоду в "{}"'.format(city))
    else:
        print(response.text)


def main():
    for city in ['Лондон', 'Шереметьево', 'Череповец']:
        get_weather(city)


if __name__ == '__main__':
    main()
