# Create a topic in Kafka using the Dockerized setup

## Topic Creation through kafka cli tool
------------------------------------------------

### 1. Start the Kafka and Zookeeper containers
Run the dokcer-compose.yml file
```bash
docker compose -f docker-compose.yml up -d
```

### 2.  Access the Kafka container
Once the Kafka container is up and running, we can access it by running:
```bash
docker exec -it kafka bash
```

### 3. Create a Kafka topic
Now, to create a topic, we need the kafka binaries. The Kafka binaries are usually located in `/usr/bin/`

```bash
kafka-topics --create --topic my-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```
- `topic my-topic:` The name of the topic you want to create.
- `bootstrap-server localhost:9092:` Connects to the Kafka broker running on port 9092.
- `partitions 1:` Specifies the number of partitions (can be set as needed).
- `replication-factor 1:` Since you likely have a single broker in this setup, this should be 1.

### 4. Verify the topic creation
We can list all topics to verify that the topic was created successfully :
```bash
kafka-topics --list --bootstrap-server localhost:9092
```

## Topic 