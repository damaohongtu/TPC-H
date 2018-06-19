while :
do
 ps uax|grep hive|grep -v grep |  awk '{print $1,$2,$3,$4,$5,$6,$7}' >> ~/hive-all.log;
 sleep 1;
done
