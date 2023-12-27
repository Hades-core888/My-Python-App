from math import fabs, sqrt
def Function_1 (a,b,c): #Ham giai pt bac 1
    if   (a != 0 ):
        if  ( b == 0):
            print("Phuong trinh co nghiem:" + str(float(  c/a    )))
        else:
            print("Phuong trinh co nghiem:" + str(float( (c-b)/a )))
    elif ( a == 0 ):
        if  ( b == 0):
            print("Phuong trinh vo so nghiem")
        else:
            print("Phuong trinh vo nghiem")
def Function_2 (a,b,c): #Ham giai pt bac 2
    Delta = float((pow(b,2)-4*a*c))
    if   ( a + b + c == 0):
        print ("Phuong trinh co nghiem:" + " 1 va "+  str(float( c/a)))
    elif ( a - b + c == 0):
        print ("Phuong trinh co nghiem:" + "-1 va "+  str(float(-c/a)))
    elif  ( Delta >  0 ):
        print("Phuong trinh co nghiem:" + str(float( (-b+sqrt(Delta))/(2*a) ))+ " va " + str(float( (-b-sqrt(Delta))/(2*a) )))
    elif  ( Delta == 0 ):
        print("Phuong trinh co hai nghiem kep:"+ str(float(-b/2*a)))    
    else:
        m = str(float( (-b)/(2*a) ))
        n = str(float( sqrt(fabs(Delta))/(2*a) ))    
        print("Phuong trinh co nghiem phuc:" +m+ "+" +n+ "i") 
        print("Phuong trinh co nghiem phuc:" +m+ "-" +n+ "i") 
def main():
    print('Nhap phuong trinh can giai: ')
    print('1: Bac 1 \t 2: Bac hai')
    x = int(input('Nhap lua chon: '))
    match x: 
        case 1: 
            a = int(input('A: '))
            b = int(input('B: '))
            c = int(input('C: '))
            Function_1(a,b,c)
        case 2:
            a = int(input('A: '))
            b = int(input('B: '))
            c = int(input('C: '))
            Function_2(a,b,c)
    print('Continue ? Y/N: ')
    i = input('Anwser: ')
    match i:
        case 'y':
            main()
        case 'n':
            pass    
main()
