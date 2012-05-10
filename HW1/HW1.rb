# re-implementing PS398 HW1 in Ruby

def shout(str)
  return if str.class != String
  output = str.upcase.tr("(),?!':.[]", "") + '!'
  output
end

def reverse(str)
  return if str.class != String
  output = str.reverse
  output
end

def reversewords(str)
  return if str.class != String
  temp = str.tr("(),? !':.[]", " ")
  temp = temp.split(' ')
  temp = temp.reverse
  temp = temp.join(' ')
end

def reversewordletters(str)
  return if str.class != String
  temp = str.tr("(),? !':.[]", " ")
  temp = temp.split(' ')
  #temp.each_index { |w| temp[w] = reverse(temp[w]) }
  temp = temp.map { |w| reverse(w) } 
  temp = temp.join(' ')
end
  
  
  
  
