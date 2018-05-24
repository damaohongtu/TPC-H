# Hive环境搭建
<p color="red" size=4>注意：hive的元数据需要放在传统的RDBMS中，所以需要安装关系型数据库，这里采用安装mysql，为hadoop用户安装hadoop？且hadoop是否需要分布到不同的机器上？</p>

1. Hive下载
2. 解压
3. 环境变量配置
4. 安装mysql
5. Hive配置
```
#conf/hive-site.xml
<configuration>
	<property>
  		<name>javax.jdo.option.ConnectionURL</name>
    	<value>jdbc:mysql://localhost:3306/sparksql?createDatabaseIfNotExist=true</value>
    </property>
    
	<property>
    	<name>javax.jdo.option.ConnectionDriverName</name>
        <value>com.mysql.jdbc.Driver</value>
   	</property>
   	<!--数据库用户名-->
	<property>
  		<name>javax.jdo.option.ConnectionUserName</name>
    	<value>root</value>
    </property>
    <!--数据库密码-->
	<property>
  		<name>javax.jdo.option.ConnectionPassword</name>
    	<value>root</value>
    </property>
</configuration>
```
6. 拷贝mysql驱动到$HIVE_HOME/lib/
7. 启动hive: $HIVE_HOME/bin/hive
8. 测试
```
# 建表
create table hive_wordcount(context string);
# 加载数据
load data local inpath '/home/hadoop/data/hello.txt' into table hive_wordcount;
# 查询
select word, count(1) from hive_wordcount lateral view explode(split(context,'\t')) wc as word group by word;
lateral view explode(): 
```