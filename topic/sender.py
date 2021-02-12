import pika


connection=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))


ch=connection.channel()


ch.exchange_declare(exchange='topic_logs',exchange_type='topic')


messages={

    'error.warning.important':'this is importang  message',

    'info.debug.notimportant':'this is not important  message',
}

print ('message sent')

for k,v in messages.items():

     ch.basic_publish(exchange='topic_logs',routing_key=k,body=v)


connection.close()