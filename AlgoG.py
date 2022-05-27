import time

def ordenar_g(lista,f,c,L):
    lista_a = lista
    pivot = pivote(lista)
    block = -1
    M =0

    while(orden(lista)==False):
        print(pivot)
        if (block!=0):
            if ((pivot//f)==(pivot+1)//f):
                print("g1")
                lista_a=swap(lista_a,pivot,pivot+1)
                if (M<concor(lista_a)):
                    print("g1")
                    M = concor(lista_a)
                    lista = lista_a
                    print(lista)
                print(lista)
                lista_a = swap(lista_a,pivot,pivot+1)     
                print(lista)
                
                

        if (block!=1):
            if ((pivot+c)<L):
                print("g2")
                lista_a=swap(lista_a,pivot,pivot+c)
                if (M<concor(lista_a)):
                    print("g2")
                    M = concor(lista_a)
                    lista = lista_a
                lista_a = swap(lista_a,pivot,pivot+c)
                

        if (block!=2):
            if ((pivot//f)==(pivot-1)//f):
                print("g3")
                lista_a=swap(lista_a,pivot,pivot-1)
                if (M<concor(lista_a)):
                    print("g3")
                    M = concor(lista_a)
                    lista = lista_a
                lista_a = swap(lista_a,pivot,pivot-1)
           
                
        if (block!=3):
            if ((pivot-c)>=0):
                print ("g4")
                lista_a=swap(lista_a,pivot,pivot-c)
                if (M<concor(lista_a)):
                    print("g4")
                    M = concor(lista_a)
                    lista = lista_a
                lista_a = swap(lista_a,pivot,pivot-c)
                
        pivot = pivote(lista)
        print(lista)
        print(orden(lista))
        time.sleep(1)

        lista_a=lista
                

     #   print(lista)


        
    print(lista)
    return lista

def pivote(lista):
    for x in range (0,len(lista)):
        if(lista[x]==len(lista)-1):
            return x
        
def orden(lista):
    if (concor(lista)== len(lista)):
        return True
    else:
        return False

def swap(Lista,pos1,pos2):

    var = Lista[pos1]
    Lista[pos1]= Lista[pos2]
    Lista[pos2] = var
    return Lista

def concor(lista):
    con = 0
    for x in range (0,len(lista)):
        if(x==lista[x]):
            con+=1

    return con

def Max (a,b):
    if (a>b):
        return a
    else:
        return b
























#ordenar_g([0,1,2,3,4,5,6,8,7],3,3,9)


#age = int(input("enter the pruve:  "))

mario = 0
print(mario+1)


















