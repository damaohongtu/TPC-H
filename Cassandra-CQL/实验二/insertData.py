import os
import time
#from cassandra.cluster import Cluster
time1 = time.time()
#cluster = Cluster(['node-master'])
#session = cluster.connect()
#session.set_keyspace('tpch1g')

#session.execute('create table partsupp(PS_PARTKEY int,PS_SUPPKEY int, PS_AVAILQTY int, PS_SUPPLYCOST double, PS_COMMENT text, P_NAME text, P_MFGR text, P_BRAND text, P_TYPE text, P_SIZE int, P_CONTAINER text, P_RETAILPRICE double, P_COMMENT text, S_NAME text, S_ADDRESS text, S_NATIONKEY int, S_PHONE text, S_ACCTBAL double, S_COMMENT text, primary key(PS_PARTKEY, PS_SUPPKEY))')
'''
rows = session.execute('select count(*) from lineitem',[],6000)
for i in rows:
	print(i)

'''
path = '/home/hadoop/tpc-h_data/tpc-h_1G/'
fout = open(path + 'temp.tbl','w')
count = 1
part = {}
with open(path + 'part1.tbl', 'r') as file:
        for line in file:
                record = line.split('|')
		part[record[0]] = line

suppliers = {}
with open(path + 'supplier1.tbl', 'r') as file:
	for line in file:
		record = line.split('|')
		suppliers[record[0]] = line

with open(path + 'partsupp1.tbl', 'r') as file:
	for line in file:
		r = line.split('|')
		partkey = r[0]
		suppkey = r[1]
		q = r[0]
		textIndex = [4]
		for i in range(1, len(r)):
			if i in textIndex:
				q = q + ', \'' + r[i] + '\''
			else:
				q = q + ', ' + r[i]
		r = part[partkey].split('|')
		textIndex = [0, 1, 2, 3, 5, 7]
		for i in range(0, len(r)-1):
                        if i in textIndex:
                                q = q + ', \'' + r[i+1] + '\''
                        else:
                                q = q + ', ' + r[i+1]
		r = suppliers[suppkey].split('|')
                textIndex = [0, 1, 3, 5]
                for i in range(0, len(r)-1):
                        if i in textIndex:
                                q = q + ', \'' + r[i+1] + '\''
                        else:
                                q = q + ', ' + r[i+1]
		w = line.strip()
		r = part[partkey].strip().split('|')
		for i in range(1,len(r)):
			w = w + '|' + r[i]
		r = suppliers[suppkey].strip().split('|')
		for i in range(1,len(r)):
			w = w + '|' + r[i]
		fout.write(w + '\n')
		#session.execute('insert into partsupp(PS_PARTKEY, PS_SUPPKEY, PS_AVAILQTY, PS_SUPPLYCOST, PS_COMMENT, P_NAME, P_MFGR, P_BRAND, P_TYPE, P_SIZE, P_CONTAINER, P_RETAILPRICE, P_COMMENT, S_NAME, S_ADDRESS, S_NATIONKEY, S_PHONE, S_ACCTBAL, S_COMMENT) values(' + q +')', [], 6000)
		count = count + 1
		if count % 10000 == 0:
			print(count)
fout.close()
print('insert time 1', time.time() - time1)

#Copy partsupp(PS_PARTKEY, PS_SUPPKEY, PS_AVAILQTY, PS_SUPPLYCOST, PS_COMMENT, P_NAME, P_MFGR, P_BRAND, P_TYPE, P_SIZE, P_CONTAINER, P_RETAILPRICE, P_COMMENT, S_NAME, S_ADDRESS, S_NATIONKEY, S_PHONE, S_ACCTBAL, S_COMMENT) from '/home/hadoop/tpc-h_data/tpc-h_1G/temp.tbl' with DELIMITER = '|';
#session.execute('create table nation(N_NATIONKEY int, N_NAME text, N_REGIONKEY int, N_COMMENT text, R_NAME text, R_COMMENT text, primary key((N_NATIONKEY), R_NAME))')

#session.execute('create table customer(C_CUSTKEY int, C_NAME text, C_ADDRESS text, C_NATIONKEY int, C_PHONE text, C_ACCTBAL double, C_MKTSEGMENT text, C_COMMENT text, primary key(C_CUSTKEY))')

#session.execute('create table orders(O_ORDERKEY int, O_CUSTKEY int, O_ORDERSTATUS text, O_TOTALPRICE double, O_ORDERDATE date, O_ORDERPRIORITY text, O_CLERK text, O_SHIPPRIORITY int, O_COMMENT text, primary key((O_ORDERKEY),O_ORDERDATE))')

#session.execute('create table lineitem(L_ORDERKEY int, L_PARTKEY int, L_SUPPKEY int, L_LINENUMBER int, L_QUANTITY double, L_EXTENDEDPRICE double, L_DISCOUNT double, L_TAX double, L_RETURNFLAG text, L_LINESTATUS text, L_SHIPDATE date, L_COMMITDATE date, L_RECEIPTDATE date, L_SHIPINSTRUCT text, L_SHIPMODE text, L_COMMENT text, primary key((L_ORDERKEY, L_LINENUMBER), L_SHIPDATE))')
