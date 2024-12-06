from kafka import KafkaProducer
import json

def serialize_data(data):
    if isinstance(data, bytes):
        return data  # Already in byte format, return as is
    else:
        return json.dumps(data).encode('utf-8')

# Kafka configuration
KAFKA_BOOTSTRAP_SERVERS =  ['localhost:8097', 'localhost:8098', 'localhost:8099']
TOPIC_NAME = 'invoice'

if __name__=="__main__":
    
    try:
        # Create a Kafka producer
        producer = KafkaProducer(
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            acks='all',  # Ensure all replicas acknowledge the message
            retries=5,   # Retry in case of failure
            value_serializer=serialize_data,
            key_serializer=serialize_data
        )

        # Test data
        key_data = {"id": 123}
        value_data = {"name": "test_data", "amount": 1000}

        print(f"Connecting to Kafka Cluster at {KAFKA_BOOTSTRAP_SERVERS}")
        print(producer)

        producer.send('invoice', key=key_data, value=value_data) # Send json data
        producer.send('invoice', key=b'key', value=b'value') # Send normal string data

    except Exception as e:
        print(f"Error sending data to Kafka: {e}")
    finally:
        # Ensure the producer is closed after the data is sent
        producer.close()
