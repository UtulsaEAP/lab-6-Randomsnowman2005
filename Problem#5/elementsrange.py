# Mohamad Ali fakhoury @ Thurs @ 2pm
def filter_and_print_range(input_list, min_val, max_val):
      for num in input_list:
        if min_val <= num <= max_val:
            print(num, end=",")

        

if __name__ == '__main__':
    user_input = input("Enter a space-separated string of numbers: ")
    integer_list = [int(a) for a in user_input.split()]
    user_input = input("Enter the min and max values separated by a space: ")
    min_val, max_val = map(int, user_input.split())
    filter_and_print_range(integer_list, min_val, max_val)

   
