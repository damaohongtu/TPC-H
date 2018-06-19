import time

from cassandra.cluster import Cluster
cluster = Cluster(['192.168.152.128', '192.168.152.129', '192.168.152.130'])
session = cluster.connect()
session.set_keyspace('tpch1g')
'''
time1 = time.time()
future = session.execute_async('select l_returnflag, l_linestatus, l_quantity, l_extendedprice, l_discount, l_tax from lineitem where l_shipdate = \'1998-09-01\' allow filtering;', [], 6000)
print(time.time() - time1)
rows = session.execute('select l_returnflag, l_linestatus, l_quantity, l_extendedprice, l_discount, l_tax from lineitem where l_shipdate = \'1998-09-01\' allow filtering;', [], 6000)
'''

orders = session.execute('select o_orderkey, o_custkey from orders where o_orderdate >= \'1994-01-01\' and o_orderdate < \'1995-01-01\' allow filtering;' ,[], 6000)
rows2 = session.execute('select n_nationkey, n_name from nation where r_name = \'ASIA\' allow filtering;', [], 6000)
for row2 in rows2:
	supps = session.execute('select ps_suppkey from partsupp where s_nationkey = ' + str(row2[0]) + ' allow filtering;', [], 6000)
	custs = session.execute('select c_custkey from customer where c_nationkey = ' + str(row2[0]) + ' allow filtering;', [], 6000)
	finalRows = []
	supp = set()
	for row in supps:
		supp.add(row[0])
	cust = set()
	for row in custs:
		cust.add(row[0])
	for order in orders:
		if order[1] in cust:
			rows3 = session.execute('select l_extendedprice, l_discount, l_suppkey from lineitem where l_orderkey = ' + str(order[0]) + ' allow filtering')
			for row3 in rows3:
				if row3[2] in supp:
					finalRows.append(row3)

	revenue = 0.0
	for row in finalRows:
		revenue = revenue + float(row[0]) * (1.0 - float(row[1]))		
	print(str(revenue) +  row2[1])
'''
rows = [['a', '1', '1', '1', '1', '1'], ['a','1','3','3','3','3'], ['b', '2', '2', '2', '2', '2']]
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
'''
select
s_acctbal,
s_name,
n_name,
p_partkey,
p_mfgr,
s_address,
s_phone,
s_comment
from
part,
supplier,
partsupp,
nation,
region
where
p_partkey = ps_partkey
and s_suppkey = ps_suppkey
and p_size = [SIZE]
and p_type like '%[TYPE]'
and s_nationkey = n_nationkey
and n_regionkey = r_regionkey
and r_name = '[REGION]'
and ps_supplycost = (
selectTPC BenchmarkTM H Standard Specification Revision 2.17.3 Page 31
min(ps_supplycost)
from
partsupp, supplier,
nation, region
where
p_partkey = ps_partkey
and s_suppkey = ps_suppkey
and s_nationkey = n_nationkey
and n_regionkey = r_regionkey
and r_name = '[REGION]'
)
order by
s_acctbal desc,
n_name,
s_name,
p_partkey;
'''
