# country_codes.py

# from pygal_maps_world.i18n import COUNTRIES
from pygal_maps_world.i18n import COUNTRIES
def get_country_code(country_name):
    '''функция возвращает для заданной страны её код Pygal, состоящий из 2 букв'''
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        # Если страна не найдена, вернуть None
    return None

