# Kafka Cluster Architecture

## Overview

In a development environment, Kafka starts with a single broker, but in production, a cluster of 3 or more brokers is preferred. As the workload grows, Kafka clusters can scale to hundreds of brokers. This scalability brings questions about how Kafka manages its cluster members and administrative tasks without a master node.

## Key Concepts:

1. Masterless Architecture:
    - Kafka does not follow the traditional master-slave architecture. Instead, it uses Zookeeper to manage cluster membership, handle broker failures, and coordinate the cluster's operational tasks.

2. Cluster Membership:
    - Kafka brokers are assigned unique broker IDs configured in their setup files.
    - Zookeeper maintains the list of active brokers by creating ephemeral nodes for each broker under the path `/brokers/ids`. These nodes remain as long as the broker is active and connected to Zookeeper.
    - When a broker disconnects or crashes, Zookeeper removes its corresponding ephemeral node, marking the broker as inactive.

3. Controller Role:
    - Kafka clusters require a controller, a broker with additional responsibilities for managing cluster-level administrative tasks.
    - The controller ensures that when a broker fails, its responsibilities (like managing partitions) are reassigned to another active broker.
    - The controller is not a dedicated broker but a regular broker elected to handle extra tasks. Only one broker can act as a controller at any time in a Kafka cluster.

## Controller Election Process:
- The first broker that starts up becomes the controller by creating an ephemeral controller node in Zookeeper.
- Other brokers that start after the controller try to create this node but receive an error since the controller node already exists.
- If the controller crashes, its ephemeral node in Zookeeper is removed, and the other brokers try to become the controller by creating the node again. Only one broker succeeds in becoming the new controller.

## Broker Failures and Reassignment:
- When a broker goes offline, the controller detects it through Zookeeper and reassigns its responsibilities to other active brokers.
- If a broker comes back online after losing its controller status, it simply rejoins as a regular broker. It does not regain controller status unless a re-election is triggered.

## Example Setup and Demonstration:
- A three-node Kafka cluster uses Zookeeper to manage broker IDs and the controller election.
- Commands like ls in the Zookeeper shell can display the list of active brokers and show which broker is the current controller.
- If the current controller broker is brought down, Zookeeper will automatically elect a new controller and continue operations seamlessly.

## Partition Allocation in Kafka:

1. Self-contained Partitions:
    - Each partition is a self-contained unit, storing its segment files, indexes, and logs in its own directory. This design allows Kafka to distribute partitions across brokers in the cluster.

2. Kafka Clusters:
    - A Kafka cluster consists of multiple brokers. For large-scale production environments, brokers are often distributed across multiple racks for better reliability and fault tolerance.

## Partition Assignment in the Cluster:

To ensure load balancing and fault tolerance, Kafka follows a specific process when allocating partitions to brokers. Let's explore this step by step:

1. Replication and Distribution Goals:

    - **Even Distribution:** Kafka aims to distribute partitions evenly across brokers to balance the load.

    - **Fault Tolerance:** Duplicate copies (replicas) of partitions should be placed on different brokers and even across different racks to ensure high availability.

2. Partition Allocation Strategy:

    - Kafka creates an ordered list of brokers and assigns partitions using a round-robin approach. For example, if you create a topic with 10 partitions and a replication factor of 3, Kafka will have 30 replicas to distribute across brokers.

3. Leader and Follower Assignments:

    - **Leaders:** Kafka assigns leader partitions to brokers first. The leader is responsible for handling all requests from producers and consumers.

    - **Followers:** Kafka then assigns follower replicas, ensuring they are placed on different brokers to maintain redundancy and fault tolerance.

4. Example:

    - In a 6-broker cluster with 10 partitions and a replication factor of 3, Kafka starts by assigning leader partitions to brokers in a round-robin manner. Once all leaders are assigned, follower partitions are distributed to other brokers in the cluster, ensuring replicas are not on the same broker.

## Fault Tolerance in Kafka:
Fault tolerance is crucial for Kafka, and it is achieved through replication and careful placement of replicas across brokers and racks.

1. Replica Distribution:

    - By ensuring that replicas are distributed across different brokers and racks, Kafka guarantees that if a broker or rack goes down, the system will still have at least one active replica to serve requests.

2. In-Sync Replicas (ISR):

    - Kafka maintains a list of In-Sync Replicas (ISR), which are the replicas that are up-to-date with the leader. If a follower replica falls too far behind, it is removed from the ISR list until it catches up.

## Leader and Follower Responsibilities:

1. Leader Broker:

    - The leader broker for a partition handles all requests from producers (writing data) and consumers (reading data). It ensures the data is replicated to its follower brokers.

2. Follower Brokers:
    - Follower brokers are responsible for replicating data from the leader to stay in sync. They do not handle direct requests from producers or consumers but can take over as leaders if the current leader fails.

## Committed vs. Uncommitted Messages:

1. Committed Messages:

    - A message is considered committed once it has been replicated to all replicas in the ISR list. Committed messages are durable and cannot be lost unless all replicas fail.

2. Uncommitted Messages:

    - Messages that have not been replicated to all ISR members are uncommitted. If the leader fails, these messages may be lost, but producers can resend them if they don't receive an acknowledgment.

## Minimum In-Sync Replicas Configuration:

Kafka allows you to configure the minimum number of in-sync replicas (ISR) required for a message to be committed. For example, if you set a minimum ISR of 2 and two replicas are not in sync, the broker will stop accepting new messages for that partition to ensure data consistency.