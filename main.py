# Task311 Superheroes
# https://github.com/netology-code/py-homeworks-basic/tree/new_oop/9.http.requests

from superheroApi import SuperheroApi

TOKEN = "2619421814940190"


def hero_to_string(hero: ()):
    return f"'{hero[0]}': {hero[-1]}"


def print_resume(heroes: []):
    if len(heroes_intelligence):
        print(f"\nСамый умный из этих героев - {hero_to_string(heroes_intelligence[-1])}")
        if len(heroes_intelligence) > 1:
            print(f"Самый глупый из этих героев - {hero_to_string(heroes_intelligence[0])}")


if __name__ == '__main__':
    heroes = SuperheroApi(token=TOKEN)
    heroes_name_list = ['Captain America',
                        'Hulk',
                        'Thanos',
                        'aaaaaa']
    heroes_intelligence = heroes.get_heroes_intelligence_list(heroes_name_list)
    print_resume(heroes_intelligence)
