def find_all_index(arr,item):
    return [i for i,a in enumerate(arr) if a==item]


list=['138','123','123123','123','123','123']
set_l=set(list)

for i in set_l:
    a=find_all_index(list,i)
    print(i+"有"+str(len(a))+"个")
