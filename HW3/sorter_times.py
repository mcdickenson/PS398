import csv
import random
import math
import time
import sorter


# recorded time will be average of 100 trials on 90 random lists
maxDraws = 100
repetitions = 100

selection_sort_times = []
bubble_sort_times = []
quick_sort_times = []
sort_N = range(10, maxDraws)


# Selection sort
for draw in range(10,maxDraws):
    start= time.clock()
    for attempt in range(repetitions):
        toSort = random.sample(range(0,maxDraws), int(draw))
        sorter.selection(toSort)
    end= time.clock()
    selection_sort_times.append((end-start)/repetitions)

# Bubble Sort
for draw in range(10,maxDraws):
    start= time.clock()
    for attempt in range(repetitions):
        toSort = random.sample(range(0,maxDraws), int(draw))
        sorter.bubble(toSort)
    end= time.clock()
    bubble_sort_times.append((end-start)/100)

# Quick Sort (well, we'll see...)
for draw in range(10,maxDraws):
    start= time.clock()
    for attempt in range(repetitions):
        toSort = random.sample(range(0,maxDraws), int(draw))
        sorter.quicksort(toSort)
    end= time.clock()
    quick_sort_times.append((end-start)/100)
      
#Write these times to a csv names times.csv where each time gets its own column
csvWriter = csv.writer(open('times.csv', 'wb'))

for i in range(0,len(selection_sort_times)):
  csvWriter.writerow([sort_N[i], selection_sort_times[i], bubble_sort_times[i], quick_sort_times[i]])

