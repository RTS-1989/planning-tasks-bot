import os
import requests
from typing import List, Dict

from dotenv import load_dotenv

from countries_app.config_countries import COUNTRIES, COUNTRY_DATA_TO_SEARCH, REGIONS

dotenv_file_path = os.path.join(os.path.dirname(__file__), '../.env')

if dotenv_file_path:
    load_dotenv(dotenv_file_path)


countries_by_region_url = f"{os.getenv('COUNTRIES_URL')}/region/"
country_url = f"{os.getenv('COUNTRIES_URL')}/name/"
all_countries_url = f"{os.getenv('COUNTRIES_URL')}/all"


headers = {
    'x-rapidapi-key': os.getenv('x-rapidapi-key'),
    'x-rapidapi-host': os.getenv('x-rapidapi-host')
    }


def get_country(country_name: str) -> Dict:
    full_url = country_url + f'{country_name}'
    response = requests.get(full_url, headers=headers).json()
    data = {key: value for key, value in response[0].items() if key in COUNTRY_DATA_TO_SEARCH}
    return data


def get_all_countries() -> List:
    response = requests.get(all_countries_url, headers=headers).json()
    data = [item['name'] for item in response]
    return data


def get_countries_by_region(region: str) -> List:
    region_on_english = [item[1] for item in REGIONS.values() if item[0] == region][0]
    full_url = countries_by_region_url + f'{region_on_english}'
    response = requests.get(str(full_url), headers=headers).json()
    data = [country_info['name'] for country_info in response]
    result = [f'{n}. {COUNTRIES[i]}' for n, i in enumerate(data, start=1) for country in COUNTRIES if i == country]
    return result


def get_country_by_message(message: str) -> Dict:
    result = ''
    for key, value in COUNTRIES.items():
        if message.capitalize() in value:
            country_info = get_country(key)
            country_info_list = [value for value in country_info.values()]
            result = {'Название': country_info_list[0], 'Столица': country_info_list[1],
                      'Население': country_info_list[2], 'Границы': country_info_list[3],
                      'Количество соседей': len(country_info_list[3]), 'Валюта': country_info_list[4],
                      'Язык': country_info_list[5]}
    return result
