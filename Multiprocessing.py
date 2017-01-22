import multiprocessing

def spawn(num1, num2):
    print('Spawned! {} {}'.format(num1, num2))

#means it will run only being called directly, not by othr process
if __name__ == '__main__':
    for i in range(50):
        p = multiprocessing.Process(target=spawn, args=(i,i+1))
        p.start()
        #waiting for the process to be complete
        p.join()
