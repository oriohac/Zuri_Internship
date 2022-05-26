
from operator import truediv


is_nighttime = True
houroftheday = 0
while is_nighttime:
    if houroftheday == 10:
        print("wake up!")
        break
    #keep sleeping
    houroftheday =houroftheday + 1
    print(houroftheday)

    
