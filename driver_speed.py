def driver_speed(speed):
    a = speed // 5
    if speed > 70:
        if a > 12:
            return "license is suspended"
        else:
            return "speed is more than 70"
    else:
        return "speed is less than 70 "
speed = int(input("enter no"))
print(driver_speed(speed))
