# -*- coding: utf-8 -*-
# Χρησιμοποιεί heapq
import heapq


class PriorityQueue(object):
    def __init__(self, list_input = None):
        """
        Constructor για το αντικείμενο PriorityQueue
        :param list_input: λίστα με αρχικές τιμές, αν έχουμε δηλώσει
        """
        if list_input is None:
            self.heap = []
            self.count = 0
        else:
            self.heap = list(list_input)
            heapq.heapify(self.heap)
            self.count = len(list_input)
        return

    def push(self, item, priority):
        """
        Λειτουργία push
        :param item: τιμή
        :param priority: προτεραιότητα
        :return:
        """
        self.count += 1
        heapq.heappush(self.heap, (priority, item))
        return

    def pop(self):
        """
        Λειτουργία pop.
        Ελέγχει αν η τιμή είναι tuple ή όχι.
        :return: την τιμή ή None αν δεν υπάρχει
        """
        if not self.isEmpty():
            self.count -= 1
            popped = heapq.heappop(self.heap)
            if type(popped) is list:
                return popped[1]
            else:
                return popped
        else:
            return None

    def isEmpty(self):
        """
        Ελέγχει αν ο σωρός είναι κενός.
        :return: Αληθές αν είναι κενός.
        """
        if self.count is 0:
            return True
        else:
            return False

    def update(self, item, priority):
        """
        Ενημερώνει την προτεραιότητα μιας τιμής.
        :param item: τιμή
        :param priority: προτεραιότητα
        :return:
        """
        for i in range(0, len(self.heap)):
            if self.heap[i][1] is item:
                if self.heap[i][0] <= priority:
                    return
                else:
                    self.heap[i] = (priority, item)

        return

def PQSort(input_list):
    """
    Ταξινομεί μια λίστα αριθμών.
    :param input_list: η λίστα
    :return: μια ταξινομημένη λίστα
    """
    mypq = PriorityQueue(input_list)
    sorted_list = []
    while not mypq.isEmpty():
        sorted_list.append(mypq.pop())

    return sorted_list

pq = []
q = PriorityQueue()

q.push("task1", 1)
q.push("task1", 2)
q.push("task0", 0)
t = q.pop()
print(t)
t = q.pop()
print(t)
q.push("task3", 3)
q.push("task4", 4)
q.push("task2", 0)
t = q.pop()
print(t)

### Παράδειγμα
#ttt = [2, 6, 1, 4, 3, 10, 0]
#print PQSort(ttt)