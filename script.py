#!/usr/bin/env python3

import requests
from requests.exceptions import ConnectionError
from requests.exceptions import HTTPError


URL = 'http://wttr.in'


def get_weather(city, lang='en', unit='u'):
    payload = {
        'n': '',
        'T': '',
        'q': '',
        unit: '',
        'lang': lang
    }

    url = '{}/{}'.format(URL, city)
    response = requests.get(url, params=payload)
    response.raise_for_status()

    return response.text


def main():
    cities = [
        {'name': 'London', 'lang': 'en', 'unit': 'u'},
        {'name': 'Шереметьево', 'lang': 'ru', 'unit': 'm'},
        {'name': 'Череповец', 'lang': 'ru', 'unit': 'm'}
    ]

    for city in cities:
        try:
            result = get_weather(city['name'], lang=city['lang'], unit=city['unit'])

        except (ConnectionError, HTTPError):
            if city['lang'] == 'ru':
                error_message = 'Не удалось получить информацию о погоде в "{}"'
            else:
                error_message = 'Couldn\'t get weather info for "{}"'
            print(error_message.format(city['name']))

        else:
            print(result)


if __name__ == '__main__':
    main()
