# Mohamad Ali fakhoury @ Thurs 2pm
def process_and_print(input_string):

    inputs = input_string.split()
    input_data = [int(token) for token in inputs]
    # Filter out negative values
    input_data = [num for num in input_data if num < 0]
    # Sort integers in reverse order
    input_data.sort(reverse=True)
    # Print sorted integers
    x=0
    output_string = ''
    for x in range(len(input_data)):
        output_string = output_string + str(input_data[x]) + ' '
    print(output_string)

 

if __name__ == "__main__":

    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")
    # Call the function to process and print the result
    process_and_print(user_input)


    

