#Author  : Sateesh Kalidas
#Date    : 17/Mar/2024
#Purpose : Many algorithms within Cyient/CNH project are being developed as a proto in python.
#          I would like to develop some prototype code to try our a few things.
#          None of these are production intent.
import time

# Method : spend_time_sec
# Input  : n , which is value in seconds
# Out    : None
def spend_time_sec(n):
    print(f'Process sleeping for {n} second')
    time.sleep(n)
    print(f'Process spent {n} second in sleep state')


# MAIN
# Below is an example of sequential execution.
# The total time printed will be 15s as first call to spend_time_sec executes and completed, then second call to the same method executes and completes
# This is how the cameras are being opened in , open one camera and let it complete and then open the next camera, by the time second camera is opened, the first camera has already started to stream
# i-frames into the stitching application be in Panaromic/BEV
print('START WORLD OF SEQUENTIAL EXECUTIONS')
start = time.perf_counter()
spend_time_sec(1)
spend_time_sec(1)
finish = time.perf_counter()
print(f'The time spent is {round(finish - start,2)} seconds')
print('End of Sequential executions')

# Now trying out threading for the same method. Fingers crossed !x
# This below is an exmaple of concurrent execution, meaning first sleep is printed, then next start of sleep is printed
#START WORLD OF THREADS
#Process sleeping for 1 second
#Process sleeping for 2 second
#The time spent is 0.0 seconds
#End World of threads
#Process spent 1 second in sleep state
#Process spent 2 second in sleep state
# Adopting the below method of threads will make both cameras to start concurrently (at the same time) and will make the i-frame mis-match go to zero.
import threading
print('START WORLD OF THREADS')
start = time.perf_counter()
t1 = threading.Thread(target=spend_time_sec, args=(1,))
t2 = threading.Thread(target=spend_time_sec, args=(2,))
t1.start()
t2.start()

#This is Xtreme concurrency which causes, t1 to start  -> t2 to start -> print statements which gives a value of 0.0s which is not entirely true.
# So adding a join call ensure that both threads finish their job before moving forward to compute finish time and print time.
t1.join()
t2.join()
finish = time.perf_counter()
print(f'The time spent is {round(finish - start,2)} seconds')
print('End World of threads')
