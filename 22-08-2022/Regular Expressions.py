#1.Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)

'''import re
def char(s):
    c=re.compile(r'[^a-zA-Z0-9]')
    s=c.search(s)
    return not bool(s)
print(char("ADFaagg123"))
print(char("*&%@#!}{"))
output:
True
False
'''


#without using functions
'''import re
s="ADFasgg34"
c=re.compile(r'[^a-zA-Z0-9]')
s=c.search(s)
print(not bool(s))

output:
True'''


#2. Write a Python program that matches a string that has an a followed by zero or more b's

'''import re
s="ab"
p='^a(b*)$'
if re.search(p,s):
    print("found")
else:
    print("not found")

output:
found'''


#3.Write a Python program that matches a string that has an a followed by one or more b's.

'''import re
s="aaab"
p='ab+?'
if re.search(p,s):
    print("found")
else:
    print("not found")

output:
found'''


#4. Write a Python program that matches a string that has an a followed by zero or one 'b'.

'''import re
s="adcfdb123"
p="ab?"
if re.search(p,s):
    print("found")
else:
    print("not found")

output:

found'''

#5. Write a Python program that matches a string that has an a followed by three 'b'

'''import re
s="abbb"
p='ab{3}?'
if re.search(p,s):
    print("found")
else:
    print("not found")
output:

found'''

#6.Write a Python program that matches a string that has an a followed by two to three 'b'.

'''import re
s="abb"
p="ab{2,3}"
if re.search(p,s):
    print("found")
else:
    print("not found")
output:

found'''

#7. Write a Python program to find sequences of lowercase letters joined with a underscore.

'''import re
s="achjhv_fuf"
p="^[a-z]+_[a-z]+$"
if re.search(p,s):
    print("found")
else:
    print("not")

output:

found'''

#8. Write a Python program to find the sequences of one upper case letter followed by lower case letters.

'''import re
s="AFGGajlifoe"
p="^[A-Z]+[a-z]+$"
if re.search(p,s):
    print("found")
else:
    print("not")
output:
found'''

#9. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

'''import re
s="aabbb"
p="a.*?b$"
if re.search(p,s):
    print("found")
else:
    print("not")
output:

found'''

#10.WAP that matches a word at the beginning of a string.


'''import re
s="the quick brown fox jumps over the lazy dog."
p="^\w+"
if re.search(p,s):
    print("found")
else:
    print("not")
output:

found'''

#11.WAP that matches a word at end of string ,with optional punctuation.

'''import re
s="this is a tree."
p="\w+\S*$"
if re.search(p,s):
    print("found")
else:
    print("not")

output:

found'''

#12.WAP that matches a word containing 'Z'.

'''import re
s="a zoo"
p="\w*z.\w*"
if re.search(p,s):
    print("found")
else:
    print("not")
output:
found'''

#13.WAP that matches a word containing 'Z' not at the start or end of the word.

'''import re
s="the apple is lazy."
p="\Bz\B"
if re.search(p,s):
    print("found")
else:
    print("not")

output:
found'''

#14.Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.

'''import re
def fun(text):
    p="^[a-zA-Z0-9_]*$"
    if re.search(p,text):
        return "found"
    else:
        return "not"
print(fun("The quick brown fox12 jumps over_123."))
print(fun("Python_Exercise_1"))

output:
not
found'''

#15.Write a Python program where a string will start with a specific number.

'''import re
def fun(s):
    a=re.compile(r"^5")
    if a.match(s):
        return True
    else:
        return False
print(fun('5-233'))
print(fun('6-654'))

output:
True
False'''

#16.Write a Python program to remove leading zeros from an IP address.

'''import re
ip="2175.086.8998"
s=re.sub("\.[0]*",".",ip)
print(s)

output:
 2175.86.8998'''

#17. Write a Python program to check for a number at the end of a string

'''import re
def fun(n):
    t=re.compile(r".*[0-9]$")
    if t.match(n):
        return True
    else:
        return False
print(fun('addffhhg'))
print(fun('sgfgfh7'))

output:
False
True'''

#18.Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string. Go to the editor

'''import re
r=re.finditer(r"([0-9]{1,3})","Exercise number 1,12,13,2334 and 345 are important")
print("number of the lenght 1 to 3")
for i in r:
    print(i.group(0))

output:

number of the lenght 1 to 3
1
12
13
345'''

##19. Write a Python program to search some literals strings in a string. Go to the editor
##Sample text : 'The quick brown fox jumps over the lazy dog.'
##Searched words : 'fox', 'dog', 'horse'
##
'''import re
p= [ 'fox', 'dog', 'horse' ]
t = 'The quick brown fox jumps over the lazy dog.'
for i in p:
    print('Searching for "%s" in "%s" ->' % (i, t),)
    if re.search(i,t):
        print('Matched!')
    else:
        print('Not Matched!')

output:
Searching for "fox" in "The quick brown fox jumps over the lazy dog." ->
Matched!
Searching for "dog" in "The quick brown fox jumps over the lazy dog." ->
Matched!
Searching for "horse" in "The quick brown fox jumps over the lazy dog." ->
Not Matched!'''

#20.Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs.

'''import re
pattern = 'fox'
text = 'The quick brown fox jumps over the lazy dog.'
match = re.search(pattern, text)
s = match.start()
e = match.end()
print('Found "%s" in "%s" from %d to %d ' % \
    (match.re.pattern, match.string, s, e))
output:
Found "fox" in "The quick brown fox jumps over the lazy dog." from 16 to 19 
'''

#21. Write a Python program to find the substrings within a string.
##Sample text :
##
##'Python exercises, PHP exercises, C# exercises'
##
##Pattern :
##
##'exercises'
##
##Note: There are two instances of exercises in the input string

'''import re
text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for match in re.findall(pattern, text):
    print('Found "%s"' % match)

output:
Found "exercises"
Found "exercises"
Found "exercises"
'''
#22. Write a Python program to find the occurrence and position of the substrings within a string.

'''import re
text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('Found "%s" at %d:%d' % (text[s:e], s, e))
	
output:
Found "exercises" at 7:16
Found "exercises" at 22:31
Found "exercises" at 36:45'''

#23. Write a Python program to replace whitespaces with an underscore and vice versa.

'''import re
text = 'Python Exercises'
text =text.replace (" ", "_")
print(text)
text =text.replace ("_", " ")
print(text)

output:
Python_Exercises
Python Exercises'''

#24. Write a Python program to extract year, month and date from an url.

'''import re
def extract_date(url):
        return re.findall(r'/(\d{4})/(\d{1,2})/(\d{1,2})/', url)
url1= "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"
print(extract_date(url1))

output:
[('2016', '09', '02')]'''


#25. Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.

''''import re
def change_date_format(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)
dt1 = "2026-01-02"
print("Original date in YYY-MM-DD Format: ",dt1)
print("New date in DD-MM-YYYY Format: ",change_date_format(dt1))

output:
Original date in YYY-MM-DD Format:  2026-01-02
New date in DD-MM-YYYY Format:  02-01-2026'''







