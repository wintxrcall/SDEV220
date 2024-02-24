# Renee Guldi
# M6, Ch 15 - 15.1
# February 24, 2024
# SDEV220 - Prof. Chris Francis

import time
import datetime
import random
import multiprocessing as mp

def print_current_time():
    wait_time = random.random()
    time.sleep(wait_time)
    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    print(f"Process {mp.current_process().name}; The current time is {current_time}. ")

if __name__ == "__main__":
    processes = []
    for i in range(3):
        process = mp.Process(target=print_current_time, name=f"{i+1}")
        processes.append(process)
        process.start()

    for process in processes:
        process.join()