# 大数据系统上的TPC-H
## 1.<a href="http://www.tpc.org/tpc_documents_current_versions/current_specifications.asp">什么是TPC-H？</a>
**TPC- H 主要目的是评价特定查询的决策支持能力，强调服务器在数据挖掘、分析处理方面的能力。** `TPC- H 测试围绕22 个SELECT 语句展开，每个SELECT严格定义，遵守SQL- 92语法，并且不允许用户修改。`标准中从4 个方面定义每个SELECT 语句，即商业问题、SELECT 的语法、参数和查询确认。这些SELECT 语句的复杂程度超过大多数实际的OLTP 应用，一个SELECT 执行时间少则几十秒，多则达15 小时以上，22 个查询语句执行一遍需数个小时。（附：<a href="https://wenku.baidu.com/view/024e682cbd64783e09122bf4.html">TPC-H中文版</a>）

## 2.步骤
### （0）搭建环境，安装四种软件：Spark,Hive,Cassandra,GreenPlum
### （1）产生数据（有工具dbgen,可在Linux下编译）
### （2）建表，将数据导入
### （3）执行查询(Q1-Q22,有现成的案例，如在<a href="https://github.com/ssavvides/tpch-pig/tree/master/queries">pig</a>上的，spark上的<a href="https://github.com/ssavvides/tpch-spark/tree/master/src/main/scala">scala代码</a>)，这里可以使用脚本，将日志保存起来，然后从日志文件中提取信息。（<a href="https://github.com/tvondra/pg_tpch/blob/master/tpch.sh">参考</a>）
### （4）性能评估(参考<a href="https://yq.aliyun.com/articles/8952">云栖社区</a>)
**度量标准：**测试中测量的基础数据都与<u>**执行时间**</u>有关，这些时间又可分为：装载数据的每一步操作时间、每个查询执行时间和每个更新操作执行时间，由这些时间可计算出:<font size='4' color='#660066'>数据装载时间、Power@Size、Throughput@Size、QphH@Size 和$/QphH@Size</font>
（附：TCP官方给出的报告<a href="http://www.tpc.org/downloaded_result_files/tpch_results.xls">Current TPC-H Results Spreadsheet</a>）
## 3.测试细节
### （1）数据装载测试
建立测试数据库的过程被称为装载数据，装载测试是为测试DBMS 装载数据的能力。装载测试是第一项测试，测试装载数据的时间，这项操作非常耗时。
### （2）Power 测试
Power 测试是在数据装载测试完成后，数据库处于初始状态，未进行其它任何操作，特别是缓冲区还没有被测试数据库的数据，被称为raw查询。Power 测试要求22 个查询顺序执行1 遍，同时执行一对RF1 和RF2 操作。
### （3）Throughput 测试
Throughput 测试，也是最核心和最复杂的测试，它更接近于实际应用环境，与Power 测试比对SUT 系统的压力有非常大的增加，有多个查询语句组，同时有一对RF1 和RF2 更新流。
## 4.例子(四个方向都有涉及，供参考)
- <a href="https://github.com/ssavvides/tpch-spark">tpch-spark(github项目)</a>
- <a href="https://issues.apache.org/jira/browse/HIVE-600">Running TPC-H queries on Hive(Apache)</a>
- <a href="https://issues.apache.org/jira/browse/PIG-2397">Running TPC-H Benchmark on Pig</a>
- <a href="https://wenku.baidu.com/view/5fb10e9ca417866fb94a8e83.html">TPC-H测试精简</a>
- <a href="http://alronz.github.io/Factors-Influencing-NoSQL-Adoption/site/Cassandra/Examples/TPC-H%20Queries/">Cassandra TPC-H Queries </a>
- <a href="https://github.com/alronz/B2C-Database-Selection-Implementations">CassandraTPCHQueries(github代码，目测比较粗略)</a>
- <a href="https://insideanalysis.com/2010/09/tpc-h-fun-with-greenplum-single-node-edition/">TPC-H fun with Greenplum (single node edition)</a>

## 参考文献
- <a href="https://blog.csdn.net/leixingbang1989/article/details/8766047">TPC-H使用(帖子)</a>
- <a href="https://github.com/greenplum-db/tpch">TPC-H详细介绍，包含参数解析，而且是greenplum的仓库，不知道对greenplum有没有参考，还是针对greenplum的tpc-h？</a>
- <a href="https://wenku.baidu.com/view/46a99819a76e58fafab0035d.html">TPC-H自动测试工具TPCHDriver的研究(国内文章)</a>
- <a href="https://blog.csdn.net/mbshqqb/article/details/78564153?locationNum=1&fps=1">TPC-H工具的使用(Linux下)</a>
- <a href="https://www.slideshare.net/Hadoop_Summit/evaluation-of-tpch-on-spark-and-spark-sql-in-aloja">evaluation-of-tpch-on-spark-and-spark-sql-in-aloja(后面我们的报告可以参考，我们的实验应该加以借鉴)</a>
