def swapfile():
    file1 = input("enter the first file name")
    file2 = input("enter the second file name")
    with open(file1,'r')as a:
        data1 = a.read()
    with open(file2,'r')as b:
        data2 = b.read()
    with open(file1,'w')as a:
        a.write(data2)
    with open(file2,'w')as b:
        b.write(data1)
swapfile() 
