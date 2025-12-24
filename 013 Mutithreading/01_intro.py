# Multithreading : Used to perform multiple tasks concurrently (multitasking)
# Good for I/O bound tasks like reading file or featching data from API's
# working : threading.Trhead(target=my_function)

import threading
import time

def walk_dog(name):
    time.sleep(6)    
    print(f"You finish walking the dog named : {name}")

def take_out_trash():
    time.sleep(4)
    print("You take out the trash")

def get_mail():
    time.sleep(2)
    print("You gat the mail")

# walk_dog()
# take_out_trash()
# get_mail()

thread1 = threading.Thread(target=walk_dog, args=("Tom",))
thread1.start()

thread2 = threading.Thread(target=take_out_trash)
thread2.start()

thread3 = threading.Thread(target=get_mail)
thread3.start()

# using join method : we will wait to finish before continue to the rest of the code
thread1.join()
thread2.join()
thread3.join()

print("All threads are completed now")
