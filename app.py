def draw_diamond(n):
    # Upper pyramid
    for i in range(1, n + 1, 2):
        print(" " * ((n - i) // 2) + "*" * i)
    
    # Lower inverted pyramid
    for i in range(n - 2, 0, -2):
        print(" " * ((n - i) // 2) + "*" * i)

# Call function
draw_diamond(9)