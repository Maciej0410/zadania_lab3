def ciag2(*elementy):
    if(len.elementy !=0):
        iloczyn = 1

        for i in range(len.elementy):
            iloczyn *= elementy
        return iloczyn
    else:
        return 0


elementy=[1,2,3,4,5,6,7,8,9,10]

print(ciag2(elementy))