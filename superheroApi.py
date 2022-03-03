from pprint import pprint

import requests


def get_sorted_list(simple_dict: {}):
    list_from_dict = list(simple_dict.items())
    list_from_dict.sort(key=lambda i: i[1])
    return list_from_dict


class SuperheroApi:

    def __init__(self, token: str):
        self.token = token

    def get_address_api(self):
        return 'https://superheroapi.com/api/' + self.token

    def get_heroes_intelligence_list(self, names_list):
        print(f'\nНайдём самого умного в списке героев {names_list} ...')
        intelligences = dict()
        for name in names_list:
            print()
            api_url = f'{self.get_address_api()}/search/{name}'
            response = requests.get(api_url)
            # pprint(response.json())
            if int(response.status_code) / 100 == 2:
                if response.json()['response'] == 'error':
                    print(f"'{name}'  - isn't found data!")
                    continue
                for result_dict in response.json()['results']:
                    hero_name = result_dict['name']
                    print(f"'{hero_name}'", end='')
                    if hero_name == name:
                        intelligence = result_dict['powerstats']['intelligence']
                        intelligences[hero_name] = int(intelligence)
                        print(f': {intelligence}')
                    else:
                        print("  - isn't an exact match!")
            else:
                print(response.status_code)
        return get_sorted_list(intelligences)
