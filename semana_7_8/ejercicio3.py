'''
Given a number N, a sequence of N natural numbers must be read and the
store in an array. The program must produce a sequence with the Fibonacci number
of each of the numbers in the entry. Use the same scheme as the previous question: a
applet for reading the sequence, another for producing the Fibonacci numbers in a
second arrangement and another that takes this second arrangement and prints it on the screen. Suggestion:
write a function that, given a natural number i, produces the Fibonacci number fib(i) of said number
worth.
'''


def read_sequence(N, sequence):
    if len(sequence) != N:
        raise ValueError("Length of the input sequence must be equal to N")
    return sequence

def fibonacci(n):
    if n < 0:
        raise ValueError("Input must be a natural number")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


def produce_fibonacci_sequence(sequence):
    return [fibonacci(num) for num in sequence]


def print_sequence(sequence):
    for num in sequence:
        print(num)


##################### testing

def test_read_sequence():
    assert read_sequence(3, [1, 2, 3]) == [1, 2, 3]
    try:
        read_sequence(3, [1, 2])
    except ValueError as e:
        assert str(e) == "Length of the input sequence must be equal to N"

def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(10) == 55

def test_produce_fibonacci_sequence():
    assert produce_fibonacci_sequence([0, 1, 2, 3, 4, 5]) == [0, 1, 1, 2, 3, 5]
    assert produce_fibonacci_sequence([6, 7, 8, 9, 10]) == [8, 13, 21, 34, 55]

def test_print_sequence():
    import io
    import sys
    captured_output = io.StringIO()
    sys.stdout = captured_output
    print_sequence([0, 1, 1, 2, 3, 5])
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue() == "0\n1\n1\n2\n3\n5\n"

# Running the tests
test_read_sequence()
test_fibonacci()
test_produce_fibonacci_sequence()
test_print_sequence()

print("All tests passed!")
