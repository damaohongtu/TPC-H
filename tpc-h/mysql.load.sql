use tpch;

LOAD DATA LOCAL INFILE '/home/mao/tpch_workplace/tpc_h_tool/dbgen/customer.tbl' INTO TABLE customer FIELDS TERMINATED BY '|'  LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE '/home/mao/tpch_workplace/tpc_h_tool/dbgen/orders.tbl'   INTO TABLE orders   FIELDS TERMINATED BY '|'  LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE '/home/mao/tpch_workplace/tpc_h_tool/dbgen/lineitem.tbl' INTO TABLE lineitem FIELDS TERMINATED BY '|'  LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE '/home/mao/tpch_workplace/tpc_h_tool/dbgen/nation.tbl'   INTO TABLE nation   FIELDS TERMINATED BY '|'  LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE '/home/mao/tpch_workplace/tpc_h_tool/dbgen/partsupp.tbl' INTO TABLE partsupp FIELDS TERMINATED BY '|'  LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE '/home/mao/tpch_workplace/tpc_h_tool/dbgen/part.tbl'     INTO TABLE part     FIELDS TERMINATED BY '|'  LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE '/home/mao/tpch_workplace/tpc_h_tool/dbgen/region.tbl'   INTO TABLE region   FIELDS TERMINATED BY '|'  LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE '/home/mao/tpch_workplace/tpc_h_tool/dbgen/supplier.tbl' INTO TABLE supplier FIELDS TERMINATED BY '|'  LINES TERMINATED BY '\n';