#!/bin/bash

write_to_file()
{
    file="loaddata.sql"

    if [ ! -f "$file" ] ; then
        touch "$file"
    fi

    echo 'USE tpch;' >> $file
    echo 'SET FOREIGN_KEY_CHECKS=0;' >> $file
    
    DIR=`pwd`
    for tbl in `ls *.tbl`; do
        table=$(echo "${tbl%.*}")
        echo "LOAD DATA LOCAL INFILE '$DIR/$tbl' INTO TABLE $table" >> $file
        echo "FIELDS TERMINATED BY '|' LINES TERMINATED BY '|\n';" >> $file
    done
    echo 'SET FOREIGN_KEY_CHECKS=1;' >> $file
 }

write_to_file

# mysql --local-infile -u root -p < loaddata.sql