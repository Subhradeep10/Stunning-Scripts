from scraper import find
from itertools import  permutations


if __name__=='__main__':
    word=input("Enter the Word:")

    perms=permutations(word)

    isFound=False
    real_word = []

    # Traversing all the permutations of the word
    for word in perms:
        
        # If the word is found then we append the word to the reulatnat list
        if(find(word)):
            real_word.append(''.join(word))

    # If the word has already been found, then we print the Result
    if(len(real_word)):
        print("The Possible words are:")
        for i in real_word:
            print(i)
    
    # Else we print that we could not find the word
    else:
        print("No Valid Permutation Found!!!!!")
