import time
#from cassandra.cluster import Cluster
#cluster = Cluster()
time1 = time.time()
#session = cluster.connect()
#session.set_keyspace('tpch1g')
time2 = time.time()
print('connect time', time2 - time1)

partName = ['P_PARTKEY', 'P_NAME', 'P_MFGR', 'P_BRAND', 'P_TYPE', 'P_SIZE', 'P_CONTAINER', 'P_RETAILPRICE', 'P_COMMENT']
supplierName = ['S_SUPPKEY', 'S_NAME', 'S_ADDRESS', 'S_NATIONKEY', 'S_PHONE', 'S_ACCTBAL', 'S_COMMENT']
customerName = ['C_CUSTKEY', 'C_NAME', 'C_ADDRESS', 'C_NATIONKEY', 'C_PHONE', 'C_ACCTBAL', 'C_MKTSEGMENT', 'C_COMMENT']
ordersName = ['O_ORDERKEY', 'O_CUSTKEY', 'O_ORDERSTATUS', 'O_TOTALPRICE', 'O_ORDERDATE', 'O_ORDERPRIORITY', 'O_CLERK', 'O_SHIPPRIORITY', 'O_COMMENT']
lineitemName = ['L_ORDERKEY 0', 'L_PARTKEY 1', 'L_SUPPKEY 2', 'L_LINENUMBER 3', 'L_QUANTITY 4', 'L_EXTENDEDPRICE 5', 'L_DISCOUNT 6', 'L_TAX 7', 'L_RETURNFLAG 8', 'L_LINESTATUS 9', 'L_SHIPDATE 10', 'L_COMMITDATE 11', 'L_RECEIPTDATE 12', 'L_SHIPINSTRUCT 13', 'L_SHIPMODE 14', 'L_COMMENT 15']
nationName = ['n_nationkey', 'n_name', 'n_regionkey', 'n_comment']
regionName = ['R_REGIONKEY', 'R_NAME', 'R_COMMENT']

#session.execute("CREATE TABLE IF NOT EXISTS TPCH_Q1 ( L_ORDERKEY int, L_LINENUMBER int, L_QUANTITY double, L_EXTENDEDPRICE double, L_DISCOUNT double, L_TAX double, L_RETURNFLAG text, L_LINESTATUS text, L_SHIPDATE date, PRIMARY KEY ((l_returnflag, l_linestatus), l_shipdate, l_orderkey, l_linenumber) );")

index = [0, 3, 4, 5, 6, 7, 8, 9, 10]
textIndex = [6, 7, 8]
path = '/home/user31/tpc-h_data/tpc-h_1G/'

count = 1

fout = open('/home/user31/qmd/joinedData/Q1', 'w')
with open(path + 'lineitem1.tbl', 'r') as file:
	for line in file:
		record = line.split('|')
		#q = 'insert into TPCH_Q1(L_ORDERKEY, L_LINENUMBER, L_QUANTITY, L_EXTENDEDPRICE, L_DISCOUNT, L_TAX, L_RETURNFLAG, L_LINESTATUS, L_SHIPDATE) values(' + record[index[0]]
		#for i in range(1,len(index)):
		#	if i in textIndex:
		#		q = q + ', \'' + record[index[i]] + '\''
		#	else:
		#		q = q + ', ' + record[index[i]]
		#q = q + ');'
		count = count + 1
		q = record[index[0]]
		for i in range(1,len(index)):
			q = q + '|' + record[index[i]]
		fout.write(q + '\n')
		if count % 10000 == 0:
			print(count)
		#session.execute(q)
fout.close()
time3 = time.time()
print('insert time', time3 - time2)	
