# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

print("Wanna know if two words are anagrams? -- Enter")
def find_anagram(word, anagram):
    # [assignment] Add your code here

     

    if(sorted(word)== sorted(anagram)):
        return("True")
    else:
        return("False")        
         
         
word = input("Input the Word: \t")
anagram = input("Input the possible anagram: \t")
print(find_anagram(word, anagram))
    

