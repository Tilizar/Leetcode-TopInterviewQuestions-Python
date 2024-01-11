def romanToInt(s: str) -> int:
        mapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        output = 0

        for index, roman in enumerate(s):
            if index + 1 < len(s) and mapping[roman] < mapping[s[index + 1]]:
                output -= mapping[roman]
            else:
                output += mapping[roman]

        return output


if __name__ == '__main__':
    assert 3 == romanToInt("III")
    assert 58 == romanToInt("LVIII")
    assert 1994 == romanToInt("MCMXCIV")
