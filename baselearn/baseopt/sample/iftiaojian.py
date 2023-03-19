while True:
    try:
        num1 = float(input("please input a number:"))
        if num1 == 0:
            print("this is 0")
        elif num1 > 0:
            print("this is zhengshu")
        else:
            print("this is fushu")
        break
    except ValueError:
        print("please input a valid number")
