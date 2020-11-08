import os, time
from concurrent.futures import ThreadPoolExecutor

print("hi outside of main()")

def hello(x):
    print("inside hello()")
    print("Proccess id: ", os.getpid())
    time.sleep(3)
    return x*x

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = executor.map(hello, range(3))
        for result in results:
            print(result)