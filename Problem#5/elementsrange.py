# Mohamad Ali fakhoury @ Thurs @ 2pm
def filter_and_print_range(input_list, min_val, max_val):
    x=0
    fin = ''
    while x < len(input_list):
     z = int(input_list[x])
     input_list[x] = z
     x = x+1 
    else:
     x=-1
     while x < len(input_list)-1:
      if input_list[x+1]>=int(min_val) and input_list[x+1]<=int(max_val):
        fin= fin+(str(input_list[x+1]))+','
        x=x+1
      else:
        x=x+1
     else:
       print(fin)

        

if __name__ == '__main__':
    # Get input for the list of integers
    user_input = input("Enter a space-separated string of numbers: ")
    integer_list = user_input.split()

    # Get input for the range (min and max values)
    user_input = input("Enter the min and max values separated by a space: ")
    min_val, max_val = user_input.split()
    filter_and_print_range(integer_list,min_val,max_val)

    # Call the function to filter and print the numbers in the given range
   
