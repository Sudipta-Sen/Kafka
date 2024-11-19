# Setup Producer for kafka

##  Kafka producer using command-line tool
-------------------------------------------

### 1. Access the Kafka container
Go inside the Kafka container
```bash
docker exec -it kafka bash
```
assume name of the container is `kafka`

### 2. Use the Kafka producer to send messages
Use the kafka-console-producer command to send messages to your Kafka topic. The Kafka binaries are usually located in `/usr/bin/`

```bash
kafka-console-producer --topic my-topic --bootstrap-server localhost:9092
```
- `--topic my-topic`: The name of the topic you want to send data to.
- `--bootstrap-server localhost:9092`: Connects to your Kafka broker running on port 9092.

### 3. Send data interactively
After running the command, we will enter interactive mode where you can type messages. Each line you type will be sent as a message to the Kafka topic.

For example:
```bash
> Hello Kafka!
> This is a test message.
> Kafka is awesome!
```

### 4. Exit the producer
To exit the producer, press `Ctrl + C`.