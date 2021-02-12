import pika


connection=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))


ch=connection.channel()


ch.exchange_declare(exchange='direct_logs',exchange_type='direct')

result=ch.queue_declare(queue='',exclusive=True)

qname=result.method.queue


ch.queue_bind(queue=qname,exchange='direct_logs',routing_key='error')


print('waiting for message')

def callback(ch,method,propertis,body):

    with open('error_logs.log','a') as el:
        el.write(str(f'{body}')+'\n')


ch.basic_consume(queue=qname,on_message_callback=callback,auto_ack=True)


ch.start_consuming()