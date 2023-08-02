import sys

def main(): 
    arguments = sys.argv[1:]    
    num_arguments = len(arguments)
    print(f"{num_arguments}", end='')
    print(" argument" if num_arguments == 1 else " arguments", end='')   
    print(":" if num_arguments > 0 else ".")

    for index, argument in enumerate(arguments, start=1):
        print(f"{index}: {argument}")

if __name__ == "__main__":
    main()
