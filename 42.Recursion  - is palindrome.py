# recursion from Lynda.com
def isPalindrome(s):
    # return if string s is a Palindrome
    if len(s) <= 1:   # base case
        return True
    else:
        return s[0] == s[-1] and isPalindrome(s[1:-1])

s = "h"
print(s, isPalindrome(s))
s = "mum"
print(s, isPalindrome(s))
s = "apple"
print(s, isPalindrome(s))
    