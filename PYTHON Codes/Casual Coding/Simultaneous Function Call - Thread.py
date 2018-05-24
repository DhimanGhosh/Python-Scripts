import thread

# create a lock you can use to block the threads until you are ready
mymutex = thread.allocate_lock()

def MyConcurrentFunction():
    # important concurrent stuff
    pass

def ThreadThing():
    # thread will hang on 'acquire' until mutex is released
    mymutex.acquire()
    # release lock for the next thread
    mymutex.release()
    # now do your stuff
    MyConcurrentFunction()

mymutex.acquire()
# launch your threads
thread.start_new_thread(ThreadThing, ())
thread.start_new_thread(ThreadThing, ())
thread.start_new_thread(ThreadThing, ())
# your threads are all hung on the 'acquire' statement
# release the lock, unblocking the threads
mymutex.release()
# now all your threads are grabbing and releasing the mutex

# all done
input()
