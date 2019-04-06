def can_devide(number,power,divisor):
    yu = number % divisor
    if yu == 0:
        power = power + 1
        return can_devide(number/divisor,power,divisor)
    else:
        return power,number


def sys_main(number):
    ori = number
    if number.isdigit():
        number = int(number)
        list_power = []
        for divisor in[2,3,5]:
            power_divisor, number = can_devide(number,power=0,divisor=divisor)
            list_power.append(power_divisor)
        if number == 1:
            print(ori,'is a simple number',ori,'= 2^',list_power[0],'+3^',list_power[1],'+5^',list_power[2])
        else:
            print(ori,'is not a simple number')
    else:
        print("not a digit number,please restart")

print("please enter a number:")
x = input()
while x != 'stop':
    sys_main(x)
    print("please enter a number(or stop to exit):")
    x = input()