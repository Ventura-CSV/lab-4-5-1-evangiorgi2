import random


def main():
   
    total = 0
    i = 0
    numbers = []
    while i < 5:
        numbers = random.randint(0, 100)
        total = total + numbers[i]
        i += 1
    
    
    print(f'The random values are {numbers}')
    print(f'The total is {total}')


    return numbers, total


if __name__ == '__main__':
    main()
