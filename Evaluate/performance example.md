# 性能监控
## 1.性能监控脚本
```sh
#!/bin/bash

#监控cpu系统负载
IP=`ifconfig eth0 | grep "inet addr" | cut -f 2 -d ":" | cut -f 1 -d " "`
cpu_num=`grep -c 'model name' /proc/cpuinfo`
count_uptime=`uptime |wc -w`
load_15=`uptime | awk '{print $'$count_uptime'}'`
average_load=`echo "scale=2;a=$load_15/$cpu_num;if(length(a)==scale(a)) print 0;print a" | bc`
average_int=`echo $average_load | cut -f 1 -d "."`
load_warn=0.70
if [ $average_int -gt 0 ]
then
echo "$IP服务器单个核心15分钟的平均负载为$average_load，超过警戒值1.0，请立即处理！！！$(date +%Y%m%d/%H:%M:%S)" >>/usr/monitor/performance/performance_$(date +%Y%m%d).log
echo "$IP服务器单个核心15分钟的平均负载为$average_load，超过警戒值1.0，请立即处理！！！$(date +%Y%m%d/%H:%M:%S)" | mail -s "$IP服务器系统负载严重告警" XXXX@qq.com
else
echo "$IP服务器单个核心15分钟的平均负载值为$average_load,负载正常   $(date +%Y%m%d/%H:%M:%S)">>/usr/monitor/performance/performance_$(date +%Y%m%d).log
fi

#监控cpu使用率
cpu_idle=`top -b -n 1 | grep Cpu | awk '{print $5}' | cut -f 1 -d "."`
if [ $cpu_idle -lt 20 ]
then

echo "$IP服务器cpu剩余$cpu_idle%,使用率已经超过80%,请及时处理。">>/usr/monitor/performance/performance_$(date +%Y%m%d).log

echo "$IP服务器cpu剩余$cpu_idle%,使用率已经超过80%,请及时处理！！！" | mail -s "$IP服务器cpu告警" XXXX@qq.com
else

echo
"$IP服务器cpu剩余$cpu_idle%,使用率正常">>/usr/monitor/performance/performance_$(date +%Y%m%d).log
fi
```
## 2.进程监控
```sh
#!/bin/bash
IP=`ifconfig eth0 | grep "inet addr" | cut -f 2 -d ":" | cut -f 1 -d " "`

tomcat_dir="/opt/apache-tomcat-7.0.8"
mysql_dir="/usr/local/mysql/bin/mysqld_safe"
vsftp_dir="/usr/sbin/vsftpd"
ssh_dir="/usr/sbin/sshd"

for dir in $tomcat_dir $mysql_dir $vsftp_dir  $ssh_dir
do
process_count=$(ps -ef | grep "$dir" | grep -v grep | wc -l)

        for service in tomcat mysql vsftp ssh
        do
                echo "$dir" |grep -q "$service"
                if [ $? -eq 0 ]
                then
                        if [ $process_count -eq 0 ]
                        then
                            echo "$service is down at $(date +%Y%m%d%H:%M:%S)" >>/usr/monitor/process/process_$(date +%Y%m%d).log
                            echo "$service is down at $(date +%Y%m%d%H:%M:%S)" | mail -s "$IP服务器 $service服务关闭告警" XXXX@qq.com
                        else
                            echo "$service is running at $(date +%Y%m%d%H:%M:%S)" >>/usr/monitor/process/process_$(date +%Y%m%d).log
                        fi
                else
                        continue
                fi
        done
done
```
## 3.流量监控
```sh
#!/bin/bash
#
R1=`cat /sys/class/net/eth0/statistics/rx_bytes`
T1=`cat /sys/class/net/eth0/statistics/tx_bytes`
sleep 1
R2=`cat /sys/class/net/eth0/statistics/rx_bytes`
T2=`cat /sys/class/net/eth0/statistics/tx_bytes`
TBPS=`expr $T2 - $T1`
RBPS=`expr $R2 - $R1`
TKBPS=`expr $TBPS / 1024`
RKBPS=`expr $RBPS / 1024`
echo "上传速率 eth0: $TKBPS kb/s 下载速率 eth0: $RKBPS kb/s at $(date +%Y%m%d%H:%M:%S)" >>/usr/monitor/network/network_$(date +%Y%m%d).log

```
## 4.流量分析统计
```sh
#!/bin/bash
TX=0;
RX=0;
MAX_TX=0;
MAX_RX=0;
while read line
do
        a=`echo $line | grep "eth0" |awk '{print $3}'`
if [ $a -ge 0 ]
then
        TX=$a
        if [ $TX -ge $MAX_TX ]
        then
                MAX_TX=$TX
        fi
fi
        b=`echo $line | grep "eth0" |awk '{print $7}'`
if [ $b -ge 0 ]
then
        RX=$b
        if [ $RX -ge $MAX_RX ]
        then
                MAX_RX=$RX
        fi
fi
done < /usr/monitor/network/network_$(date +%Y%m%d).log
echo "最高上传速度为 $MAX_TX kb/s at $(date +%Y%m%d)">>/usr/monitor/network/tongji.log
echo "最高下载速度为 $MAX_RX kb/s at $(date +%Y%m%d)">>/usr/monitor/network/tongji.log

```
## 5.内存硬盘登录用户数监控
```sh
#!/bin/bash
#监控系统负载与CPU、内存、硬盘、登录用户数，超出警戒值则发邮件告警。

#提取本服务器的IP地址信息
IP=`ifconfig eth0 | grep "inter addr" | cut -f 2 -d ":" | cut -f 1 -d " "`



# 1、监控系统负载的变化情况，超出时发邮件告警：

#抓取cpu的总核数
cpu_num=`cat /proc/cpuinfo | grep -c "model name"`

#抓取当前系统15分钟的平均负载值
load_15=`uptime | awk '{print $12}'`

#计算当前系统单个核心15分钟的平均负载值，结果小于1.0时前面个位数补0。
average_load=`echo "scale=2;a=$load_15/$cpu_num;if(length(a)==scale(a)) print 0;print a" | bc`

#取上面平均负载值的个位整数
average_int=`echo $average_load | cut -f 1 -d "."`

#设置系统单个核心15分钟的平均负载的告警值为0.70(即使用超过70%的时候告警)。
load_warn=0.70

#当单个核心15分钟的平均负载值大于等于1.0（即个位整数大于0） ，直接发邮件告警；如果小于1.0则进行二次比较
if [ $average_int > 0 ]; then
echo "$IP服务器单个核心15分钟的系统平均负载为$average_load，超过警戒值1.0，请立即处理." | mutt -s "$IP 服务器系统负载严重告警." fuquanjun@9kpoker.com
else

#当前系统15分钟平均负载值与告警值进行比较（当大于告警值0.70时会返回1，小于时会返回0）
load_now=`expr $average_load \> $load_warn`

#如果系统单个核心15分钟的平均负载值大于告警值0.70（返回值为1），则发邮件给管理员
if [ $load_now == 1 ]; then
echo "$IP服务器单个核心15分钟的系统平均负载为$average_load，超过警戒值0.70，请及时处理." | mutt -s "$IP 服务器系统负载告警" fuquanjun@9kpoker.com
fi
fi




# 2、监控系统cpu的情况，当使用超过80%的时候发告警邮件：

#取当前空闲cpu百份比值（只取整数部分）
cpu_idle=`top -b -n 1 | grep Cpu | awk '{print $5}' | cut -f 1 -d "."`

#设置空闲cpu的告警值为20%，如果当前cpu使用超过80%（即剩余小于20%），立即发邮件告警
if (($cpu_idle < 20)); then
echo "$IP服务器cpu剩余$cpu_idle%，使用率已经超过80%，请及时处理。" | mutt -s "$IP服务器CPU告警" fuquanjun@9kpoker.com
fi





# 3、监控系统交换分区swap的情况，当使用超过80%的时候发告警邮件：

#系统分配的交换分区总量
swap_total=`free -m | grep Swap | awk '{print $2}'`

#当前剩余的交换分区free大小
swap_free=`free -m | grep Swap | awk '{print $4}'`

#当前已使用的交换分区used大小
swap_used=`free -m | grep Swap | awk '{print $3}'`

if (($swap_used != 0)); then
#如果交换分区已被使用，则计算当前剩余交换分区free所占总量的百分比，用小数来表示，要在小数点前面补一个整数位0
swap_per=0`echo "scale=2;$swap_free/$swap_total" | bc`

#设置交换分区的告警值为20%(即使用超过80%的时候告警)。
swap_warn=0.20

#当前剩余交换分区百分比与告警值进行比较（当大于告警值(即剩余20%以上)时会返回1，小于(即剩余不足20%)时会返回0 ）
swap_now=`expr $swap_per \> $swap_warn`

#如果当前交换分区使用超过80%（即剩余小于20%，上面的返回值等于0），立即发邮件告警
if (($swap_now == 0)); then
echo "$IP服务器swap交换分区只剩下 $swap_free M 未使用，剩余不足20%，使用率已经超过80%，请及时处理。" | mutt -s "$IP 服务器内存告警" | fuquanjun@9kpoker.com
fi
fi




# 4、监控系统硬盘根分区使用的情况，当使用超过80%的时候发告警邮件：

#取当前根分区（/dev/sda3）已用的百份比值（只取整数部分）
disk_sda3=`df -h | grep /dev/sda3 | awk '{print $5}' | cut -f 1 -d "%"`

#设置空闲硬盘容量的告警值为80%，如果当前硬盘使用超过80%，立即发邮件告警
if (($disk_sda3 > 80)); then
echo "$IP 服务器 /根分区 使用率已经超过80%，请及时处理." | mutt -s "$IP 服务器硬盘告警" fuqunajun@9kpoker.com
fi





#5、监控系统用户登录的情况，当用户数超过3个的时候发告警邮件：

#取当前用户登录数（只取数值部分）
users=`uptime | awk '{print $6}'`

#设置登录用户数的告警值为3个，如果当前用户数超过3个，立即发邮件告警
if (($users >= 3)); then
echo "$IP 服务器用户数已经达到$users个，请及时处理。" | mutt -s "$IP 服务器用户数告警" fuquanjun@9kpoker.com
fi
```
## 6.系统初始化脚本
```sh
#!/bin/bash

os_check() {
        if [ -e /etc/redhat-release ]; then
                REDHAT=`cat /etc/redhat-release |cut -d' '  -f1`
        else
                DEBIAN=`cat /etc/issue |cut -d' ' -f1`
        fi

        if [ "$REDHAT" == "CentOS" -o "$REDHAT" == "Red" ]; then
                P_M=yum
        elif [ "$DEBIAN" == "Ubuntu" -o "$DEBIAN" == "ubutnu" ]; then
                P_M=apt-get
        else
                Operating system does not support.
                exit 1
        fi
}

if [ $LOGNAME != root ]; then
    echo "Please use the root account operation."
    exit 1
fi

if ! which vmstat &>/dev/null; then
        echo "vmstat command not found, now the install."
        sleep 1
        os_check
        $P_M install procps -y
        echo "-----------------------------------------------------------------------"
fi

if ! which iostat &>/dev/null; then
        echo "iostat command not found, now the install."
        sleep 1
        os_check
        $P_M install sysstat -y
        echo "-----------------------------------------------------------------------"
fi



while true; do
    select input in cpu_load disk_load disk_use disk_inode mem_use tcp_status cpu_top10 mem_top10 traffic quit; do
        case $input in
            cpu_load)
                #CPU利用率与负载
                echo "---------------------------------------"
                i=1
                while [[ $i -le 3 ]]; do
                    echo -e "\033[32m  参考值${i}\033[0m"
                    UTIL=`vmstat |awk '{if(NR==3)print 100-$15"%"}'`
                    USER=`vmstat |awk '{if(NR==3)print $13"%"}'`
                    SYS=`vmstat |awk '{if(NR==3)print $14"%"}'`
                    IOWAIT=`vmstat |awk '{if(NR==3)print $16"%"}'`
                    echo "Util: $UTIL"
                    echo "User use: $USER"
                    echo "System use: $SYS"
                    echo "I/O wait: $IOWAIT"
                    i=$(($i+1))
                    sleep 1
                done
                echo "---------------------------------------"
                break
                ;;

            disk_load)
                #硬盘I/O负载
                echo "---------------------------------------"
                i=1
                while [[ $i -le 3 ]]; do
                    echo -e "\033[32m  参考值${i}\033[0m"
                    UTIL=`iostat -x -k |awk '/^[v|s]/{OFS=": ";print $1,$NF"%"}'`
                    READ=`iostat -x -k |awk '/^[v|s]/{OFS=": ";print $1,$6"KB"}'`
                    WRITE=`iostat -x -k |awk '/^[v|s]/{OFS=": ";print $1,$7"KB"}'`
                    IOWAIT=`vmstat |awk '{if(NR==3)print $16"%"}'`
                    echo -e "Util:"
                    echo -e "${UTIL}"
                    echo -e "I/O Wait: $IOWAIT"
                    echo -e "Read/s:\n$READ"
                    echo -e "Write/s:\n$WRITE"
                    i=$(($i+1))
                    sleep 1
                done
                echo "---------------------------------------"
                break
                ;;

            disk_use)
                #硬盘利用率
                DISK_LOG=/tmp/disk_use.tmp
                DISK_TOTAL=`fdisk -l |awk '/^Disk.*bytes/&&/\/dev/{printf $2" ";printf "%d",$3;print "GB"}'`
                USE_RATE=`df -h |awk '/^\/dev/{print int($5)}'`
                for i in $USE_RATE; do
                    if [ $i -gt 90 ];then
                        PART=`df -h |awk '{if(int($5)=='''$i''') print $6}'`
                        echo "$PART = ${i}%" >> $DISK_LOG
                    fi
                done
                echo "---------------------------------------"
                echo -e "Disk total:\n${DISK_TOTAL}"
                if [ -f $DISK_LOG ]; then
                    echo "---------------------------------------"
                    cat $DISK_LOG
                    echo "---------------------------------------"
                    rm -f $DISK_LOG
                else
                    echo "---------------------------------------"
                    echo "Disk use rate no than 90% of the partition."
                    echo "---------------------------------------"
                fi
                break
                ;;

            disk_inode)
                #硬盘inode利用率
                INODE_LOG=/tmp/inode_use.tmp
                INODE_USE=`df -i |awk '/^\/dev/{print int($5)}'`
                for i in $INODE_USE; do
                    if [ $i -gt 90 ]; then
                        PART=`df -h |awk '{if(int($5)=='''$i''') print $6}'`
                        echo "$PART = ${i}%" >> $INODE_LOG
                    fi
                done
                if [ -f $INODE_LOG ]; then
                    echo "---------------------------------------"
                    rm -f $INODE_LOG
                else
                    echo "---------------------------------------"
                    echo "Inode use rate no than 90% of the partition."
                    echo "---------------------------------------"
                fi
                break
                ;;

            mem_use)
                #内存利用率
                echo "---------------------------------------"
                MEM_TOTAL=`free -m |awk '{if(NR==2)printf "%.1f",$2/1024}END{print "G"}'`
                USE=`free -m |awk '{if(NR==3) printf "%.1f",$3/1024}END{print "G"}'`
                FREE=`free -m |awk '{if(NR==3) printf "%.1f",$4/1024}END{print "G"}'`
                CACHE=`free -m |awk '{if(NR==2) printf "%.1f",($6+$7)/1024}END{print "G"}'`
                echo -e "Total: $MEM_TOTAL"
                echo -e "Use: $USE"
                echo -e "Free: $FREE"
                echo -e "Cache: $CACHE"
                echo "---------------------------------------"
                break
                ;;

            tcp_status)
                #网络连接状态
                echo "---------------------------------------"
                COUNT=`netstat -antp |awk '{status[$6]++}END{for(i in status) print i,status[i]}'`
                echo -e "TCP connection status:\n$COUNT"
                echo "---------------------------------------"
                ;;

            cpu_top10)
                #占用CPU高的前10个进程
                echo "---------------------------------------"
                CPU_LOG=/tmp/cpu_top.tmp
                i=1
                while [[ $i -le 3 ]]; do
                    #ps aux |awk '{if($3>0.1)print "CPU: "$3"% -->",$11,$12,$13,$14,$15,$16,"(PID:"$2")" |"sort -k2 -nr |head -n 10"}' > $CPU_LOG
                    ps aux |awk '{if($3>0.1){{printf "PID: "$2" CPU: "$3"% --> "}for(i=11;i<=NF;i++)if(i==NF)printf $i"\n";else printf $i}}' |sort -k4 -nr |head -10 > $CPU_LOG
                    #循环从11列（进程名）开始打印，如果i等于最后一行，就打印i的列并换行，否则就打印i的列
                    if [[ -n `cat $CPU_LOG` ]]; then
                       echo -e "\033[32m  参考值${i}\033[0m"
                       cat $CPU_LOG
                       > $CPU_LOG
                    else
                        echo "No process using the CPU."
                        break
                    fi
                    i=$(($i+1))
                    sleep 1
                done
                echo "---------------------------------------"
                break
                ;;

            mem_top10)
                #占用内存高的前10个进程
                echo "---------------------------------------"
                MEM_LOG=/tmp/mem_top.tmp
                i=1
                while [[ $i -le 3 ]]; do
                    #ps aux |awk '{if($4>0.1)print "Memory: "$4"% -->",$11,$12,$13,$14,$15,$16,"(PID:"$2")" |"sort -k2 -nr |head -n 10"}' > $MEM_LOG
                    ps aux |awk '{if($4>0.1){{printf "PID: "$2" Memory: "$3"% --> "}for(i=11;i<=NF;i++)if(i==NF)printf $i"\n";else printf $i}}' |sort -k4 -nr |head -10 > $MEM_LOG
                    if [[ -n `cat $MEM_LOG` ]]; then
                        echo -e "\033[32m  参考值${i}\033[0m"
                        cat $MEM_LOG
                        > $MEM_LOG
                    else
                        echo "No process using the Memory."
                        break
                    fi
                    i=$(($i+1))
                    sleep 1
                done
                echo "---------------------------------------"
                break
                ;;

            traffic)
                #查看网络流量
                while true; do
                    read -p "Please enter the network card name(eth[0-9] or em[0-9]): " eth
                    #if [[ $eth =~ ^eth[0-9]$ ]] || [[ $eth =~ ^em[0-9]$ ]] && [[ `ifconfig |grep -c "\<$eth\>"` -eq 1 ]]; then
                    if [ `ifconfig |grep -c "\<$eth\>"` -eq 1 ]; then
                        break
                    else
                        echo "Input format error or Don't have the card name, please input again."
                    fi
                done
                echo "---------------------------------------"
                echo -e " In ------ Out"
                i=1
                while [[ $i -le 3 ]]; do
                    #OLD_IN=`ifconfig $eth |awk '/RX bytes/{print $2}' |cut -d: -f2`
                    #OLD_OUT=`ifconfig $eth |awk '/RX bytes/{print $6}' |cut -d: -f2`
                    OLD_IN=`ifconfig $eth |awk -F'[: ]+' '/bytes/{if(NR==8)print $4;else if(NR==5)print $6}'`
                    #CentOS6和CentOS7 ifconfig输出进出流量信息位置不同，CentOS6中RX与TX行号等于8，CentOS7中RX行号是5，TX行号是5，所以就做了个判断.

                    OLD_OUT=`ifconfig $eth |awk -F'[: ]+' '/bytes/{if(NR==8)print $9;else if(NR==7)print $6}'`
                    sleep 1
                    NEW_IN=`ifconfig $eth |awk -F'[: ]+' '/bytes/{if(NR==8)print $4;else if(NR==5)print $6}'`
                    NEW_OUT=`ifconfig $eth |awk -F'[: ]+' '/bytes/{if(NR==8)print $9;else if(NR==7)print $6}'`
                    IN=`awk 'BEGIN{printf "%.1f\n",'$((${NEW_IN}-${OLD_IN}))'/1024/128}'`
                    OUT=`awk 'BEGIN{printf "%.1f\n",'$((${NEW_OUT}-${OLD_OUT}))'/1024/128}'`
                    echo "${IN}MB/s ${OUT}MB/s"
                    i=$(($i+1))
                    sleep 1
                done
                echo "---------------------------------------"
                break
                ;;
                        quit)
                                exit 0
                                ;;
               *)
                    echo "---------------------------------------"
                    echo "Please enter the number."
                    echo "---------------------------------------"
                    break
                    ;;
        esac
    done
done
```
