import time
from cassandra.cluster import Cluster
cluster = Cluster(['192.168.152.128', '192.168.152.129', '192.168.152.130'])
session = cluster.connect()
session.set_keyspace('tpch1g')

time1 = time.time()
'''
future = session.execute_async('select l_returnflag, l_linestatus, l_quantity, l_extendedprice, l_discount, l_tax from lineitem where l_shipdate = \'1998-09-01\' allow filtering;', [], 6000)
print(time.time() - time1)
rows = session.execute('select l_returnflag, l_linestatus, l_quantity, l_extendedprice, l_discount, l_tax from lineitem where l_shipdate = \'1998-09-01\' allow filtering;', [], 6000)
'''

rows = session.execute('select n_nationkey, n_name from nation where r_name = \'EUROPE\' allow filtering;' ,[], 6000)

finalRows = []
minCost = 1000.0;
minRow = []
for row in rows:
	n_nationkey = int(row[0])
	rows3 = session.execute('select s_acctbal, s_name, ps_partkey, p_mfgr, s_address, s_phone, s_comment, p_type, ps_supplycost,s_nationkey  from partsupp where p_size = 15 and s_nationkey = ' + str(row[0]) + ' allow filtering;', [], 6000)
	for row3 in rows3:
	        if row3[7].find('BRASS') != -1:
			if row3[8] < minCost:
				minCost = row3[8]
				minRow = row3
print(minRow)
print(time.time() - time1)
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
