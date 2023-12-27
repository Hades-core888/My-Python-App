def main():
    n = int(input('Please insert amount of the list: '))
    List = []
    for i in range (n):
        List.append(int(input('[ '+str(i)+' ]: ')))
    class Sort ():
        def funcion_1 (): #sort list ascending.
            print('The list after short:')
            List.sort(reverse = False)
            for i in range(len(List)):
                print('[ '+str(i)+' ]: ',List[i])
        def funcion_2 (): #sort list decending.
            print('The list after short:')
            List.sort(reverse = True)
            for i in range(len(List)):
                print('[ '+str(i)+' ]: ',List[i])
    class Action ():
        def funcion_3 (): #Information of list and max min value.
            print('amount of the list:'+ str(len(List)))
            print('Max value: '+ str(max(List)))
            print('Min value: '+ str(min(List)))
        def funcion_4 ():
            x = int(input('Insert element to delete: '))
            List.remove(x)
            print('Element has been deleted ! \n')
            for i in List:
                print('[ '+ str(i)+' ]:',i)
    print('1: sort list ascending')
    print('2: sort list decending')
    print('3: show information of the list')
    print('4: remove element of the list')
    sec = int(input('Insert your command: '))
    match sec:
        case 1:
            Sort.funcion_1()
        case 2:
            Sort.funcion_2()
        case 3:
            Action.funcion_3()
        case 4:
            Action.funcion_4()    
main()
