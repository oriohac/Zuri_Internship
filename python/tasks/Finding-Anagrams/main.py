# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True



def find_anagram(word, anagram):
    # [assignment] Add your code here
 
        if word == anagram:
           return True
        else:
           return False
word = input("Enter Text: ")
anagram = input("Enter Second Text To Test For Anagram: ")
word = word.replace(" ","")
anagram = anagram.replace(" ","")
word = word.lower()
anagram = anagram.lower()
if len(word)==len(anagram):
        word = sorted(word)
        anagram = sorted(anagram)
find_anagram(word, anagram)
