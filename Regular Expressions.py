#1. Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)#
'''import re
a="usha123"
b=re.compile(r'[a-zA-Z0-9]')
c=b.search(a)
print(not(c))'''

##2. Write a Python program that matches a string that has an a followed by zero or more b's
'''import re
a="012abbb"
b="ab+?"
if re.search(b,a):
    print("found")
else:
    print("not found")'''

##3. Write a Python program that matches a string that has an a followed by one or more b's.
'''import re
a="11112aab"
b="ab+?"
if re.search(b,a):
    print("found")
else:
    print("not found")'''
##4. Write a Python program that matches a string that has an a followed by zero or one 'b'.
'''import re
a="0ab"
b="ab?"
if re.search(b,a):
    print("found")
else:
    print("not found")'''
##5. Write a Python program that matches a string that has an a followed by three 'b'
import re
a="012abbbb"
b="b+?"
if re.search(b,a):
    print("found")
else:
    print("not found")
##6. Write a Python program that matches a string that has an a followed by two to three 'b'. 
##7. Write a Python program to find sequences of lowercase letters joined with a underscore.
##8. Write a Python program to find the sequences of one upper case letter followed by lower case letters.\
##9. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
##10. Write a Python program that matches a word at the beginning of a string.
##11. Write a Python program that matches a word at the end of string, with optional punctuation.
##12. Write a Python program that matches a word containing 'z'.
##13. Write a Python program that matches a word containing 'z', not at the start or end of the word.
##14. Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.
##15. Write a Python program where a string will start with a specific number.
##16. Write a Python program to remove leading zeros from an IP address.
##17. Write a Python program to check for a number at the end of a string.
##18. Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string.
##19. Write a Python program to search some literals strings in a string. Go to the editor
##Sample text : 'The quick brown fox jumps over the lazy dog.'
##Searched words : 'fox', 'dog', 'horse'
##20. Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs. Go to the editor
##
##Sample text : 'The quick brown fox jumps over the lazy dog.'
##Searched words : 'fox'
##21. Write a Python program to find the substrings within a string. Go to the editor
##
##Sample text :
##
##'Python exercises, PHP exer
