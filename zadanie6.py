def ciag(a, b, ile):

    elementy=[]
    an=1*b
    elementy.append(a)
    elementy.append(an)
    iloczyn_elementow= a*an
    for i in range (2,ile+1,1):
        x= an*b
        elementy.insert(i,x)
        an=x
        iloczyn_elementow *= x

        return iloczyn_elementow, elementy



a=1
b=4
ile=10
print(ciag(a,b,ile))

