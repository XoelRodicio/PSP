# Python program to understand 
# the concept of pool
import multiprocessing
import os
  
def square(n):
    print("Worker process id for {0}: {1}".format(n, os.getpid()))
    return (n*n)
  
if __name__ == "__main__":
    # input list
    mylist = [n for n in range(1000)]
  
    # creating a pool object
    p = multiprocessing.Pool()
  
    # map list to target function
    result = p.map(square, mylist)
  
    print(result)