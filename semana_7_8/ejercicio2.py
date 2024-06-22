'''
Habiamos resuelto lo siguiente:
Determinar si una secuencia de enteros está ordenada en forma creciente o
decreciente, o está en desorden. Escriba un subprograma para la lectura de los elementos de la
secuencia que lo realice hasta un número N especificado por el usuario. No se admite la
secuencia vacía ni unitaria. Luego realice otro subprograma que tome la secuencia y vea el tipo
de ordenamiento. Finalice con un subprograma que muestre en pantalla el resultado. El programa
principal debe llamar a estos tres subprogramas. 

'''

# de esta manera:
def read_sequence(n):
    """
    Reads a sequence of n integers from the user.
    Preconditions: n > 1
    """
    if n <= 1:
        raise ValueError("The sequence must have more than one element.")
    
    sequence = []
    print(f"Enter {n} integers:")
    for i in range(n):
        while True:
            try:
                number = int(input(f"Element {i+1}: "))
                sequence.append(number)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")
    return sequence

def determine_order(sequence):
    """
    Determines if the sequence is increasing, decreasing, or unordered.
    """
    is_increasing = all(sequence[i] <= sequence[i + 1] for i in range(len(sequence) - 1))
    is_decreasing = all(sequence[i] >= sequence[i + 1] for i in range(len(sequence) - 1))
    
    if is_increasing:
        return "increasing"
    elif is_decreasing:
        return "decreasing"
    else:
        return "unordered"

def display_result(result):
    """
    Displays the result of the order check.
    """
    print(f"The sequence is {result}.")

def main():
    """
    Main function to coordinate the applets.
    """
    try:
        n = int(input("Enter the number of elements in the sequence: "))
        if n <= 1:
            raise ValueError
        
        sequence = read_sequence(n)
        result = determine_order(sequence)
        display_result(result)
    except ValueError:
        print("Invalid input. The number of elements must be an integer greater than 1.")

if __name__ == "__main__":
    main()


'''
Para hacer tests sobre esto:
'''
def test_read_sequence():
    from io import StringIO
    import sys
    
    input_values = ['5', '1', '2', '3', '4', '5']
    output = []

    def mock_input(s):
        output.append(s)
        return input_values.pop(0)

    sys.stdin = StringIO("\n".join(input_values))
    input_func = input
    try:
        input = mock_input
        sequence = read_sequence(5)
        assert sequence == [1, 2, 3, 4, 5]
    finally:
        input = input_func

def test_determine_order():
    assert determine_order([1, 2, 3, 4, 5]) == "increasing"
    assert determine_order([5, 4, 3, 2, 1]) == "decreasing"
    assert determine_order([1, 3, 2, 4, 5]) == "unordered"

def test_display_result():
    from io import StringIO
    import sys
    
    output = StringIO()
    sys.stdout = output
    
    display_result("increasing")
    assert output.getvalue().strip() == "The sequence is increasing."
    
    display_result("decreasing")
    assert output.getvalue().strip() == "The sequence is decreasing."
    
    display_result("unordered")
    assert output.getvalue().strip() == "The sequence is unordered."

    sys.stdout = sys.__stdout__

def run_tests():
    test_read_sequence()
    test_determine_order()
    test_display_result()
    print("All tests passed.")

if __name__ == "__main__":
    run_tests()

