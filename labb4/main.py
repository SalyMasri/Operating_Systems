import threading
import time
from datetime import datetime

reader_lock = threading.Semaphore(3)  # semaphore for reader access control
writer_lock = threading.Lock()  # lock for exclusive writer access

# Shared variable to simulate the shared resource
shared_resource = ""

def reader():
    #no need
    while True:
        global shared_resource
        #while loop for the lock writer instead of an is statement
        while writer_lock.locked():
            
            print('Writing...\n')
            time.sleep(2)
        else:
            reader_lock.acquire()
            print('Reading!...')
            # Simulate reading by printing the shared data
            print(f'Data: {shared_resource}\n')
            reader_lock.release()
            print('Releasing the lock')
            time.sleep(2)

def writerA():
    while True:
        global shared_resource

        writer_lock.acquire()

        for i in range(3):
            reader_lock.acquire()
        writer_lock.release()

        print('Writer is Writing!')
        # Simulate writing by updating the shared variable
        shared_resource = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        print('Stops writing!\n')

        for i in range(3):
            reader_lock.release()

        time.sleep(2)

def writerB():
    while True:
        global shared_resource

        writer_lock.acquire()

        for i in range(3):
            reader_lock.acquire()
        writer_lock.release()

        print('Writer is Writing!')
        # Simulate writing by updating the shared variable
        shared_resource = f'Writer B writes at {time.ctime()}'[::-1]
        print('Stops writing!\n')

        for i in range(3):
            reader_lock.release()

        time.sleep(2)

# Start the reader and writer threads
reader1 = threading.Thread(target=reader)
reader2 = threading.Thread(target=reader)
reader3 = threading.Thread(target=reader)
writer1 = threading.Thread(target=writerA)
writer2 = threading.Thread(target=writerB)

reader1.start()
reader2.start()
reader3.start()
writer1.start()
writer2.start()
