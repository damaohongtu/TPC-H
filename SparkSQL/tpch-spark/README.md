# tpch-spark

TPC-H queries implemented in Spark using the DataFrames API.
Tested under Spark 2.3.0

z3ero

liangzhizhou@iie.ac.cn

### Running

First compile using:

```
sbt package
```
find spark-tpc-h-queries_2.11-2.0.jar in the dir=>target/scala-2.11

You can then run a query using:

```
spark-submit --class "main.scala.TpchQuery" --master spark://host4:7077 target/scala-2.11/spark-tpc-h-queries_2.11-1.0.jar <num> <input_data_dir> <output_result_dir>
```

1. where <num> is the number of the query to run e.g 1, 2, ..., 22
and MASTER specifies the spark-mode e.g local, yarn, standalone etc...

2. when <num> = 0, all queries (22 queries) will be excute

3. input_data_dir could be local dir, eg: file:///home/data, and could be hdfs dir, eg: hdfs://ip:9000/data

4. the result of excuting query will be saved in output_result_dir, and the time of excuting every query will also be save in output_result_dir's TIMES.txt


### reference
	https://github.com/ssavvides/tpch-spark	
	My program is based on the above program, slightly modified

