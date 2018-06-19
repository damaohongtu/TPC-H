import os
import time
from cassandra.cluster import Cluster
time1 = time.time()
cluster = Cluster(['node-master'])
session = cluster.connect()
session.set_keyspace('tpch1g')

#session.execute('create table partsupp(PS_PARTKEY int,PS_SUPPKEY int, PS_AVAILQTY int, PS_SUPPLYCOST double, PS_COMMENT text, P_NAME text, P_MFGR text, P_BRAND text, P_TYPE text, P_SIZE int, P_CONTAINER text, P_RETAILPRICE double, P_COMMENT text, S_NAME text, S_ADDRESS text, S_NATIONKEY int, S_PHONE text, S_ACCTBAL double, S_COMMENT text, primary key(PS_PARTKEY, PS_SUPPKEY))')

path = '/home/hadoop/tpc-h_data/tpc-h_1G/'

#session.execute('create table nation(N_NATIONKEY int, N_NAME text, N_REGIONKEY int, N_COMMENT text, R_NAME text, R_COMMENT text, primary key((N_NATIONKEY), R_NAME))')

count = 1
region = {}
with open(path + 'region1.tbl', 'r') as file:
        for line in file:
                record = line.split('|')
		region[record[0]] = line

with open(path + 'nation1.tbl', 'r') as file:
	for line in file:
		r = line.split('|')
		regionkey = r[2]
		q = r[0]
		textIndex = [1,3]
		for i in range(1, len(r)):
			if i in textIndex:
				q = q + ', \'' + r[i] + '\''
			else:
				q = q + ', ' + r[i]
		r = region[regionkey].split('|')
		textIndex = [1,2]
                for i in range(1, len(r)):
                        if i in textIndex:
                                q = q + ', \'' + r[i] + '\''
                        else:
                                q = q + ', ' + r[i]
		session.execute('insert into nation(N_NATIONKEY, N_NAME,  N_REGIONKEY, N_COMMENT, R_NAME, R_COMMENT) values(' + q +')', [], 6000)
		count = count + 1
		if count % 10000 == 0:
			print(count)
time2 = time.time()
print('insert time 1', time2 - time1)


#session.execute('create table customer(C_CUSTKEY int, C_NAME text, C_ADDRESS text, C_NATIONKEY int, C_PHONE text, C_ACCTBAL double, C_MKTSEGMENT text, C_COMMENT text, primary key(C_CUSTKEY))')
#session.execute('Copy customer(C_CUSTKEY, C_NAME, C_ADDRESS, C_NATIONKEY, C_PHONE, C_ACCTBAL, C_MKTSEGMENT, C_COMMENT) from \'/home/user31/tpc-h_data/tpc-h_1G/customer1.tbl\' with DELIMITER = \'|\';',[], 6000)

#session.execute('create table orders(O_ORDERKEY int, O_CUSTKEY int, O_ORDERSTATUS text, O_TOTALPRICE double, O_ORDERDATE date, O_ORDERPRIORITY text, O_CLERK text, O_SHIPPRIORITY int, O_COMMENT text, primary key((O_ORDERKEY),O_ORDERDATE))')
#session.execute('Copy orders(O_ORDERKEY, O_CUSTKEY, O_ORDERSTATUS, O_TOTALPRICE, O_ORDERDATE, O_ORDERPRIORITY, O_CLERK, O_SHIPPRIORITY, O_COMMENT) from \'/home/user31/tpc-h_data/tpc-h_1G/orders1.tbl\' with DELIMITER = \'|\';', [], 6000)

#session.execute('create table lineitem(L_ORDERKEY int, L_PARTKEY int, L_SUPPKEY int, L_LINENUMBER int, L_QUANTITY double, L_EXTENDEDPRICE double, L_DISCOUNT double, L_TAX double, L_RETURNFLAG text, L_LINESTATUS text, L_SHIPDATE date, L_COMMITDATE date, L_RECEIPTDATE date, L_SHIPINSTRUCT text, L_SHIPMODE text, L_COMMENT text, primary key((L_ORDERKEY, L_LINENUMBER), L_SHIPDATE))')
#session.execute('Copy lineitem(L_ORDERKEY, L_PARTKEY, L_SUPPKEY, L_LINENUMBER, L_QUANTITY, L_EXTENDEDPRICE, L_DISCOUNT, L_TAX, L_RETURNFLAG, L_LINESTATUS, L_SHIPDATE, L_COMMITDATE, L_RECEIPTDATE, L_SHIPINSTRUCT, L_SHIPMODE, L_COMMENT) from \'/home/user31/tpc-h_data/tpc-h_1G/lineitem1.tbl\' with DELIMITER = \'|\';', [], 6000)
#print('insert time2', time.time() - time2)
