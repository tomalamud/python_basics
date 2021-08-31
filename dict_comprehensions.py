import math

def run():
    # WITHOUT COMPREHENSIONS
    # my_dict = {}
    # for i in range(1, 101):
    #     my_dict[i] = i**3

    my_dict = {i: math.sqrt(i) for i in range(1, 101) if i % 3 != 0}
    print(my_dict)

if __name__ == '__main__':
    run()