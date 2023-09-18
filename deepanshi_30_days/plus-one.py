def plusOne(digits):
    for i in range(len(digits)):
        digits[i] = str(digits[i])
            
    digit_str = "".join(digits)
    digit_num = int(digit_str)
    plus_one_digit = str(digit_num + 1)
    res = []
    for i in range(len(plus_one_digit)):
        res.append(int(plus_one_digit[i]))

    return res
        
        