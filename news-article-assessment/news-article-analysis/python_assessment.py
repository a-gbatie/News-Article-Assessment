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


# print(most_common_word("Apple pie apple banana apple"))
# print(most_common_word("Python python PYTHON"))
# print(most_common_word(""))
# print(most_common_word(article))

def calculate_average_word_length(text):
  words = text.split()
  char = 0
  count = 0
  
  for word in words:
    str = "".join(char for char in word if char.isalnum()) # Removes punctuation and special charcters, checks if character is letter or number, joins accepted characters into new string
    
    if str:
      char += len(str)
      count += 1
  
  if count == 0:
    return 0.0
  
  return char / count

# print(calculate_average_word_length("I love Python"))
# print(calculate_average_word_length("Hi! Hello."))
# print(calculate_average_word_length(""))
# print(calculate_average_word_length("!!!"))
# print(calculate_average_word_length(article))

def count_paragraphs(text):
  paragraphs = text.strip().split("\n\n")
  return len(paragraphs)

# print(count_paragraphs("First paragraph.\n\nSecond paragraph."))
# print(count_paragraphs("Just one paragraph."))
# print(count_paragraphs(""))
# print(count_paragraphs("One.\n\nTwo.\n\nThree."))
# print(count_paragraphs(article))
