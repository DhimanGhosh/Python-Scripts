import List

if __name__=='__main__':
    a1=[6,3,8,1,7]
    a2=[5,2,9,4]
    l1=List(a1)
    l1.append(0)
    l1.extend(a2)
    print(l1.get_a())
    
