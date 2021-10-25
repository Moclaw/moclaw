from numpy import random

# tìm kiếm tuyến tính
def linear_search(array_search,key):
    print("Tìm kiếm tuyến tính")
    for i in range(len(array_search)): 
    	if array_search[i] == key:
        	print("Vị trí cần tìm là: ",i+1)    
print("----------------------------------")
    
# tìm kiếm nhị phân
def binary_search(array_search2,key2):
    left=0
    right= len(array_search2)
    mid=0
    i=0
    while (left<=right):
        i=i+1
        mid=(left+right)//2
        if key2==array_search2[mid]:
            print("Vị trí",mid)
        if key2<array_search2[mid]:
            right= mid-1
        else:
            left= mid+1
    print("Không có")
if __name__ == '__main__':
	array_need_search = random.randint(100, size=(10))
	print("Cho mảng ngâu nhiên: ",array_need_search)
	try:
		key_search = int(input("Nhập số cần tìm: "))
		linear_search(array_need_search,key_search)
		binary_search(array_need_search,key_search)
	except:
		print("Try Again!!")