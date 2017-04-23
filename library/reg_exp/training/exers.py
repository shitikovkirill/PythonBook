import re
import unittest

gem_mapping = ['Abalone', 'Agate', 'Alexandrite', 'Amazonite', 'Amber', 'Amethyst', 'Andalusite', 'Apatite',
                       'Aquamarine', 'Aragonite', 'Aventurine', 'Azurite', 'Beryl', 'Carnelian', 'Cats Eye',
                       'Chalcedony',
                       'Chrome Diopside', 'Chrysoberyl', 'Chrysophrase', 'Citrine', 'Coral', 'Danburite', 'Druzy',
                       'Emerald',
                       'Garnet', 'Hematite', 'Howlite', 'Iolite', 'Jade', 'Jadeite', 'Jasper', 'Kunzite', 'Kyanite',
                       'Labradorite', 'Lapis', 'Larimar', 'Magnesite', 'Malachite', 'Marcasite', 'Moissanite',
                       'Moonstone',
                       'Morganite', 'Multi-Stone', 'N/A', 'None', 'Obsidian', 'Onyx', 'Opal', 'Peridot', 'Prehnite',
                       'Pyrite',
                       'Quartz', 'Rhodolite', 'Rose de France', 'Rubelite', 'Ruby', 'Sapphire', 'Sardonyx', 'Shell',
                       'Sodalite',
                       'Spessartite', 'Spinel', 'Sugalite', 'Sunstone', 'Tanzanite', 'Tigers Eye', 'Topaz',
                       'Tourmaline',
                       'Tsavorite', 'Turquoise', 'Variscite', 'Zircon', 'Diamond']
pearl_mapping = ['Akoya', 'Baroque', 'Biwa', 'Blister', 'Coin', 'Faux', 'Freshwater', 'Keshi', 'Mabe',
                         'Mother of Pearl', 'Shell', 'South Sea', 'Tahitian']

class TestRegexp(unittest.TestCase):

    def test_regexp(self):
        sub_type = None
        result = None
        category = 'Gemstone'
        name = 'Pear / Amethyst / 0.7ct / 7 x 5 mm / 3 Prong / AA Quality: AA '
        info = '1/10 CT Diamond TW And 3/4 CT TGW Amethyst Fashion Pendant With Chain Pink Silver GH I1;I2'
        res = get_component_type('gemstone', sub_type, category, name, info, gem_mapping, pearl_mapping, result)
        self.assertEqual(None, res)


def get_component_type(component_type, sub_type, category, name, info, gem_mapping, pearl_mapping, result):
    if sub_type:
        if component_type == 'gemstone':
            if sub_type in gem_mapping:
                result = sub_type
        if component_type == 'pearl':
            if sub_type in pearl_mapping:
                result = sub_type
    elif 'diamond' in category.lower():
        result = category
    else:
        regex = re.compile("^.*?\/(.*?)\/")
        data = regex.findall(info)
        if data:
            if component_type == 'gemstone':
                if data[0] in gem_mapping:
                    result = data[0]
            if component_type == 'pearl':
                if data[0] in pearl_mapping:
                    result = data[0]
        else:
            regex = re.compile("TGW\s([A-Za-z]+\s[A-Za-z]+)")
            data = regex.findall(name)
            if data:
                if component_type == 'gemstone':
                    if data[0] in gem_mapping:
                        result = data[0]
                if component_type == 'pearl':
                    if data[0] in pearl_mapping:
                        result = data[0]

    return result

if __name__ == '__main__':
    unittest.main()