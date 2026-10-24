with open("news-article.txt", "r", encoding="utf-8") as file: # Open file in read mode
  article = file.read() # Reads article into one string, saved into varible that can be accessed later
# print(article)

def count_specific_word(text, search_word): # Accepts article and word to find as variables
  words = text.lower().split() # Splits article into lowercase list of words
  count = 0 # Starts counter at 0
  
  for word in words: # Go through each word
    if word.strip(".,!?;:\"'()") == search_word.lower(): # Removes punctuation and checks whether both words match
      count += 1 # Increment counter for each match
      
  return count

# print(count_specific_word("Apple pie apple", "apple"))
# print(count_specific_word("Pie, pie! PIE.", "pie"))
# print(count_specific_word("Apple pie", "banana"))
# print(count_specific_word(article, "pie"))

def most_common_word(text):
  words = text.lower().split()
  word_counter = {} # Create empty dictionary
  
  for word in words:
    word = word.strip(".,!?;:\"'()“”’")
    
    if word in word_counter: # If word is already in dictionary increment by one, if not, initialize it with 1
      word_counter[word] += 1
    else:
      word_counter[word] = 1
  
  if not word_counter: # If dictionary is empty return None because there is no most common word
    return None
  
  return max(word_counter, key=word_counter.get) # Tells Python to compare counts associated with each word instead of comparing the words themselves. For example, "apple" appears 3x and "pie" appears 1x, Python returns "apple".


print(most_common_word("Apple pie apple banana apple"))
print(most_common_word("Python python PYTHON"))
print(most_common_word(""))
print(most_common_word(article))

  


