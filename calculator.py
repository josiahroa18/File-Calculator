# Josiah Roa
# 102
# calculator.py
# This homework is to let us get practice with opening, reading, and closing files. It also
# allows us to get used to iterating through a file and using the information to perform
# different actions


# This function is the main menu function taking in no arguments
# It returns the value that the user has entered and only accepts
# values in the range 1-6
def main_menu():
    print('1: count lines')
    print('2: add numbers')
    print('3: subtract numbers')
    print('4: average numbers')
    print('5: minimum')
    print('6: maximum')
    print('0: exit')
    while True:
        answer = input('> ')
        for i in '0123456':
            if answer == i:
                return answer
        else:
            continue


# This function counts the lines in the file taking the file as a parameter.
# It returns the amount of times it iterates through a file
def count_lines(file):
    lines = 0
    for l in file:
        lines += 1
    return lines


# This function adds or subtracts the numbers in the file
# It takes in one parameter, add which is a boolean statement pass from main
# If add is True, it will add contents of the file and return the value, if add is False, it will
# subtract contents of file, and print it directly
def math_operation(file, add):
    sum_numbers = 0
    for line in file:
        line_int = int(line)
        sum_numbers += line_int
    if add:
        return sum_numbers
    else:
        print('Result: -' + str(sum_numbers))
        print(' ')


# This function will find the min or the max value of the file
# It takes two parameters, the file, and a boolean value for min_
# If min is True, it will return the min value
# If min is False, it will return the max value
def find_value(file, min_):
    min_value = 0
    max_value = 0
    for line in file:
        line_int = int(line)
        # if line_int is less than min
        if line_int < min_value:
            min_value = line_int
        # if line_int is bigger than num, create new max
        if line_int > max_value:
            max_value = line_int
    if min_:
        return min_value
    else:
        return max_value


# This is the main function
def main():
    file = input('File? ')
    menu = True
    # While this is true, the program will keep asking for user input and performing actions
    # based off of their input
    while menu:
        in_file = open(file, 'r')
        process = main_menu()
        # Count Lines
        if process == '1':
            lines = count_lines(in_file)
            print('Result: ' + str(lines) + '\n')
            in_file.close()
        # Add
        elif process == '2':
            added_numbers = math_operation(in_file, True)
            print('Result: ' + str(added_numbers) + '\n')
            in_file.close()
        # Subtract
        elif process == '3':
            math_operation(in_file, False)
            in_file.close()
        # Average
        # this conditional statement uses the count_lines function and math_operation function
        # to get the average value of the contents of the file
        elif process == '4':
            sum_numbers = math_operation(in_file, True)
            in_file.close()
            # We need to re-open the file in order to perform the count_lines function again
            in_file = open(file, 'r')
            lines = count_lines(in_file)
            in_file.close()
            average = round(float(sum_numbers / lines), 2)
            print('Result: ' + str(average))
            print(' ')
        # Minimum
        elif process == '5':
            min_number = find_value(in_file, True)
            in_file.close()
            print("Result: " + str(min_number))
            print(' ')
        # Maximum
        elif process == '6':
            max_number = find_value(in_file, False)
            in_file.close()
            print('Result: ' + str(max_number))
            print(' ')
        # Break out of loop and end program
        elif process == '0':
            in_file.close()
            break


if __name__ == '__main__':
    main()
