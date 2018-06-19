import time
time1 = time.time()
time2 = time.time()
print('connect time', time2 - time1)

partName = ['P_PARTKEY 0', 'P_NAME 1', 'P_MFGR 2', 'P_BRAND 3', 'P_TYPE 4', 'P_SIZE 5', 'P_CONTAINER 6', 'P_RETAILPRICE 7', 'P_COMMENT 8']
supplierName = ['S_SUPPKEY 0', 'S_NAME 1', 'S_ADDRESS 2', 'S_NATIONKEY 3', 'S_PHONE 4', 'S_ACCTBAL 5', 'S_COMMENT 6']
partsuppName = ['PS_PARTKEY 0', 'PS_SUPPKEY 1','PS_AVAILQTY 2', 'PS_SUPPLYCOST 3','PS_COMMENT 4']
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

fout = open('/home/user31/qmd/joinedData/Q2', 'w')

nationMap = {}
with open(path + 'nation1.tbl', 'r') as file:
	for line in file:
		record = line.split('|')
		nationKey = record[0]
		nationName = record[1]
		regionKey = record[2]
		with open(path + 'region1.tbl', 'r') as file2:
			for line2 in file2:
				record2 = line2.split('|')
				if record2[0] == regionKey:
					nationMap[nationKey] = [nationName, record2[1]]
print(nationMap)

index2 = [0, 5, 4, 2]
index3 = [0, 1, 5, 2, 4, 3, 6]

with open(path + 'partsupp1.tbl', 'r') as file:
	for line in file:
		record = line.split('|')
		record2 = ''
		record3 = ''
		PS_PARTKEY = record[0]
		PS_SUPPKEY = record[1]
		with open(path + 'part1.tbl', 'r') as file2:
			for line2 in file2:
				record2 = line2.split('|')
				if record2[0] == PS_PARTKEY:
					break;
		with open(path + 'supplier1.tbl', 'r') as file3:
			for line3 in file3:
				record3 = line3.split('|')
				if record3[0] == PS_SUPPKEY:
					break;
		count = count + 1
		q = record[index[0]]
		for i in range(0,len(index2)):
			q = q + '|' + record2[index2[i]]
		for i in range(1,len(index3)):
			q = q + '|' + record3[index3[i]]
		nationKey = record3[3]
		q = q + '|' + nationMap[nationKey][0] + '|' + nationMap[nationKey][1]
		fout.write(q + '\n')
		if count % 10000 == 0:
			print(count)
fout.close()
time3 = time.time()
print('insert time', time3 - time2)	
