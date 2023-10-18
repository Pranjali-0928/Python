#read
# file1 = open("file_1.txt" ,"rt")
# print(file1.read())
# file1.close()
# print(file1.closed)
with( open('file_1.txt',"r") as file1):
    #  print(file1.readlines())
     list1 = []
     for i in file1:
         list1.append(i.strip())
print(list1)