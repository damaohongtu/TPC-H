#!/usr/bin/env bash

# set up configurations

BASE_DIR=`pwd`

TIME_CMD="/usr/bin/time -f Time:%e"

NUM_OF_TRIALS=3

LOG_FILE="benchmark.log"

LOG_DIR="$BASE_DIR/logs"

# hadoop
HADOOP_CMD="$HADOOP_HOME/bin/hadoop"

# hive
HIVE_CMD="$HIVE_HOME/bin/hive"

# hive tpch queries
# hive all benchmark queries

HIVE_TPCH_QUERIES_ALL=( \
        "tpch-5G/q1_pricing_summary_report.hive" \
		"tpch-5G/q2_minimum_cost_supplier.hive" \
		"tpch-5G/q3_shipping_priority.hive" \
		"tpch-5G/q4_order_priority.hive" \
                "tpch-5G/q5_local_supplier_volume.hive" \
        	"tpch-5G/q6_forecast_revenue_change.hive" \
       		"tpch-5G/q7_volume_shipping.hive" \
        	"tpch-5G/q8_national_market_share.hive" \
        	"tpch-5G/q9_product_type_profit.hive" \
        	"tpch-5G/q10_returned_item.hive" \
        	"tpch-5G/q11_important_stock.hive" \
        	"tpch-5G/q12_shipping.hive" \
        	"tpch-5G/q13_customer_distribution.hive" \
        	"tpch-5G/q14_promotion_effect.hive" \
        	"tpch-5G/q15_top_supplier.hive" \
        	"tpch-5G/q16_parts_supplier_relationship.hive" \
        	"tpch-5G/q17_small_quantity_order_revenue.hive" \
		"tpch-5G/q18_large_volume_customer.hive" \
        	"tpch-5G/q19_discounted_revenue.hive" \
        	"tpch-5G/q20_potential_part_promotion.hive" \
        	"tpch-5G/q21_suppliers_who_kept_orders_waiting.hive" \
        	"tpch-5G/q22_global_sales_opportunity.hive" \
)


if [ -e "$LOG_FILE" ]; then
	timestamp=`date "+%F-%R" --reference=$LOG_FILE`
	backupFile="$LOG_FILE.$timestamp"
	mv $LOG_FILE $LOG_DIR/$backupFile
fi

echo ""
echo "***********************************************"
echo "*           PC-H benchmark on Hive            *"
echo "***********************************************"
echo "                                               " 
echo "Running Hive from $HIVE_HOME" | tee -a $LOG_FILE
echo "Running Hadoop from $HADOOP_HOME" | tee -a $LOG_FILE
echo "See $LOG_FILE for more details of query errors."
echo ""

trial=0
while [ $trial -lt $NUM_OF_TRIALS ]; do
	trial=`expr $trial + 1`
	echo "Executing Trial #$trial of $NUM_OF_TRIALS trial(s)..."

	for query in ${HIVE_TPCH_QUERIES_ALL[@]}; do
		echo "Running Hive query: $query" | tee -a $LOG_FILE
		$TIME_CMD $HIVE_CMD -f $BASE_DIR/$query 2>&1 | tee -a $LOG_FILE | grep '^Time:'
                returncode=${PIPESTATUS[0]}
		if [ $returncode -ne 0 ]; then
			echo "ABOVE QUERY FAILED:$returncode"
		fi
	done

done # TRIAL
echo "***********************************************"
echo ""
