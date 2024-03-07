# Mohamad Ali fakhoury @ Thurs 2pm
def process_and_print(input_string):
    inputs = input_string.split()
    x = 0
    while x < len(inputs):
     z = int(inputs[x])
     inputs[x] = z
     x = x+1 
    else:
     inputs.sort(reverse = True)
     x= 0
     fin = []
     while x < len(inputs):
        if x == len(inputs)-1:
          if inputs[x]<0:
            fin.append(str(inputs[x]))
            x=x+1
          else:
            x=x+1
        elif inputs[x] < 0 and inputs[x+1] >= 0:
         fin.append(str(inputs[x]))
         x = x+1
         z =z+1
        elif inputs[x] < 0 and inputs[x+1]<0:
         fin.append(str(inputs[x]))
         x = x+1 
         z=z+1
        else:
          x=x+1
     else:
        final = ' '.join(fin)
        print(f'{final} ' )
        
   
    

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function to process and print the result
    process_and_print(user_input)
