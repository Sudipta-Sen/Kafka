# Kafka Producer

These exists an example of an existing Kafka Producer implementation [Here](../StorageArchitecture/produceData.py)

## Kafka Producer Workflow Overview
- Set the configuration for the producer.
- Create the producer object.
- Send messages using the send() method.
- Close the producer after sending all messages.

In Python, we typically combine the first and second steps of creating a Kafka producer into a single action. 

##  ProducerRecord Object

- Each message must be wrapped in a ProducerRecord object.
- ProducerRecord includes:
    - **Topic Name:** Destination where the message will be sent.
    - **Message Value:** Actual content of the message.
    - **Optional fields:** 
        - Message Key
        - Target Partition
        - Message Timestamp.

- The `ProducerRecord` object is used in java. In Python, when sending messages with Kafka using the `KafkaProducer`, there is no separate `ProducerRecord` object. Instead, the `producer.send()` method directly takes the parameters.

## Serialization

- Kafka serializes the message before sending it over the network.
- Key and value must be serialized using serializers like `StringSerializer` or custom serializers (e.g., JSON, Avro).
- **Custom Serializers:** Useful for complex Java objects or other data formats.

## Partitioning in Kafka
- Kafka topics are partitioned. The producer determines the partition to send the message to.

- Two ways to assign partitions:
    1. **Explicit Partitioning:** Specify partition number in the ProducerRecord.
    2. **Default Partitioner:** Uses either hash-based partitioning (when a key is provided) or round-robin (when the key is absent).

- Custom partitioners can be implemented, but the default one is generally sufficient for most use cases.

##  Message Timestamp

- Kafka provides two types of timestamps:
    1. Create Time: Time when the producer created the message.
    2. Log Append Time: Time when the broker received the message.

- The timestamp configuration can be set at the topic level.

## Buffering and Network Transmission
- Kafka producer buffers messages before sending them to the broker.
- This allows the producer to send messages asynchronously.
- The buffer size can be configured using the buffer.memory property (default: 32MB).
- If the buffer is full, the send() method may block or throw a TimeoutException.

## Retries and Acknowledgement
- The producer’s background I/O thread sends the message to the broker and waits for an acknowledgment.
- If the broker fails to acknowledge, the producer retries sending the message.
- The number of retries is controlled by the retries property.
- If all retries fail, the producer returns an error.

## Producer Process Summary
- **Serialization:** The message is serialized (key and value).
- **Partitioning:** The partition number is determined.
- **Buffering:** The message is stored in a buffer.
- **Transmission:** The background I/O thread sends the message to the broker.
- **Acknowledgement:** The broker responds with success or failure.
- If the producer doesn’t get an acknowledgment, it retries and eventually returns an error if unsuccessful.

    ![plot](Pictures/1.jpeg)