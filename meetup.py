#!/bin/python3

import math
import os
import random
import re
import sys

# def countMeetings(firstDay, lastDay):
#     meetups  = 0
#     max_day = max(lastDay) +1
#     meetings = set([i for i in range(1, max_day)])
#     # meet = (window_size, investor)
#     windows  = [(lastDay[i] -firstDay[i] +1, firstDay[i], lastDay[i], i) for i in range(len(firstDay))] 
#     windows.sort(key=lambda x: x[0]) 
#     # print(windows)
#     for i, meet in enumerate(windows):
#         investor_availability = [i for i in range(meet[1], meet[2] +1)]
#         slots_available = list(meetings.intersection(investor_availability))
#         # print("Check", meet, investor_availability, slots_available)
#         if len(slots_available) != 0:
#             slot_alloted = slots_available[0]
#             # print("Allocate slot", slot_alloted,"out of", slots_available, "to investor", meet[3], "within availability", investor_availability)
#             meetings.remove(slot_alloted)
#             meetups += 1
#         else:
#             # print("No slots available for investor", meet[3], "within availability", investor_availability)
#             continue
#     return meetups

# def countMeetings(firstDay, lastDay):
#     meetups  = 0
#     max_day = max(lastDay) +1
#     meetings = set([i for i in range(1, max_day)])
#     # meet: (w_size, first_d, last_d, id)
#     windows  = [(lastDay[i] -firstDay[i] +1, firstDay[i], lastDay[i], i) for i in range(len(firstDay))] 
#     windows.sort(key=lambda x: x[0]) 
#     k = 0
#     while len(meetings) != 0 and k < len(firstDay):
#         meet = windows[k]
#         k += 1
#         investor_availability = [i for i in range(meet[1], meet[2] +1)]
#         slots_available = list(meetings.intersection(investor_availability))
#         if len(slots_available) != 0:
#             slot_alloted = slots_available[0]
#             meetings.remove(slot_alloted)
#             meetups += 1
#     return meetups

def countMeetings(firstDay, lastDay):
    meetups  = 0
    max_day = max(lastDay) +1
    #meetings = set([i for i in range(1, max_day)])
    meetings = [i for i in range(1, max_day)]
    # meet = (window_size, investor)
    windows  = [(lastDay[i] -firstDay[i] +1, firstDay[i], lastDay[i], i) for i in range(len(firstDay))] 
    # windows  = [(lastDay[i] -firstDay[i] +1, firstDay[i], lastDay[i],[j for j in range(firstDay[i], lastDay[i] +1)], i) for i in range(len(firstDay))] 
    windows.sort(key=lambda x: x[0]) 
    # print(windows)
    k = 0
    while len(meetings) != 0 and k < len(firstDay):
        meet = windows[k]
        print(meet[1], ">=", meetings[0], meet[2], "<=", meetings[len(meetings) -1])
        k += 1
        #print("Start", meet[1], "End", meet[2], "In", meetings)
        #investor_availability = [i for i in range(meet[1], meet[2] +1)]
        if meet[1] >= meetings[0] or meet[2] <= meetings[len(meetings) -1]:
            slot_alloted = max(meetings[0], meet[1])
            print("Allocate slot", str(slot_alloted),"out of", meetings[0], meetings[len(meetings) -1], "to investor", meet[3], "within availability", meet[1], meet[2])
            meetings.remove(slot_alloted)
            meetups += 1
        # investor_availability = meet[3]
        #slots_available = list(meetings.intersection(investor_availability))
        # print("Check", meet, investor_availability, slots_available)
        #if len(slots_available) != 0:
        #    slot_alloted = slots_available[0]
        #    print("Allocate slot", slot_alloted,"out of", slots_available, "to investor", meet[3], "within availability", investor_availability)
        #    meetings.remove(slot_alloted)
        #    meetups += 1
        #else:
        #    print("No slots available for investor", meet[3], "within availability", investor_availability)
    return meetups
    

# if __name__ == '__main__':
#     #firstDay = [1,2,1,2,2]
#     #lastDay  = [3,2,1,3,3]
#     firstDay = [1, 10, 11]
#     lastDay = [11, 10, 11]
#     #firstDay = [1,2,3,3,3]
#     #lastDay  = [2,2,3,4,4]
#     result   = countMeetings(firstDay, lastDay)
#     print(result) # 4

if __name__ == '__main__':
    fptr = open('out.txt', 'w')

    firstDay_count = int(input().strip())

    firstDay = []

    for _ in range(firstDay_count):
        firstDay_item = int(input().strip())
        firstDay.append(firstDay_item)

    lastDay_count = int(input().strip())

    lastDay = []

    for _ in range(lastDay_count):
        lastDay_item = int(input().strip())
        lastDay.append(lastDay_item)

    result = countMeetings(firstDay, lastDay)

    fptr.write(str(result) + '\n')

    fptr.close()
