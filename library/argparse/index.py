import argparse

parser = argparse.ArgumentParser(description='Some items.')
parser.add_argument('items', metavar='Item', type=str, nargs='+',
                    help="""Items""")

parser.add_argument('--type', choices=['invoice_no', 'name', 'po_number'], type=str, default='invoice_no',
                    help="""Type of items such as: 'invoice_no', 'name', 'po_number'.""")

args = parser.parse_args()

print('type = {}'.format(args.type))
print('Count of items: {}'.format(len(args.items)))
print(args)


def get_ids_all(type_f, items):
    if type_f == 'po_number':
        type_f = 'so.{}'.format(type_f)
    else:
        type_f = 'sp.{}'.format(type_f)

    sql = """
    SELECT
      sp.id   AS id,
      sp.name AS name
    FROM
      stock_picking AS sp
      LEFT JOIN
      sale_order AS so
        ON so.id = sp.sale_id
      LEFT JOIN
      res_partner AS rp
        ON rp.id = so.partner_id
      LEFT JOIN
      res_partner_address AS ra
        ON ra.id = sp.address_id
    WHERE 1 = 1
          AND {field} IN ('{items}')
          AND sp.state = 'done'
    """.format(field=type_f, items="', '".join(items))
    print(sql)

print()
get_ids_all(args.type, args.items)
