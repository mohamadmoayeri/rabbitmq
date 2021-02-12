import pika

import time

connection=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

ch=connection.channel()

ch.queue_declare(queue='first',durable=True)

def callback(ch,method,properties,body):

    print(f"recieved {body}")

    print(method)

    print(properties.headers)

    time.sleep(9)

    print('done')
    ch.basic_ack(delivery_tag=method.delivery_tag)
ch.basic_qos(prefetch_count=1)

ch.basic_consume(queue='first',on_message_callback=callback)

ch.start_consuming()

    