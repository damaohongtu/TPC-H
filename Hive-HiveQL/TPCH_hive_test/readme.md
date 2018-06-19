1G-tpch_benchmark.sh、3G-tpch_benchmark.sh、5G-tpch_benchmark.sh脚本是Q1-Q22的连续查询脚本，顺序执行22个查询语句，循环测试3次，3个脚本分别对应测试1G、3G、5G数据量。每个查询语句使用hive-f命令读取tpchQL-1G文件夹中对应的.hive查询语句文件。（3G、5G的查询语句修改tpchQL-1G文件夹中22个.hive文件使用的数据库名称即可。），查询执行的信息将记录到日志benchmark.log中，可以通过日志中查看执行时间。

hive_check.sh是用ps命令查看进程信息。

