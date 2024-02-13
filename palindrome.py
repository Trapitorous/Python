def ispalindrome(string):
     if(string==string[::-1]):
         return"The string is palindrome"
string=input("Enter string")
print(ispalindrome(string))


def isPalindrome(string):
    string=string.lower().replace('','')
    first,last=0,len(string)-1
    while(first<last):
        if(string[first]==string[last]):
            first+=1
            last-=1
        else:
            return"The string is not a palindrome"
        return"The string is a palindrome"
str1=input("Enter string")
print(isPalindrome(str1))