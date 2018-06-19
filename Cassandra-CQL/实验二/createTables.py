from cassandra.cluster import Cluster
cluster = Cluster(['node-master'])
session = cluster.connect()
session.set_keyspace('tpch1g')

session.execute('create table partsupp(PS_PARTKEY int,PS_SUPPKEY int, PS_AVAILQTY int, PS_SUPPLYCOST double, PS_COMMENT text, P_NAME text, P_MFGR text, P_BRAND text, P_TYPE text, P_SIZE int, P_CONTAINER text, P_RETAILPRICE double, P_COMMENT text, S_NAME text, S_ADDRESS text, S_NATIONKEY int, S_PHONE text, S_ACCTBAL double, S_COMMENT text, primary key(PS_PARTKEY, PS_SUPPKEY))')

session.execute('create table nation(N_NATIONKEY int, N_NAME text, N_REGIONKEY int, N_COMMENT text, R_NAME text, R_COMMENT text, primary key((N_NATIONKEY), R_NAME))')

session.execute('create table customer(C_CUSTKEY int, C_NAME text, C_ADDRESS text, C_NATIONKEY int, C_PHONE text, C_ACCTBAL double, C_MKTSEGMENT text, C_COMMENT text, primary key(C_CUSTKEY))')

session.execute('create table orders(O_ORDERKEY int, O_CUSTKEY int, O_ORDERSTATUS text, O_TOTALPRICE double, O_ORDERDATE date, O_ORDERPRIORITY text, O_CLERK text, O_SHIPPRIORITY int, O_COMMENT text, primary key((O_ORDERKEY),O_ORDERDATE))')

session.execute('create table lineitem(L_ORDERKEY int, L_PARTKEY int, L_SUPPKEY int, L_LINENUMBER int, L_QUANTITY double, L_EXTENDEDPRICE double, L_DISCOUNT double, L_TAX double, L_RETURNFLAG text, L_LINESTATUS text, L_SHIPDATE date, L_COMMITDATE date, L_RECEIPTDATE date, L_SHIPINSTRUCT text, L_SHIPMODE text, L_COMMENT text, primary key((L_ORDERKEY, L_LINENUMBER), L_SHIPDATE))')
