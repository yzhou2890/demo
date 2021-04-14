


# example of creating a thread - naive style

# see demo_oop.py for a single thread example designed with object-oriented programming
# see demo_mthread.py
#     demo_multiplethread.py for more powerful examples

import thread


def child(tid):
    print('Hello thread ', tid)
    return tid


def parent():
    i = 0
    while 1:
        i = i+1
        thread.start_new(child,(i,))
        if raw_input() == 'q': 
            break


parent()



