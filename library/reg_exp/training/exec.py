import re
import unittest


class TestRegexp(unittest.TestCase):

    def test_regexp(self):
        orders_str = '8 combined orders: [PUPDL141103.X2_5X1-0R, PUPDL141103X2_4X1-0R], [PUPDL141104X24X1-0, PUPDL141104X25X1-0]'
        result = self.get_orders_list_from_string(orders_str)
        self.assertEqual(['PUPDL141103.X2_5X1-0R', 'PUPDL141103X2_4X1-0R', 'PUPDL141104X24X1-0', 'PUPDL141104X25X1-0'],
                         result)

        result = self.get_orders_list_from_string('')
        self.assertEqual([], result)

        result = self.get_orders_list_from_string('dfsd dsfsdf')
        self.assertEqual([], result)

    def get_orders_list_from_string(self, string):
        regex = re.compile(r"(?<=:\s)(?P<orders_list>\[?[A-Z\d\-\._]{4,}[,?\s\]]?,?\s*){1,}")
        list_of_orders = regex.finditer(string)
        orders_str = ', '.join([value.group(0) for value in list_of_orders])
        orders_str = re.sub('\[|\]', '', orders_str)
        orders = re.split('\s*,?\s+', orders_str)
        new_orders = []
        for order in orders:
            letter = re.search(r"[A-Z]", order)
            number = re.search(r"\d", order)
            dash   = re.search(r"-", order)

            if not (letter and number and dash):
                continue
            new_orders.append(order)
        return new_orders

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