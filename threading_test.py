import threading
from queue import Queue
import time


# print_lock = threading.Lock()

# def exampleJob(worker):
#     time.sleep(.5)
#     with print_lock:
#         print(threading.current_thread().name, worker)

# def threader():
#     while True:
#         # gets an worker from the queue
#         worker = q.get()
#         # Run the example job with the avail worker in queue (thread)
#         exampleJob(worker)
#         # completed with the job
#         q.task_done()
        
# q = Queue()
# for x in range(10):
#     t = threading.Thread(target = threader)
#     t.deamon = True
#     t.start()

# start = time.time()

# for worker in range(20):
#     q.put(worker)

# q.join()

# print("Entire job took:", time.time()-start)

#print(sys.version)

#############################################################
#_thread
#############################################################
def print_time(threadName, delay):
   count=0
   while count<5:
       time.sleep(delay)
       count +=1
       print("%s: %s" % (threadName, time.ctime(time.time())))
try:
   _thread.start_new_thread(print_time, ("Thread-1",2,))
   _thread.start_new_thread(print_time, ("Thread-2",4,))
except:
   print("Error: unable to start thread")

while 1:
   pass

