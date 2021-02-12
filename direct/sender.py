import pika


connection=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))


ch=connection.channel()


ch.exchange_declare(exchange='direct_logs',exchange_type='direct')


messages={

    'error':'this is error  message',

    'info':'this is info  message',

    'warning':'this is warning  message',
}

for k,v in messages.items():

     ch.basic_publish(exchange='direct_logs',routing_key=k,body=v)


connection.close()