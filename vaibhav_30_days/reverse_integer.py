def reverse_integer(x: int) -> int:

    max_allow = 2 ** 31 - 1
    min_allow = -2 ** 31
    negative = bool()

    result = []
    res_int = 0
    if x < 0:
        x = abs(x)
        negative = True

    while abs(x)//10 > 0:

        remainder = x % 10
        x = x//10
        result.append(remainder)

    result.append(x)

    for num in result:
        res_int = res_int*10 + num

    if res_int < min_allow:
        return 0
    if res_int > max_allow:
        return 0

    if negative:
        res_int = -res_int

    return res_int


print(reverse_integer(-123))



