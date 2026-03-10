#  while Loop with User Input

if __name__ == '__main__':
        
    num = int(input("Enter a number to multiply by 5 (0 to stop): "))
    while num != 0:
        print(f"{num} multiply by 5: {num*5}")
        num = int(input("Enter a number to multiply by 5 (0 to stop): "))
    
    print("Good Bye.")