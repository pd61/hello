import random
import time
import pandas as pd
import numpy as np


class ListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ', '.join(nodes) + ']'


    def insert(self, data):
        """
        Insert a new element at the end of the list.
        Takes O(n) time.
        """
        if not self.head:
            self.head = ListNode(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(data=data)
        self.size += 1

    def find(self, key):
        """
        Search for the first element with `data` matching
        `key`. Return the element or `None` if not found.
        Takes O(n) time.
        """
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
        return curr  # Will be None if not found

    def removePosition(self, position):

        if self.head == None:
            return False

            # Store head node
        temp = self.head

        if position == 0:
            self.head = temp.next
            temp = None
            return temp.data

            # Find previous node of the node to be deleted
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break

        # If position is more than number of nodes
        if temp is None:
            return
        if temp.next is None:
            return

            # Node temp.next is the node to be deleted
        # store pointer to the next of node to be deleted
        data=temp.next.data
        next = temp.next.next

        # Unlink the node from linked list
        temp.next = None

        temp.next = next
        return data #returning fligh detail which is cancelled

    def remove(self):
        """
        Remove the first occurrence of `key` in the list.
        Takes O(n) time.
        """
        if self.size==0:
            return
        # Find the element and keep a
        # reference to the element preceding it
        temp=self.head
        self.head=temp.next
        self.size -= 1

        return temp.data
    def get_first(self):
        if self.size==0:
            return
        else:
            return self.head.data

    def getSize(self):
        return self.size


def main():

    #creating american airline queue
    american=SinglyLinkedList()
    american.insert('127 DCA 10')
    american.insert('322 BUF 11' )
    american.insert('233 FLL 12' )
    american.insert('742 LAX 13' )
    american.insert('112 CAE 14' )
    american.insert('437 LGA 15' )

    #creating delta airline queue
    delta=SinglyLinkedList()
    delta.insert('221 SFO 20')
    delta.insert('348 DET 21')
    delta.insert('765 CVG 22')
    delta.insert('612 SAN 23')
    delta.insert('148 FLL 24')

    #creating SouthWest Airline queue

    southwest=SinglyLinkedList()
    southwest.insert('345 LGA 40')
    southwest.insert('657 PHL 41')
    southwest.insert('211 BOS 42')
    southwest.insert('324 SFO 43')
    southwest.insert('367 SAN 44')
    southwest.insert('311 LAX 45')
    southwest.insert('375 FLL 46')


    #creating Runaway queue

    runaway=SinglyLinkedList()

    """Generating random number after every 2 seconds"""
    delt=0
    a=1
    y=0
    no_takeoff=0 #to check if a flight is coming to change y to not work until next 4 seconds
    curr_time=0
    filename="simulation.txt"
    file=open(filename,"w")
    while(1):
            x=random.random()
            time.sleep(2.0)
            if(delt==0):
                    if(american.getSize() == 0 and delta.getSize() == 0 and southwest.getSize()>0):
                        queue = southwest.remove()
                        runaway.insert(queue)
                        print("SouthWest flight is added in queueu. Details are :  \n")
                        print(queue)  # flight detail

                    elif (american.getSize() == 0 and southwest.getSize() == 0 and delta.getSize()>0):
                        queue = delta.remove()
                        runaway.insert(queue)
                        print("Delta flight is added in queueu. Details are :  \n")
                        print(queue)  # flight detail

                    elif (southwest.getSize() == 0 and delta.getSize() == 0 and american.getSize()>0):
                        queue = american.remove()
                        runaway.insert(queue)
                        print("American flight is added in queueu. Details are :  \n")
                        print(queue)  # flight detail

                    elif(american.getSize()==0 and delta.getSize()>0 and southwest.getSize()>0):
                        if(x<=0.5):
                            queue = delta.remove()
                            runaway.insert(queue)
                            print("Delta flight is added in queueu. Details are :  \n")
                            print(queue)  # flight detail
                        else:

                            queue = southwest.remove()
                            runaway.insert(queue)
                            print("SouthWest flight is added in queueu. Details are : \n")
                            print(queue)  # flight detail

                    elif(delta.getSize()==0 and american.getSize()>0 and southwest.getSize()>0):

                        if(x <= 0.5):
                            queue = american.remove()
                            runaway.insert(queue)
                            print("American flight is added in queueu. Details are :  \n")
                            print(queue)  # flight detail
                        else:

                            queue = southwest.remove()
                            runaway.insert(queue)
                            print("SouthWest flight is added in queueu. Details are : \n")
                            print(queue)  # flight detail

                    elif (southwest.getSize() == 0 and delta.getSize()>0 and american.getSize()>0):

                        if (x <= 0.5):
                            queue = american.remove()
                            runaway.insert(queue)
                            print("American flight is added in queueu. Details are :  \n")
                            print(queue)  # flight detail
                        else:
                            queue = delta.remove()
                            runaway.insert(queue)
                            print("Delta flight is added in queueu. Details are :  \n")
                            print(queue)  # flight detail

                    elif(american.getSize()>0 and delta.getSize()>0 and southwest.getSize()>0):
                        if(x<=0.33):

                            queue=american.remove()
                            runaway.insert(queue)
                            print("American flight is added in queueu. Details are : \n")
                            print(queue) #flight detail

                        elif(x<=0.67):
                            queue=delta.remove()
                            runaway.insert(queue)
                            print("Delta flight is added in queueu. Details are :  \n")
                            print(queue)  # flight detail
                        else:

                            queue = southwest.remove()
                            runaway.insert(queue)
                            print("SouthWest flight is added in queueu. Details are : \n")
                            print(queue)  # flight detail
                    elif (american.getSize() == 0 and delta.getSize() == 0 and southwest.getSize() ==0):

                        delt=1



            if (a % 2 == 0):

                if (runaway.getSize() == 0 and delt == 1):
                    print('No flight awaiting in runaway and airport.')
                    file.write('No flight awaiting in runaway and airport.')
                    break

                y = random.random()
                c_time=time.time()
                if(c_time-curr_time>=4.0):
                    no_takeoff=0

                if (y <= 0.5 and no_takeoff==0):
                    takeoff_flight = runaway.remove()
                    print('Flight took off from the runaway.')
                    print('Flight Detail : \n')
                    print(takeoff_flight)
                    file.write('Flight took off from the runaway.')
                    file.write(takeoff_flight)

                    #random generation for cancellation of flight
                    z=random.random()
                    if(z<=0.1):
                        if(american.getSize()>0):
                            cancelled_flight=american.remove()
                            print('\nAmerican Airline with following details has been cancelled. \n')
                            print(cancelled_flight)
                            file.write('Airline with following details has been cancelled.')
                            file.write(cancelled_flight)
                    elif(z>=0.50 and z<=0.60):
                        if (delta.getSize() > 0):
                            cancelled_flight = delta.remove()
                            print('\nDelta Airline with following details has been cancelled. \n')
                            print(cancelled_flight)
                            file.write('Airline with following details has been cancelled.')
                            file.write(cancelled_flight)
                    elif(z>=0.80 and z<=0.90):
                        if (southwest.getSize() > 0):
                            cancelled_flight = southwest.remove()
                            print('\nSouthWest Airline Flight with following details has been cancelled. \n')
                            print(cancelled_flight)
                            file.write('Airline with following details has been cancelled.')
                            file.write(cancelled_flight)



                elif(y>0.5):
                    no_takeoff = 1
                    curr_time = time.time()
                    print('There is no takeoff this time until 4 seconds. As a flight is approaching runaway. \n')
                    print('Flight to wait in runaway queue : \n')
                    print(runaway.get_first())
                    file.write('Flight to wait in runaway queue : ')
                    file.write(runaway.get_first())




                print('Flights in runaway queue : \n')
                print(runaway)
                print('American Flights at airport gate:\n')
                print(american)
                print('Delta Flights at airport gate: \n')
                print(delta)
                print('Southwest Flights at airport gate: \n')
                print(southwest)



            a=a+1
    file.close()

main()





