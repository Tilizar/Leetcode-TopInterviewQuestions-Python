from typing import List


def fizzBuzz(n: int) -> List[str]:
    output = []

    for i in range(1, n + 1):
        if i % 15 == 0:
            output.append('FizzBuzz')
        elif i % 5 == 0:
            output.append('Buzz')
        elif i % 3 == 0:
            output.append('Fizz')
        else:
            output.append(str(i))

    return output


if __name__ == '__main__':
    assert ['1', '2', 'Fizz'] == fizzBuzz(3)
    assert ['1', '2', 'Fizz', '4', 'Buzz'] == fizzBuzz(5)
    expected = ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
    assert expected == fizzBuzz(15)
