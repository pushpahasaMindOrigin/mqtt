import pika

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='consumer')

message_list = ["Hello this is my first message","Hello this is my second message"]
consumers_list = ["consumer_1","consumer_2"]

for message,consumer in zip(message_list,consumers_list):
    channel.basic_publish(exchange='', routing_key=consumer, body=message)
    print(f"sent message: {message}")

connection.close()
