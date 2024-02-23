from typing import List


def letterCombinations(digits: str) -> List[str]:
        mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        output = []

        def extract(index: int, acc: str):
            if len(digits) == index:
                output.append(acc)
                return

            for char in mapping[digits[index]]:
                extract(index + 1, acc + char)

        if digits:
            extract(0, '')

        return output


if __name__ == '__main__':
    assert ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'] == letterCombinations('23')
    assert [] == letterCombinations('')
    assert ['a', 'b', 'c'] == letterCombinations('2')
