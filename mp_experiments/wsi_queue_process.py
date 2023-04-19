import numpy as np
import multiprocessing as mp
from skimage import io 
import openslide as ops




def produce_tiles(filepath: str, queue: mp.Queue) -> None:
    print('Producer: Running\n', flush=True)
    slide = ops.OpenSlide(filepath)
    
    




def main():
    return
if __name__=="__main__":
    main()
