# Learning python if-else
def main():
    a = int(input('Insert A: '))
    b = int(input('Insert B: '))
    print('Show the compairation')
    print ('a > b') if (a > b) else print('a = b') if (a == b) else print('a < b')
    x = int(input('Want to continue ? \n Yes press 1 \t No press 0 \n Answer: '))
    match x:
        case 1:
            main()
        case 0: 
            print('\tProgram End\t')
main()