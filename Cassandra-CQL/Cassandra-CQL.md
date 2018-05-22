# Cassandra-CQL
```
# 下载
wget http://www-eu.apache.org/dist/cassandra/3.11.2/apache-cassandra-3.11.2-bin.tar.gz
tar -zxvf apache-cassandra-3.11.2-bin.tar.gz
# 修改环境变量
# vim /etc/profile
export CASSANDRA_HOME=/home/mao/Apache/apache-cassandra-3.11.2
```
# 初级教程（<a href="https://www.w3cschool.cn/cassandra/">W3C教程</a>）
```
# 启动
$CASsANDRA_HOME/bin/cassandra -f
# 创建空间
# 新的控制台
$ cqlsh
cqlsh> CREATE KEYSPACE tpch WITH replication = {'class':'SimpleStrategy', 'replication_factor' : 3};
# 建表
cqlsh> USE tpch;

# 查询
cqlsh:tutorialspoint> select * from emp;
```


## 建表并加载数据
```
CREATE TABLE NATION  ( N_NATIONKEY     int PRIMARY KEY,
                          N_NAME       text,
                          N_REGIONKEY  int,
                          N_COMMENT    text );

case class NATION(N_NATIONKEY: Integer, 
                       N_NAME: String, 
                       N_REGIONKEY: Integer,
                       N_COMMENT: String);
normalfill.map(line => (line(0), line(1), line(2),line(3))).saveToCassandra("tpch", "NATION", Seq("N_NATIONKEY", "N_NAME", "N_REGIONKEY","N_COMMENT"))



CREATE TABLE REGION  ( R_REGIONKEY     int PRIMARY KEY,
                          R_NAME       text,
                          R_COMMENT    text );

CREATE TABLE PART  ( P_PARTKEY          int PRIMARY KEY,
                          P_NAME        text,
                          P_MFGR        text,
                          P_BRAND       text,
                          P_TYPE        text,
                          P_SIZE        int,
                          P_CONTAINER   text,
                          P_RETAILPRICE decimal,
                          P_COMMENT     text );

CREATE TABLE SUPPLIER ( S_SUPPKEY       int PRIMARY KEY,
                          S_NAME        text,
                          S_ADDRESS     text,
                          S_NATIONKEY   int,
                          S_PHONE       text,
                          S_ACCTBAL     decimal,
                          S_COMMENT     text );

CREATE TABLE PARTSUPP ( PS_PARTKEY       int PRIMARY KEY,
                          PS_SUPPKEY     int,
                          PS_AVAILQTY    int,
                          PS_SUPPLYCOST  decimal,
                          PS_COMMENT     text );

CREATE TABLE CUSTOMER ( C_CUSTKEY       int PRIMARY KEY,
                          C_NAME        text,
                          C_ADDRESS     text,
                          C_NATIONKEY   int,
                          C_PHONE       text,
                          C_ACCTBAL     decimal,
                          C_MKTSEGMENT  text,
                          C_COMMENT     text );

CREATE TABLE ORDERS  ( O_ORDERKEY       int PRIMARY KEY,
                          O_CUSTKEY        int,
                          O_ORDERSTATUS    text,
                          O_TOTALPRICE     decimal,
                          O_ORDERDATE      date,
                          O_ORDERPRIORITY  text,  
                          O_CLERK          text, 
                          O_SHIPPRIORITY   int,
                          O_COMMENT        text );

CREATE TABLE LINEITEM ( L_ORDERKEY        int PRIMARY KEY,
                          L_PARTKEY       int,
                          L_SUPPKEY       int,
                          L_LINENUMBER    int,
                          L_QUANTITY      decimal,
                          L_EXTENDEDPRICE  decimal,
                          L_DISCOUNT      decimal,
                          L_TAX           decimal,
                          L_RETURNFLAG    text,
                          L_LINESTATUS    text,
                          L_SHIPDATE      date,
                          L_COMMITDATE    date,
                          L_RECEIPTDATE   date,
                          L_SHIPINSTRUCT  text,
                          L_SHIPMODE      text,
                          L_COMMENT       text );

```

```
cqlsh:tpch> describe tables;
# customer  lineitem  partsupp  region  nation  part  supplier  orders
cqlsh:tpch> SELECT * FROM tpch.customer
```

```
scala>  val normalfill = sc.textFile("hdfs://localhost:9000/tpch/customer/customer.tbl").map(line => line.split("|"));


scala> normalfill.map(line => (line(0), line(1), line(2))).saveToCassandra(
 "int_ks", "int_compound", Seq("pkey", "ckey1", "data1"))
```