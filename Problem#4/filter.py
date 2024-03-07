# Mohamad Ali fakhoury @ Thurs 2pm
def process_and_print(input_string):

 tokens = input_string.split()
 input_data = []
 for token in tokens:
    if int(token) < 0:
        input_data.append(int(token))
 input_data.sort(reverse=True)
 for values in input_data:
    print(values, end=' ')


if __name__ == "__main__": # User inputs string w/ numbers
 user_input = input("Enter a space-separated string of numbers: ") # Call the function to process and print the result
 process_and_print(user_input)


    

