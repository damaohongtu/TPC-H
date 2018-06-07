# TPC-H EVALUATE
## 1.条件控制
- 数据量大小1G,2G,5G,10G
- 集群节点数目
- Q1-Q22中部分查询的条件
- Memory bandwidth
- 各个系统的参数配置

## 2.对比指标
- 加载数据时间，计算资源消耗，磁盘占有率等
- query时间，CPU cost，I/O cost等

## 3.实验
- 资源使用情况脚本编写
- 同样配置下，load数据
- 同样配置下，执行Q1-Q22
- 按照类型将Q1-Q22进行分类，比较在大类query下各自的表现，比如(scan-based queries和long-running queries)
