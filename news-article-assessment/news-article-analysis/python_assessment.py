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


print(count_specific_word("Apple pie apple", "apple"))
print(count_specific_word("Pie, pie! PIE.", "pie"))
print(count_specific_word("Apple pie", "banana"))
print(count_specific_word(article, "pie"))
