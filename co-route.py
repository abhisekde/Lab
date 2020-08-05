#!/bin/python3

import math
import os
import random
import re
import sys

def consumer():
    while True:
        x = yield
        print(x)

def producer(n):
    for _ in range(n):
        x = int(input())
        yield x


def rooter():
    n = 1
    while True:
        n = yield math.floor(math.sqrt(n)) # get n and, also send n**1/2
    

def squarer():
    n = 1
    while True:
        n = yield n*n # get n and, also return n**2


def accumulator():
    total = 0
    while True:
        n = 0
        n = yield total+n  # get n and, also return  n+n
        # total += n


def pipeline(prod, workers, cons):
    for num in prod:
        for i, w in enumerate(workers):
            num = w.send(num)
        cons.send(num)
    for worker in workers:
        worker.close()
    cons.close()

if __name__ == '__main__':
    order = input().strip()
    
    n = int(input())

    prod = producer(n)

    cons = consumer()
    next(cons)
    
    root = rooter()
    next(root)

    accumulate = accumulator()
    next(accumulate)

    square = squarer()
    next(square)

    pipeline(prod, eval(order), cons)
