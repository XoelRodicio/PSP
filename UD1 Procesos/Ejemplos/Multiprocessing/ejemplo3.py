import time
import multiprocessing

def daemon_worker():
   while True:
       print("Daemon worker is running")
       time.sleep(1)

if __name__ == '__main__':
   daemon_process = multiprocessing.Process(target=daemon_worker)
   daemon_process.daemon = True
   daemon_process.start()

   time.sleep(5)
   print("Main process is done")