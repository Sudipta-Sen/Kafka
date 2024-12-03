# Kafka Storage Architectural Concepts

## What is Apache Kafka?

### Basic Definition
Apache Kafka is a messaging broker.

- **Messaging Broker:** Kafka acts as an intermediary between producers (who send messages) and consumers (who receive messages).
    - **Receive Messages:**
        - Kafka brokers receive messages from producers and acknowledge the successful receipt. This ensures that the producer knows the message has been successfully received.
    - **Store Messages:**
        - Messages are stored in a log file. This storage is critical for safeguarding messages from potential loss and ensuring that consumers can consume them later, not necessarily in real-time.
    - **Deliver Messages:**
        - Kafka delivers messages to consumers upon request. This allows consumers to retrieve messages at their convenience.

### Advanced Definition
Apache Kafka is a horizontally scalable, fault-tolerant, distributed streaming platform designed for building real-time streaming data architectures.

- **Horizontally Scalable:** Kafka can handle increasing loads by adding more nodes to the cluster, allowing for seamless scaling.
- **Fault-Tolerant:** Kafka is designed to handle failures without data loss, ensuring reliability.
- **Distributed Streaming Platform:** Kafka can handle large-scale data streams distributed across multiple servers.

## Kafka Architecture Overview
We can break down its architecture into three parts:
1. Kafka Message Storage Architecture
2. Kafka Cluster Architecture
3. Work Distribution in Kafka Cluster

## Kafka Message Storage Architecture

- **Kafka Topics:**
    -  A Kafka topic is a logical name used to group messages, similar to how a database table groups data records.
    - Records are stored and published using a kafka topic. Topics are partitioned and replicated across multiple brokers. 

- **Partitions:**
    - Mechanism to divide a topic into smaller, more manageable parts.
    - Partitions allow Kafka to scale horizontally. Each partition is an ordered, immutable sequence of records that is continually appended to. Partitions are distributed across multiple brokers.
    - **Physical Representation:** Each partition is a separate directory.

    - Example
        - `Invoice` Topic: Created with 5 partitions.
        - Result: Kafka creates 5 directories for the `invoices` topic, one for each partition.

- **Replication Factor:**
    - The replication factor determines how many copies of the log we want to maintain the Kafka cluster. This ensures data redundancy and fault tolerance.

    - Example
        -  If you create a Topic called `invoices` with 5 partitions and a replication factor of 2, Kafka will create 10 directories i.e each partition has a total 2 copies each so that if 1 got destroied we can retrive the data from another copy.

- **Log Files and Segments**
    -  Messages are stored in the directories as log files.
    - **Splitting Log Files:** Instead of one large log file, Kafka splits these into smaller segments to manage them better.
        - Default Segment Size: 1 GB or 1 week of data, whichever is smaller.
        - Custom Configuration: You can configure smaller sizes (e.g., 1 MB).

- **Offsets:**
    - Each message within a partition has a unique identifier called an offset. These are `32-bit` integers.
        - First message has offset 0000.
        - Second message has offset 0001 and so on.
    - **Segment File Naming:** The name of the segment file includes the first offset in that segment.

-  **Locating Messages:** 
    - To find a specific message, we need to know three things:
        - Topic name
        - Partition number
        - Offset number

- **Indexing**

    - **Offset Index:** Kafka maintains an index of offsets to quickly find messages.
        - **Purpose:** Helps brokers quickly locate a message based on its offset.
    - **Time Index:** Kafka also keeps a time index to fetch messages based on timestamps.
        - **Use Case:** Useful for reading all events created after a specific time.

## Work Distribution in Kafka Cluster

- **Leaders:**

    - Each partition has a leader broker responsible for all reads and writes for that partition. The leader ensures data consistency and handles replication.

    - These are the main partitions created initially. For 5 partitions, Kafka will create 5 leader directories.

- **Followers:**
    - Follower brokers replicate the leader's data and take over if the leader fails, ensuring high availability.  If the replication factor is 3, Kafka will create 2 follower directories for each leader.

- **In Sync Replicas (ISRs):**
    - ISRs are replicas that are fully caught up with the leader's data. They ensure the durability of data.

- **Committed and Uncommitted Messages:**
    - Committed messages are those that have been successfully written to the leader and replicated to the ISRs. Uncommitted messages are not yet replicated and are at risk of loss if the leader fails.