def isPalindrome( x):
    if x < 0:
        return False
    elif  x == 0:
        return True
    digit = x
    res = ""
    while digit > 0:
        res = res + str(digit % 10)
        digit = digit // 10
       
    if int(res) == x:
        return True
    else:
        False