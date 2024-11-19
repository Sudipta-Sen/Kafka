# Kafka Basics

Kafka was originally developed by LinkedIn in 2011. It is an open-source distributed event streaming platform for handling real-time data feeds.

## Kafka Components
1. `Kafka Broker:` The central server system where Kafka processes run.
2. `Kafka Client:` Includes libraries like Producer and Consumer APIs.
3. `Kafka Connect:` Helps with data integration by connecting external systems with Kafka.
4. `Kafka Streams:` A library for building real-time stream processing applications.
5. `KSQL:` Provides a SQL-like interface for Kafka streams, making it act like a database.

## Core Kafka Concepts

1. `Producer:` An application that sends data (called messages or records) to Kafka, for kafka it is simple array of bits
2. `Consumer:` Receives data from Kafka and reads the messages from a Producer provided they have permission to read
3. `Broker:` The Kafka server. Producers and consumers uses kafka as a broker to exchange messages.
4. `Cluster:` A group of Kafka brokers (servers) running together.
5. `Topic:` A stream of records (like a table in a database), with a unique name.
6. `Partitions:` Subdivisions of a topic, allowing parallelism in reading and writing.
7. `Offset:` A unique ID for each message within a partition.
8. `Consumer Group:` A group of consumers that share the work of consuming messages from a topic.

To locate a specific message in Kafka, we need:

- Topic name
- Partition
- Offset

### Partitions and Scalability
Kafka partitions help with scaling by allowing multiple consumers to read data in parallel. However, only one consumer within a group can read from a single partition to prevent duplicates.

## Kafka Connect
Kafka Connect simplifies integration between external systems and Kafka. It can be used to:

1. `Source Connector:` Reads data from an external system and sends it to Kafka (acts as a producer).
2. `Sink Connector:` Reads data from Kafka and sends it to an external system (acts as a consumer).


## Kafka Connect Framework
----------------------
**Source Connectors:** Use `SourceConnector` and `SourceTask` classes to interact with external systems to read data and write to kafka.

**Sink Connectors:** Use `SinkConnector` and `SinkTask` classes to write data to external systems.


Kafka connect is itself is a cluster. Each individual unit in the connect cluster is called a connect worker. We can have one kafka connect cluster which acts as both source and sink connector.

Kafka connect can perform basic SMT's (Single Message Transformation), for example:
- Add a new field in your record using static data or metadata
- Filter or rename fields
- Mask some field with null value
- Change the record
- Route the record to a different kafka Topic

## Kafka connect architecture

Key components in Kafka Connect architecture:
Three things in the architecture:
1. Worker: The unit that runs tasks and connectors.
2. Connector: Manages connection to external systems.
3. Task: Handles parallel data processing for the connectors.

Each kafka connect cluster has a unique group id, if we want to add a worker in a cluster we need to start the worker with the respective group id.

These clusters are fault tolerant and self managed.

The SourceTask is responsible solely for interacting with the source database; it does not directly send data to the Kafka cluster. Instead, it is the worker nodes that handle the task of transmitting data to the Kafka broker.

There are two key variations across different input systems:

1. **Input Splitting for Parallel Processing:** Managed by the Task class, which determines how to partition input data for efficient parallelism.

2. **Interaction with External Systems:** Handled by the Connector class, which defines how the system interfaces with the external source.

## Kafka Streams

Kafka Streams is used for **real-time stream processing**. It processes an unbounded stream of data (continuous data with no fixed size) in small packets.

Data streams are unbounded, infinite sequences of data packets, typically measured in kilobytes (KB). The term "unbounded" refers to the absence of a defined start or end point. These streams are often continuous or ever-growing, with data transmitted in small, sequential packets.

Kafka Streams works by:
- Creating logical tasks based on the number of topic partitions.
- Rebalancing tasks if a machine fails, ensuring processing continues.

Kafka Streams is a library that allows real-time data processing by streaming input data into a Kafka topic. Internally, Kafka Streams creates logical tasks corresponding to the number of partitions in a topic. The Kafka framework then evenly distributes these partitions, assigning one partition from each topic to a task. Based on the number of available consumer machines, these tasks are allocated accordingly.

Kafka Streams ensures dynamic rebalancing of workloads across application instances, with partition-level granularity. If a task is running on a machine that fails, Kafka Streams seamlessly reassigns and reruns that task on another available instance, ensuring fault tolerance and continuous processing.

## KSQL

KSQL is a SQL interface to Kafka streams that allows users to treat Kafka topics like tables and query them using SQL-like syntax.

It operates in two modes:
1. Interactive Mode: Ideal for development (CLI or Web UI).
2. Headless Mode: Ideal for production (automated, no user interaction).

## KSQL Components

1. **KSQL Engine:** Processes SQL-like commands.
2. **REST Interface:** Receives commands from the user.
3. **KSQL Client:** User interface (CLI or UI).

KSQL allows me to use the kafka topic as a table and fire SQL like queries over those topics

## Kafka Use Cases

1. Data Integration

Kafka simplifies data integration with external systems using Kafka Broker, Kafka Client APIs, and Kafka Connect. Data producers (like IoT devices) send data to Kafka, which can then be consumed by any interested system.  Kafka simplifies data integration with external systems using Kafka Broker, Kafka Client APIs, and Kafka Connect. Data producers (like IoT devices) send data to Kafka, which can then be consumed by any interested system. 

2. Microservices for Stream Processing

Kafka is often used in microservices to create and process real-time data streams. It can manage both data streaming and processing, utilizing Kafka Broker, Streams, and Producer APIs. 

3. Real-Time Data Warehousing

Kafka acts as a real-time data pipeline, storing data in data lakes or warehouses, and KSQL can be used to run SQL-like queries for reporting.

## Usage of kafka
1. `Data Ingestion/integration:` It uses -   
- Kafka broker and internals
- kafka connect and commonly used connetors

2. `Microservice architecture:` It uses -
- Kafka broker and internals
- kafka client apis
- kafka streams

3. `Data Engnieering:` It uses -
- Kafka broker and internals
- Interacting with kafka using spark structured streaming