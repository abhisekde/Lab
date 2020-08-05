#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'predictAnswer' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY stockData
#  2. INTEGER_ARRAY queries
#

def predictAnswer(stockData, queries):
    result = []
    maxVal = max(stockData) +1
    minList = [None]*maxVal
    for i, stock in enumerate(stockData):
        # print(stock, minList[stock], i) #.append(i)
        l = minList[stock]
        if l is None:
            l = [i]
        else: 
            l.append(i)
        #print(stock, l)
        minList[stock] = l
    
    for qd in queries:
        iList = [i if i < stockData[qd] else -1 for i in range(1, len(minList)+1)]

    print(iList)

    result = minList
    # bt = [None] *(4*len(stockData))
    # for i, stock in enumerate(stockData):
    #     p = 1 # head position of our binary tree
    #     while bt[p] is not None:
    #         # print("Compare {}, {}".format(stock, bt[p]))
    #         p = 2*p +1 if stock >= stockData[bt[p]] else 2*p 
    #     # print("Allocate {} at position {}".format(stock, p))
    #     bt[p] = i # Note the index
    # print(bt)
    # print([stockData[i] if i is not None else None for i in bt])
    # i = 0
    # for dn in queries:
    #     p = 1;f = -1 
    #     dn -= 1 # day number is 1 based index
    #     query = stockData[dn]
    #     curr_value = stockData[bt[p]] if bt[p] is not None else -1
    #     print("if {} != {}".format(query, curr_value))
    #     while bt[p] is not None: 
    #         print(">  {} != {}".format(query, curr_value))
    #         if query == curr_value:
    #             break
    #         p = p*2 +1 if query >= curr_value else p*2
    #         f = 0 # go to left, also mark as found
    #         curr_value = stockData[bt[p]] if bt[p] is not None else -1
    #     if f != -1:
    #         p = int(p/2) 
    #         print(">  {} at {}".format(stockData[bt[p]], bt[p]))
    #     else:
    #         p = -1
    #     result.append(p)
    return result

if __name__ == '__main__':
    stockData = [5, 6, 8, 4, 9, 10, 8, 3, 6, 4]
    queries = [3, 1, 8] 
    result = predictAnswer(stockData, queries)
    print(result)
