## 1.The Hadoop Ecosphere

| Component | Description |
| --------- | ----------- |
| 1.Avro | Framework for transforming data into a compact binary format |
| 2.Flume | Data-flow tool for moving streaming data into Hadoop |
| 3.HBase | A columnar database that uses HDFS for its storage |
| 4.HCatalog | A service that provides a relational view of data you store in HDFS |
| 5.Hive | A distributed data warehouse for HDFS data that provides a SQL-like layer to this data |
| 6.Hue | A user and administrative interface that lets you browse HDFS files, run Pig and Hive queries and schedule workflows through Oozie |
| 6.Kafka | A message-queuing framework that handles large amounts of real-time data traffic |
| 7.Mahout | A library of machine-learning algorithms implemented in MapReduce |
| 8.Oozie | A job-scheduling tool |
| 9.Pig | A framework for analyzing large data sets that let you create data pipelines |
| 10.Sqoop |A data movement tool that moves data between HDFS and relational databases |
| 11.Storm |An object-relational mapping library that supports real-time stream processing |
| 12.Tez | A data-processing framework for batch processing that also provides interactive querying capabilities |
| 13.ZooKeeper | A coordination service used by distributed applications such as Hadoop,HBase, Storm, Hive and Kafka |

## 2.Distributed Data Processing: MapReduce and Spark, Hive and Pig
- `MapReduce` is a distributed processing framework that lets you write Java programs to
process data you store in HDFS.
- `Apache Spark` is a high-performance distributed computing framework that has evolved
into the most active Apache project.
- `Apache Hive` provides a SQL interface that enables you to use HDFS data without having
to write programs using MapReduce.
- `Pig` is a high-level framework for data processing that enables you to use a scripting language called Pig Latin to process data using MapReduce on a Hadoop cluster.

## 3.Data Integration: Apache Sqoop, Apache Flume and Apache Kafka
- `Apache Sqoop` (short for “SQL to Hadoop”) is the most well-known tool employed in Hadoop environments to move data back and forth from relational databases to HDFS.
- `Apache Flume:` Flume is a system for the collection, aggregation and moving of large amounts of streaming data from multiple sources to a data store such as HDFS.Although originally Flume was designed for aggregating log data, you can use it to move large amounts of event data or just about any type of data from any data source.
- `Apache Kafka:` Kafka, which started out at LinkedIn, is explicitly distributed and resembles a publish-subscribe system. Kafka lets you combine offline and online processing of streaming data by enabling parallel loading into the Hadoop system and the partitioning of real-time data consumption over the cluster. Architecturally,it’s a system that’s similar to well-known messaging systems such as ActiveMQ and RabbitMQ.
