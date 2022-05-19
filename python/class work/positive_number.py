user_no = input("enter a number: ")

try:
        user_no = float(user_no)
        print("hooray, you entered a number")
        if user_no >= 0:
          print("true")
        else:
            print("false")
except:
       print("this is not a number")