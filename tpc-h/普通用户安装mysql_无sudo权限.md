1. 安装cmake(<a href="https://cmake.org/files/v2.8/">下载地址</a>)
```
Unpack, e.g
   tar xvfz cmake-2.8.12.2.tar.gz
Install, e.g.:
   mkdir $HOME/CMAKE
   cd cmake-2.8.12.2
   ./bootstrap --prefix=$HOME/CMAKE
   make
   make install
Add $HOME/CMAKE/bin to your PATH.
```
2. Build MySQL.
- 下载源码
- 编译
```
# Unpack, e.g.
tar xvfz mysql-5.6.17.tar.gz
# Configure and prepare installation location, e.g.:
cd mysql-5.6.17

mkdir $HOME/MySQL
mkdir $HOME/MySQL/data
mkdir $HOME/MySQL/etc
cmake -D MYSQL_DATADIR=$HOME/MySQL/data -D SYSCONFDIR=$HOME/MySQL/etc -D CMAKE_INSTALL_PREFIX=$HOME/MySQL .
# Build:
make
make install
```
![](pictures/mysql_tree.png)

- 修改配置文件etc/my.cnf(关键所在)
```
[client]
port = 33306
default-character-set = utf8
socket= /home/user31/MyMySQL/lib/mysql/mysql.sock

[mysql]
port = 33306
default-character-set = utf8
socket= /home/user31/MyMySQL/lib/mysql/mysql.sock


[mysqld]
user = mysql
pid-file = /home/user31/MyMySQL/run/mysqld/mysqld.pid
socket = /home/user31/MyMySQL/lib/mysql/mysql.sock
port= 33306
# basedir = /home/user31/MyMySQL/basepath
datadir = /home/user31/MyMySQL/lib/mysql
tmdir = /home/user31/MyMySQL/tmp
# lc-messages-dir = /home/user31/MyMySQL/lib/mysql
skip-external-locking
bind-address            = 127.0.0.1

# Disabling symbolic-links is recommended to prevent assorted security risks
symbolic-links=0

[mysqld_safe]
log-error=/home/user31/MyMySQL/log/mysqld.log
pid-file=/home/user31/MyMySQL/run/mysqld/mysqld.pid
```
- 初始化
```
# Prepare base MySQL tables, e.g.:
cd $HOME/MySQL
scripts/mysql_install_db
# Start the server, and set the root password:
bin/mysqld_safe &
bin/mysqladmin -u root password '1234'

# 启动服务
cp support-files/mysql.server $HOME/bin
mysql.server stop
mysql.server start
# 进入客户端
mysql -u root -p
```