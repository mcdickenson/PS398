# sorting algorithms implemented in Ruby

def selection(list)
  for index in (0..list.length-1) # iterate over whole list
    minIndex = index
    for subIndex in (index+1..list.length-1)
      if list[subIndex] < list[minIndex]
        minIndex = subIndex
      end
    list[index], list[minIndex] = list[minIndex], list[index]
    end
  end
  list
end

print selection([5,4,3,2,1])
puts

def bubble(list)
  for index in (0..list.length-1)
    for subIndex in (0..list.length-2)
      if list[subIndex] > list[subIndex+1]
        list[subIndex], list[subIndex+1] = list[subIndex+1], list[subIndex]
      end
    end
  end
  list
end

print bubble([10,9,8,7,6])
puts

def quicksort(list)
  return [] if list.length == 0 
  pivotPoint = list[0]
  lessThanPivot = quicksort(list.select{|x| x < pivotPoint })
  equals = list.select{|x| x == pivotPoint}
  greaterThanPivot = quicksort(list.select{|x| x > pivotPoint }) 
  return lessThanPivot + [pivotPoint] + greaterThanPivot
end                            
     
print quicksort([15,14,13,12,11])
puts                      
