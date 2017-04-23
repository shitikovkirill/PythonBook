component_type = args[0].lower() if args[0] else ''
component_num = args[1]

context = locals()
product_id = context.get('product_id', False)
result = ''
types = []

for type in component_type.split(','):
  types.append("pc.name ilike '%%" + type.strip() + "%%'")

types_sql = ' or '.join(types)

if product_id:
  check_sql = """
    select
      fm."Prod_setting_type" as "setting",
      case when pc.name ilike '%%metal%%' then pl.quantity else cht.weight end as "weight",
      pc.name as "category"
    from product_product p
    left join product_template t on t.id = p.product_tmpl_id
    left join product_pack_line pl on pl.parent_product_id = p.id
    left join product_product chp on chp.id = pl.product_id
    left join product_template cht on cht.id = chp.product_tmpl_id
    left join product_category pc on pc.id = cht.categ_id
    left join fm_cmp_9_08 fm on
      trim(fm."ID_delmar") = trim(p.default_code)
      and lower(pc.name) = lower(fm.prod_type)
      and (fm."ID_delmar_familly" = chp.default_code or fm."ID_delmar_familly" = 'M_' || chp.default_code)
    where 1=1
      and p.id = %s
      and pc.name not ilike '%%labor%%'
      and (%s)
    order by COALESCE(cht.weight, pl.weight,0) DESC, cht.id
  """ % (product_id, types_sql)

  cr.execute(check_sql)
  res = cr.dictfetchall()

  if component_num and component_num <= len(res):
    setting = res[component_num-1]['setting']
    if setting:
      result = setting
