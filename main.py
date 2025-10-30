for i in range(100, 0, -1):
    s = str(i)
    count = s.count("3")
    
    if count > 0:
        print("짝" * count)
    else:
        print(i)
