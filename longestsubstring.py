#Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
#In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
#Longest substring in alphabetical order is: abc


s = 'abcbcd'
longest = ''

for i in range(0, len(s)):
    string = s[i]
    key = i
    while key + 1 < len(s) and ord(s[key]) <= ord(s[key+1]):
        string += s[key+1]
        key += 1
    if len(string) > len(longest):
        longest = string

print("Longest substring in alphabetical order is: ", longest)
