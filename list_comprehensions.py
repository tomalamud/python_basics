def run():
    # WITHOUT COMPREHENSIONS
    # squares = []
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         squares.append(i**2)
    
    # WITH COMPREHENSIONS
    # [element for element in iterable if condition]
    # [i for i in range(1, 100000) if i % 36 == 0]
    squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    
    print(squares)



if __name__ == '__main__':
    run()