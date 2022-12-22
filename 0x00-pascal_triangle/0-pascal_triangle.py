#!/usr/bin/python3

"""
0x00. Pascal's Triangle
this task is a part of the alx-interview preparation
"""

def pascal_triangle(n):
    
    """
    args:
        n -> int
             
    description:
        this returns a triangle of height (n+1) and base width of (n+1)
        this is a programmatc implementation of the Pascal triangle in ```Binomial expansion```
    """

    result = []

    if n < 0:
        return result

    elif n >= 0:
        for i in range(n+1):
            if i == 0:
                result.append([1])
            elif i == 1:
                result.append([1, 1])
            else:
                temp = []
                temp.append(1)
                for j in range(len(result[-1]) - 1):
                    #print(result[-1][j], result[-1][j+1])
                    temp.append(result[-1][j] + result[-1][j+1])
                temp.append(1)
                result.append(temp)
    return result



def main():
    #n = int(input("enter value for n\n>>"))
    n = 6
    print([row for row in pascal_triangle(n)])


if __name__ == "__main__":
    main()