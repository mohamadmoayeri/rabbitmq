import pika


connection=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))


ch=connection.channel()


ch.exchange_declare(exchange='topic_logs',exchange_type='topic')

result=ch.queue_declare('',exclusive=True)

qname=result.method.queue

binding_key='*.*.important'
ch.queue_bind(queue=qname,exchange='topic_logs',routing_key=binding_key)


print('waiting for message')

def callback(ch,method,propertis,body):

    with open('error_logs.log','a') as el:

        el.write(str(f'error{body}'))


ch.basic_consume(queue=qname,on_message_callback=callback,auto_ack=True)


ch.start_consuming()