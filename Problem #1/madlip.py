# Mohamad Ali Fakhoury Thurs @ 2pm
def food_input():
    tokens = []
    qu = ['quit','0']
    while tokens != qu:
        user_input = input()
        tokens = user_input.split()
        if tokens == qu:
            pass
        else:
         print(f'Eating {tokens[1]} {tokens[0]} a day keeps you happy and healthy.')


    

if __name__ == "__main__":
    food_input()
