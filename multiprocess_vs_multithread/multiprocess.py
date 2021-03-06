# 'outside' printed 5 times because each newly spawned process will load the module
# reference https://stackoverflow.com/questions/46045956/whats-the-difference-between-threadpool-vs-pool-in-the-multiprocessing-module

from multiprocessing import Pool
import os, time

print("hi outside of main()")

def hello(x):
    print("inside hello()")
    print("Proccess id: ", os.getpid())
    time.sleep(3)
    return x*x

if __name__ == "__main__":
    p = Pool(5)
    pool_output = p.map(hello, range(3))

    print(pool_output)