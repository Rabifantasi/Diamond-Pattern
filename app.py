def draw_diamond(n):
  
    for i in range(1, n + 1, 2):
        print(" " * ((n - i) // 2) + "*" * i)
    
    for i in range(n - 2, 0, -2):
        print(" " * ((n - i) // 2) + "*" * i)

draw_diamond(9)
