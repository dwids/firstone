# recursion from Lynda.com
def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last = n // 10     # integer division , returns int
        last = n % 10               # mod 10
        return sum_digits(all_but_last) + last

print(7, sum_digits(7))
print(15, sum_digits(15))
print(279,sum_digits(279))
print(1248, sum_digits(1248))
