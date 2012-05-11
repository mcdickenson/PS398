require 'csv'
require_relative 'sorter'

maxDraws = 90
repetitions = 100

selectionSortTimes = []
bubbleSortTimes = []
quickSortTimes = []
sortN = Array(10..maxDraws)

# average time for selection sort
for draw in sortN
  startTime = Time.now
  for attempt in (1..repetitions)
    tempList = Array(1..draw).shuffle
    selection(tempList)
  end 
  endTime = Time.now
  selectionSortTimes.push((endTime-startTime)/repetitions)
end

# avg time for bubble sort
for draw in sortN
  startTime = Time.now
  for attempt in (1..repetitions)
    tempList = Array(1..draw).shuffle
    bubble(tempList)
  end 
  endTime = Time.now
  bubbleSortTimes.push((endTime-startTime)/repetitions)
end

# avg time for quick sort
for draw in sortN
  startTime = Time.now
  for attempt in (1..repetitions)
    tempList = Array(1..draw).shuffle
    quicksort(tempList)
  end 
  endTime = Time.now
  quickSortTimes.push((endTime-startTime)/repetitions)
end

CSV.open("sortTimes.csv", "wb") do |csv|
  for i in (0..selectionSortTimes.length-1)
    csv << [sortN[i], selectionSortTimes[i], bubbleSortTimes[i], quickSortTimes[i]]
  end
end
  
