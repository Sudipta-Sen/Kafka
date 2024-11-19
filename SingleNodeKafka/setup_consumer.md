# Setup Consumer for kafka

##  Kafka consumer using command-line tool
--------------------------------------------

### 1. Access the Kafka container
Go inside the Kafka container
```bash
docker exec -it kafka bash
```
assume name of the container is `kafka`

### 2. Use the Kafka consumer to send messages
Use the kafka-console-consumer command to send messages to your Kafka topic. The Kafka binaries are usually located in `/usr/bin/`

```bash
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic <topic_name> --from-beginning --partition 0
```

- `--bootstrap-server`: Specifies the address of the Kafka broker.
- `--topic`: The name of the Kafka topic from which you want to consume messages.
- `--from-beginning`: This optional flag ensures that you consume all the messages from the beginning of the topic, even the ones produced before the consumer started.

### 3. Stop the Consumer
You can stop the consumer by pressing Ctrl+C.