def find_all_index(arr,item):
    return [i for i,a in enumerate(arr) if a==item]
list=[1,2,3,3,4,4,5,6]
print(find_all_index(list,3))