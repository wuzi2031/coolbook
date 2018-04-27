import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost'))  # localhost改成：192.168.1.118
channel = connection.channel()  # 建立了rabbit协议的通道

# 声明queue
channel.queue_declare(queue='hello')

# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()