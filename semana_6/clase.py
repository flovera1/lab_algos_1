'''
Determinar si una secuencia de enteros está 
ordenada en forma creciente o
decreciente, o está en desorden. Escriba un 
subprograma para la lectura de los elementos de la
secuencia que lo realice hasta un número N 
especificado por el usuario. No se admite la
secuencia vacía ni unitaria. Luego realice otro 
subprograma que tome la secuencia y vea el tipo
de ordenamiento. Finalice con un subprograma 
que muestre en pantalla el resultado. El programa
principal debe llamar a estos tres subprogramas. 
'''
'''
To accomplish this task, we'll break it down 
into three main functions, each corresponding
 to the "applets" described:

    Reading the sequence: This function will
    	 read a sequence of integers from the 
    	 user up to a number NN specified by 
    	 the user.
    Checking the ordering: This function will 
    	take the sequence and determine if it 
    	is in increasing order, decreasing order, 
    	or unordered.
    Displaying the result: This function will 
    	display the result of the ordering check.

Finally, we'll create a main function to call 
these three functions in order.

Here's the complete Python program with 
explanations:
'''
def read_sequence():
    """
    Reads a sequence of integers from the 
    user up to a specified number N.
    Returns the sequence as a list of integers.
    """
    while True:
        try:
            N = int(input("Enter the number of elements in the sequence (N > 1): "))
            if N <= 1:
                raise ValueError("N must be greater than 1")
            break
        except ValueError as e:
            print(e)
    
    sequence = []
    print(f"Enter {N} integers:")
    for _ in range(N):
        while True:
            try:
                num = int(input())
                sequence.append(num)
                break
            except ValueError:
                print("Please enter a valid integer.")
    
    return sequence

def check_order(sequence):
    """
    Checks the order of the given sequence.
    Returns 'increasing' if the sequence is in 
    increasing order,
    'decreasing' if the sequence is in decreasing 
    order, or 'disorder' otherwise.
    """
    is_increasing = all(sequence[i] <= sequence[i + 1] for i in range(len(sequence) - 1))
    is_decreasing = all(sequence[i] >= sequence[i + 1] for i in range(len(sequence) - 1))
    
    if is_increasing:
        return "increasing"
    elif is_decreasing:
        return "decreasing"
    else:
        return "disorder"

def display_result(order):
    """
    Displays the result of the order check.
    """
    print(f"The sequence is {order}.")

def main():
    """
    Main function to call the read_sequence, check_order, and display_result functions.
    """
    sequence = read_sequence()
    order = check_order(sequence)
    display_result(order)

# Call the main function to execute the program
if __name__ == "__main__":
    main()


'''
Explanation:

    read_sequence():
        Prompts the user to enter the number of elements in the sequence (NN).
        Validates that NN is greater than 1 (as empty or unitary sequences are not supported).
        Reads NN integers from the user and stores them in a list.
        Returns the list of integers.

    check_order(sequence):
        Checks if all elements in the sequence are in increasing order using a generator expression.
        Checks if all elements in the sequence are in decreasing order using another generator expression.
        Returns 'increasing', 'decreasing', or 'disorder' based on the checks.

    display_result(order):
        Takes the result of the order check and prints it to the screen.

    main():
        Calls the read_sequence function to get the sequence from the user.
        Calls the check_order function to determine the order of the sequence.
        Calls the display_result function to print the result.

The if __name__ == "__main__": block ensures that the main function is called only when the script is run directly, not when it is imported as a module in another script.
'''
