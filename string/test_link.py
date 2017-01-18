
import unittest

def generate_catalog_linc(tab_id, product_id):
    #context = locals()

    #tab_id = 1484122289
    #product_id = context.get('product_id', False)

    if tab_id and product_id:
        url = 'https://catalog.delmarintl.ca/?tabId=%d#/product/%d/1/false/sales/{"period":"quarter","size":"all"}'%(tab_id, product_id)
    else:
        url=''
    return url

class TestStringMethods(unittest.TestCase):

    def test_base(self):
        self.assertEqual('https://catalog.delmarintl.ca/?tabId=23123#/product/11111/1/false/sales/{"period":"quarter","size":"all"}', generate_catalog_linc(23123, 11111))

    def test_return_empty_string(self):
        self.assertEqual('', generate_catalog_linc(False, 11111))
        self.assertEqual('', generate_catalog_linc(312312, False))
        self.assertEqual('', generate_catalog_linc(False, False))


if __name__ == '__main__':
    unittest.main()


