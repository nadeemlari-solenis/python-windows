import pika, os, time

# def process_message(msg):
#   print("Message is \n")
#   print(str(msg))
#   time.sleep(0.1) # delays for 0.5 seconds
  

params = pika.URLParameters("")
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
allQs=["dlq-digi-measurements","dlq-realtiteq-alarms","dlq-realtiteq-measurements1","dlq-realtiteq-measurements2","dlq-realtiteq-measurements3","dlq-realtiteq-measurements4","dlq-realtiteq-measurements5","dlq-realtiteq-measurements6","dlq-realtiteq-measurements7","dlq-realtiteq-measurements8","dlq-realtiteq-measurements9","dlq-realtiteq-measurements10","dlq-realtiteq-measurements11","dlq-realtiteq-measurements12","dlq-realtiteq-measurements13","dlq-realtiteq-measurements14","dlq-realtiteq-measurements15"]
for q in allQs:
    frame = channel.queue_declare(queue=q,durable=True,passive=True) 
    message_count = frame.method.message_count
    
    if message_count>0:
      channel.queue_purge(queue=q)
      print("Queue "+q+" --> purged \t\t"+str(message_count)+" messages")
  
# channel.queue_declare(queue='temp-bkup',durable=True) # Declare a queue with name temp-bkup (not necessary as already declared 

# create a function which is called on incoming messages
# def callback(ch, method, properties, body):
#   process_message(body)

# set up subscription on the queue
# for q in allQs:
#     channel.basic_consume(q,  callback,  auto_ack=True)
# channel.basic_consume("temp-bkup",  callback,  auto_ack=True)

# start consuming (blocks)
# channel.start_consuming()
channel.close()
connection.close()
print("\n\nauto close in 2 sec")
time.sleep(2) # delays for 5 seconds

