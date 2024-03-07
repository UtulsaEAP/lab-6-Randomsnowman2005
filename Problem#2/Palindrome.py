# Mohamad Ali Fakhoury Thurs@2pm
def check_palindrome(user_input):
    inputs = [user_input]
    z=0
    outputs = []
    z = len(inputs[0])
    final = ''
    while z> 0:
     word = inputs[0]
     let = word[z-1]
     final = final + let
     z = z -1
    else:
     outputs.insert(0,final)
     if inputs == outputs:
        print(f"palindrome: {user_input}")
     else:
        print(f"not a palindrome: {user_input}")
 
 
if __name__ == "__main__":
    user_input = str(input())
    check_palindrome(user_input)
