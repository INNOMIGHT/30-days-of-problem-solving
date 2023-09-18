def roman_to_numeral(s: str) -> int:

    result = 0
    roman_numerals = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    for i in range(len(s)):
        if i < len(s) - 1 and roman_numerals[s[i]] < roman_numerals[s[i+1]]:
            result -= roman_numerals[s[i]]
        else:
            result += roman_numerals[s[i]]

    return result


print(roman_to_numeral("CM"))
