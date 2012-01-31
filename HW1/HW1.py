def shout(txt):
  new_txt = txt.upper()
  if (new_txt[len(new_txt) - 1] != ".") & (new_txt[len(new_txt) - 1] != "?"):
    new_txt = new_txt + "!"
  new_txt = new_txt.replace(".", "!")  
  new_txt = new_txt.replace("?", "!")
  return new_txt
  
def reverse(txt):
  if isinstance(txt, str) == False:
    return ""
      
  return txt[::-1]
  
def reversewords(txt):
  if isinstance(txt, str) == False:
    return ""
  
  new_text = ""
  reversed_sentences = []
    
  tmp = txt.replace("?", ".")
  tmp = tmp.replace("!", ".")
  sentences = tmp.split(". ")
  sentences = [s.strip() for s in sentences if len(s.strip()) > 0]
  
  last_sentence = sentences[len(sentences) - 1]
  if last_sentence[len(last_sentence) - 1] == ".":
    sentences[len(sentences) - 1] = last_sentence[0:len(last_sentence)-1]
  
  for sentence in sentences:
    words = sentence.split()
    words.reverse()
    reversed_sentence = ""
    for word in words:
      reversed_sentence += word
      reversed_sentence += " "
    reversed_sentences.append(reversed_sentence[0:(len(reversed_sentence)-1)])
  
  for sentence in reversed_sentences:
    if len(sentence) > 0:
      new_text += sentence
      new_text += ". "

  new_text = new_text.rstrip()  
  return new_text
  
def reversewordletters(txt):
  if isinstance(txt, str) == False:
    return ""
  
  tmp_text = ""
  
  back_pointer = 0
  front_pointer = 0
  stop_chars = [" ", ".", "?", "!", ",", ":", ";"]
  if txt[len(txt)-1] not in stop_chars:
    txt = txt + " "
  for i in range(0, len(txt)):
    if txt[i] in stop_chars:
      front_pointer = i
      
      word_range = range(back_pointer, front_pointer)
      word_range.reverse()
      for j in word_range:
        tmp_text += txt[j]
      tmp_text += txt[i]
      
      back_pointer = i+1

  tmp_text = tmp_text.rstrip()
  return tmp_text
  
def piglatin(txt):
  if isinstance(txt, str) == False:
    return ""
  
  tmp = txt.replace("?", ".")
  tmp = tmp.replace("!", ".")
  sentences = tmp.split(". ")
  tmp_text = ""

  for sentence in sentences:
    words = sentence.split()
    new_sentence = ""
    for word in words:
      word = word.rstrip('.!?;:,')
      new_word = word[1:len(word)] + word[0] + "e"
      new_sentence += new_word + " "
    tmp_text += new_sentence

  tmp_text = (tmp_text.rstrip()).lower() # remove trailing spaces, chg to lowercase
  return tmp_text

