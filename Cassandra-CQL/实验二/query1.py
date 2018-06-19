import time
from cassandra.cluster import Cluster
cluster = Cluster(['192.168.152.128', '192.168.152.129', '192.168.152.130'])
session = cluster.connect()
session.default_timeout = 6000
session.set_keyspace('tpch1g')

time1 = time.time()
#rows = session.execute_async('select l_returnflag, l_linestatus, l_quantity, l_extendedprice, l_discount, l_tax from lineitem where l_shipdate = \'1998-09-01\' allow filtering;', [], 6000).result()
rows = session.execute('select l_returnflag, l_linestatus, l_quantity, l_extendedprice, l_discount, l_tax from lineitem where l_shipdate = \'1998-09-01\' allow filtering;', [], 6000)
print(time.time() - time1)

time2 = time.time()
result = {}
for row in rows:
	l_quantity = float(row[2])
	l_extendedprice = float(row[3])
	l_discount = 1.0 - float(row[4])
	l_tax = 1.0 + float(row[5])
	key = row[0] + '|' + row[1]
	if key not in result:
		a = {}
		a[0] = [l_quantity]
		a[1] = [l_extendedprice]
		a[2] = [l_discount]
		a[3] = [l_tax]
		result[key] = a
	else:
		a = result[key]
		a[0].append(l_quantity)
		a[1].append(l_extendedprice)
		a[2].append(l_discount)
		a[3].append(l_tax)

for key in result:
	a = result[key]
	cal = []
	for i in range(0,8):
		cal.append(0.0)
	for i in range(0, len(a[0])):
		cal[0] = cal[0] + a[0][i]
		cal[1] = cal[1] + a[1][i]
		cal[2] = cal[2] + a[1][i] * a[2][i]
		cal[3] = cal[3] + a[1][i] * a[2][i] * a[3][i]
		cal[6] = cal[6] + a[2][i]
	cal[7] = len(a[0])
	cal[4] = cal[0] / cal[7]
	cal[5] = cal[1] / cal[7]
	cal[6] = cal[6] / cal[7]
	print(key, cal)
print('cal time', time.time() - time2)
'''
select
   l_returnflag,
   l_linestatus,
   sum(l_quantity) as sum_qty,
   sum(l_extendedprice) as sum_base_price,
   sum(l_extendedprice*(1-l_discount)) as sum_disc_price,
   sum(l_extendedprice*(1-l_discount)*(1+l_tax)) as sum_charge,
   avg(l_quantity) as avg_qty,
   avg(l_extendedprice) as avg_price,
   avg(l_discount) as avg_disc,
   count(*) as count_order
from
   lineitem
where
   l_shipdate <= date '1998-12-01' - interval '[DELTA]' day (3)
group by
   l_returnflag,
   l_linestatus
order by
   l_returnflag,
   l_linestatus;
'''
