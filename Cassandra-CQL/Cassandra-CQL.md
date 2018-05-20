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
bin/cassandra -f
# 创建空间
CREATE KEYSPACE tutorialspoint WITH replication = {'class':'SimpleStrategy', 'replication_factor' : 3};
# 建表
cqlsh> USE tutorialspoint;
cqlsh:tutorialspoint>; CREATE TABLE emp(
   emp_id int PRIMARY KEY,
   emp_name text,
   emp_city text,
   emp_sal varint,
   emp_phone varint
   );
# 查询
cqlsh:tutorialspoint> select * from emp;
```
