#Mohamad Ali fakhoury @Thurs 2pm
def process_input(input_string):
  inputs = input_string.split()
  x = 0
  while x < len(inputs):
     z = float(inputs[x])
     inputs[x] = z
     x = x+1
  else:
   inputs.sort(reverse = True)
   max_value = inputs[0]
   dem = 0
   for x in range(len(inputs)):
    dem =  dem + inputs[x]
   average_value = dem/len(inputs)
   return max_value, average_value

if __name__ == "__main__":
    user_input = input("Enter a space-separated string of numbers: ")

    max_value, average_value = process_input(user_input)

    print(f'Max Value: {max_value:.2f}')
    print(f'Average Value: {average_value:.2f}')
