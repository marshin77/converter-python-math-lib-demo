import math

## radius to circumference and area
def circlethings ():
    
    r = int(input("input radius here: "))
    pi = math.pi
    c = 2 * pi  * r
    print ("the circumference is:",c)
    a = math.pi  * r ** 2
    print ("the area is:", a)

## turns input into rectangle volume    
def rectvolume ():
    L=int(input("input length here:"))
    w=int(input("input with here:"))
    h=int(input("input height here:"))
    v = L*w*h
    print("the volume is",v)
## converts tempatures from fahrenheit to celsius and kalvin
def temp ():
    temp=int(input("input degrees fahrenheit: "))
    cel = (temp - 32)*5/9       
    print("celsius: ",cel)
    kel = (temp+459.67)*5/9
    print("kalvin: ",kel)

## takes two input numbers and divides them.
def aB ():
    a = int(input("number A: "))
    b = int(input("number B: "))
    print("quotent of a by b: ",a//b)
    print("remainder of a by b: ",a%b)
    print("quotent of b by a: ",b//a)
    print("remainder of b by a: ",b%a)

def main():
    circlethings()
    rectvolume()
    temp()
    aB()

main()
    
