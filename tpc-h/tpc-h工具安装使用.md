# TPC-H
## 1.<a href="http://www.tpc.org/tpc_documents_current_versions/download_programs/tools-download-request.asp?bm_type=TPC-H&bm_vers=2.17.3&mode=CURRENT-ONLY">下载</a>
## 2.设置Makefile文件的参数并编译项目
设置CC参数为你的c语言编译器，如：gcc
以下三个参数只能在注释所给的选项中选择
1. DATABASE= 你的数据库（没有的话只能选择最相似的数据库），如：ORACLE
2. MACHINE = 你的机器，如：LINUX
3. WORKLOAD = TPCH

## 3.执行 ./dbgen -h查看命令帮助信息
```
To generate the SF=1 (1GB), validation database population, use:
    dbgen -vf -s 1

To generate updates for a SF=1 (1GB), use:
    dbgen -v -U 1 -s 1
```
