import re
import unittest


class TestRegexp(unittest.TestCase):

    def test_regexp(self):
        orders_str = '50 orders: IC2200026658-0, [STK13705316-0, WMT488056569-0], STK13705316-1 WARNING! 3 orders have not been processed and printed: CSD500200646386-0, [IC2200027021-0, CSD500200646387-0] '
        result = self.get_orders_list_from_string(orders_str)
        self.assertEqual(['IC2200026658-0', 'STK13705316-0', 'WMT488056569-0', 'STK13705316-1', 'WARNING', 'CSD500200646386-0', 'IC2200027021-0', 'CSD500200646387-0', ''],
                         result)

        result = self.get_orders_list_from_string('')
        self.assertEqual([''], result)

        result = self.get_orders_list_from_string('dfsd dsfsdf')
        self.assertEqual([''], result)

    def get_orders_list_from_string(self, string):
        regex = re.compile(r"(?<=:\s)(?P<orders_list>\[?[\w-]*,?\s*\]?){1,}")
        list_of_orders = regex.finditer(string)
        orders_str = ', '.join([value.group(0) for value in list_of_orders])
        orders_str = re.sub('\[|\]', '', orders_str)
        return re.split('\s*,?\s+', orders_str)

    def test_format(self):

        sql = """INSERT INTO tagging_order (name, order_list, active, order_list_confirm, latest_touch_uid, create_uid,  write_uid)
                            VALUES ('{4:s}', '{1:s}', {2:s}, {3:s}, {0:d}, {0:d}, {0:d})"""

        order_ids = ['OS141036916-0', 'OS141056549-0', 'OS141042201-0', 'OS141045775-0', '']
        uid = 12
        tagging_order_name = 'SO_01.06.13qq'

        result = sql.format(uid, '\n'.join(order_ids), 'TRUE', 'FALSE', tagging_order_name)

        sql = """INSERT INTO tagging_order (name, order_list, active, order_list_confirm, latest_touch_uid, create_uid,  write_uid)
        VALUES ('%s', '%s', %s, %s, %d, %d, %d)"""
        result = sql % (tagging_order_name, '\n'.join(order_ids), 'TRUE', 'FALSE', uid, uid, uid)

        #print(result)


if __name__ == '__main__':
    unittest.main()