import multiprocessing as mp
from random import random
from time import sleep

def simple_queue():
    queue = mp.Queue(maxsize=10)
    queue.put("Hello")
    queue.put("World")
    queue.put("!")
    print('done putting items in queue')
    while not queue.empty():
        item = queue.get()
        # NOTE: queue.qsize() does not work on unix systems like macos or linux
        
        print(f"Got {item} from queue")


    return
def producer(queue: mp.Queue) -> None:
    print('Producer: Running\n', flush=True)
    for i in range(10):
        value = random()
        sleep(value)
        queue.put(value)
    queue.put(None)
    print('Producer: Done', flush=True)
def consumer(queue: mp.Queue) -> None:
    print('Consumer: Running\n', flush=True)
    while True:
        value = queue.get()
        if value is None:
            break
        sleep(value)
        print(f'Consumer: Got item {value}', flush=True)
    print('Consumer: Done', flush=True)
def random_nos():
    queue = mp.Queue(maxsize=10)
    consumer_process = mp.Process(target=consumer, args=(queue,))
    consumer_process.start()

    producer_process = mp.Process(target=producer, args=(queue,))
    producer_process.start()

    producer_process.join()
    consumer_process.join()



def main():
    # simple_queue()
    random_nos()
if __name__=="__main__":
    main()
    