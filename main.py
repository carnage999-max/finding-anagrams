# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here

     

    if(sorted(word)== sorted(anagram)):
        return("True\nThe strings are anagrams.")
    else:
        return("False\nThe strings aren't anagrams.")        
         
         
word = input("Input the Word: \t")
anagram = input("Input the possible anagram: \t")
print(find_anagram(word, anagram))
    

