import time
from cassandra.cluster import Cluster
cluster = Cluster()
time1 = time.time()
session = cluster.connect()
session.set_keyspace('tpch1g')
time2 = time.time()
print('connect time', time2 - time1)

row = session.execute('select count(*) from lineitem')
print(row, time.time() - time2)


#session.execute("CREATE TABLE IF NOT EXISTS TPCH_Q1 ( L_ORDERKEY int, L_LINENUMBER int, L_QUANTITY double, L_EXTENDEDPRICE double, L_DISCOUNT double, L_TAX double, L_RETURNFLAG text, L_LINESTATUS text, L_SHIPDATE date, PRIMARY KEY ((l_returnflag, l_linestatus), l_shipdate, l_orderkey, l_linenumber) );")

#session.execute("Copy TPCH_Q1(L_ORDERKEY, L_LINENUMBER, L_QUANTITY, L_EXTENDEDPRICE, L_DISCOUNT, L_TAX, L_RETURNFLAG, L_LINESTATUS, L_SHIPDATE) from '/home/user31/qmd/joinedItem/Q1' with DELIMITER = '|';")

##create funtions
#session.execute("CREATE OR REPLACE FUNCTION computeDiscPrice(l_extendedprice double, l_discount double) called on null input returns double language java as 'return (Double.valueOf ( l_extendedprice.doubleValue() *  (1.0 - l_discount.doubleValue() ) ));';")
#session.execute("CREATE OR REPLACE FUNCTION computeChargePrice (l_extendedprice double,l_discount double,l_tax double) CALLED ON NULL INPUT RETURNS double LANGUAGE java AS 'return (Double.valueOf( l_extendedprice.doubleValue() *  (1.0 - l_discount.doubleValue() ) * (1.0 + l_tax.doubleValue()) ));';")

##select
#rows = session.execute("SELECT l_returnflag, l_linestatus,  sum(l_quantity) as sum_qty, sum(l_extendedprice) as sum_base_price, sum(computeDiscPrice(l_extendedprice, l_discount)) as sum_disc_price, sum(computeChargePrice(l_extendedprice, l_discount, l_tax)) as sum_charge,  avg(l_quantity) as avg_qty, avg(l_extendedprice) as avg_price,  avg(l_discount) as avg_disc,  count(*) as count_order FROM  TPCH_Q1 WHERE  shipdate < '2000-01-01 22:00:00-0700'   and returnflag='N'  and linestatus = 'O' ;")

##show
#for row in rows:
#	print(row)
