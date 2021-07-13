def open_file(filename):
  file = open(filename, "rt") #open a file for reading
  list_of_lines = file.readlines() #read each line into a list 
  list_of_words = [] #create an empty list 
  for line in list_of_lines:
    line_split = line.split() #split each line into a list of words
    for word in line_split:
      list_of_words.append(word) #add each word to the list
    list_of_words.append("\n") #add a newline character at the end of each line
  return list_of_words

def write_file(filename, list_of_words):
  file = open(filename, "w")
  for word in list_of_words:
    #how do you add the word to the file?
    if word != "\n": 
      file.write(word + " ") #add a space after every word
    else:
      file.write(word) #dont add a space at the end of the line
  file.close()