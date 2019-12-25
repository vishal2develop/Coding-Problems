#for input use:
input_list = "-2,1,3,-4,5"
input_list = input_list.split(",")
input_list = [int(i) for i in input_list]

a = 0
b = 0
for i in input_list:
    new_b = b if b > a else a # 0,0,1
    a = b + i # -2,1,3
    b = new_b # 0,0,1
    print(a,b,new_b)
    print("***********")
print(b if b > a else a)
