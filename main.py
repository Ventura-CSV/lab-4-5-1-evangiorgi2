import random


def main():
   
    total = 0
    numbers = []
    while i < 5:
        numbers = random.radint(0, 100)
        total = sum(numbers)
        i += 1
    
    
    print(f'The random values are {numbers}')
    print(f'The total is {total}')


    return numbers, total


if __name__ == '__main__':
    main()
