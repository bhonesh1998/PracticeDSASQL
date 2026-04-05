

'''

queue
FIFO
elec bill queue ->  A , B , C , D
FIRST IN FIRST OUT
ENQUEUE
DEQUEUE


'''

queue1 = []


def enqueue(queue1 , element):
    queue1.append(element)
    return queue1


def dequeue(queue1):
    len_queue = len(queue1)
    if len_queue==0:
        print("queue is already empty we can not dequeue anything")
        return []
    else:
        temp = queue1.pop(0)
        print("dequeued element is : ",temp)
        return queue1

def print_queue(queue1):
    print(queue1)


enqueue(queue1,100)

print_queue(queue1)

enqueue(queue1,60)

print_queue(queue1)

enqueue(queue1,50)

print_queue(queue1)

dequeue(queue1)

print_queue(queue1)

dequeue(queue1)

print_queue(queue1)


dequeue(queue1)

print_queue(queue1)


dequeue(queue1)

print_queue(queue1)











