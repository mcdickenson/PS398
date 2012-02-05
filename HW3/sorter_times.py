import csv
import random
import math
import time
import sorter

selection_sort_times = []
bubble_sort_times = []
quick_sort_times = []
sort_times_N = range(10,100)


for draw in range(10,100):
    toSort = random.sample(range(0,100), int(draw))
    start= time.clock()
    for attempt in range(100):
        sorter.selection(toSort)
    end= time.clock()
    selection_sort_times.append((end-start)/100)
    # recorded time will be average of 100 trials on 90 random lists
  
#Write these times to a csv names times.csv where each time gets its own column
csvWriter = csv.writer(open('times.csv', 'wb'))

for i in range(0,len(selection_sort_times)):
  csvWriter.writerow([selection_sort_times[i]])



