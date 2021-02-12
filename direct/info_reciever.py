import pika


connection=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))


ch=connection.channel()


ch.exchange_declare(exchange='direct_logs',exchange_type='direct')

result=ch.queue_declare(queue='',exclusive=True)

qname=result.method.queue


for i in ['error','info','warning']:

    ch.queue_bind(queue=qname,exchange='direct_logs',routing_key=i)


print('waiting for message')

def callback(ch,method,propertis,body):

    print(f'recived {method.routing_key} {body}')


ch.basic_consume(queue=qname,on_message_callback=callback,auto_ack=True)


ch.start_consuming()