COPY customer FROM '/home/mao/tpch_workplace/tpch_greenplum/customer.tbl'  DELIMITER '|';
COPY lineitem FROM '/home/mao/tpch_workplace/tpch_greenplum/lineitem1.tbl' DELIMITER '|';
COPY nation   FROM '/home/mao/tpch_workplace/tpch_greenplum/nation1.tbl'   DELIMITER '|';
COPY orders   FROM '/home/mao/tpch_workplace/tpch_greenplum/orders1.tbl'   DELIMITER '|';
COPY part     FROM '/home/mao/tpch_workplace/tpch_greenplum/part1.tbl'     DELIMITER '|';
COPY partsupp FROM '/home/mao/tpch_workplace/tpch_greenplum/partsupp1.tbl' DELIMITER '|';
COPY region   FROM '/home/mao/tpch_workplace/tpch_greenplum/region1.tbl'   DELIMITER '|';
COPY supplier FROM '/home/mao/tpch_workplace/tpch_greenplum/supplier1.tbl' DELIMITER '|';