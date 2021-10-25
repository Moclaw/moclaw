import numpy as np
#Áp dụng thuật toán nổi bọt bubble sort
def bubble_sort(arr):
	for i in range(0,len(arr) - 1):
		for j in range(i+1,len(arr)):
			if arr[i] > arr[j]:
				tmp = arr[i]
				arr[i] = arr[j]
				arr[j] = tmp
	return arr
#Áp dụng thuật toán sắp xép chèn - insertion sort
def insertion_sort(arr2):
    for i in range(1, len(arr2)):
        key = arr2[i]
        j = i-1
        while j >= 0 and key < arr2[j] :
                arr2[j + 1] = arr2[j]
                j -= 1
        arr2[j + 1] = key
        return arr2
 #Áp dụng thuật toán sắp xép chọn - selection sort   
def selection_sort(arr3):
	for i in range(len(arr3)):
		min_idx = i
		for j in range(i+1, len(arr3)):
			if arr3[min_idx] > arr3[j]:
				min_idx = j       
				arr3[i], arr3[min_idx] = arr3[min_idx], arr3[i]
	return arr3
if __name__ == '__main__':	
	arr_need_sort_ex1 = np.random.randint(1,10,5)
	print("\nCho mảng ngẫu nhiên cần sắp xếp: ",arr_need_sort_ex1)
	arr_need_sort_ex2 = np.random.randint(1,10,7)
	print("Cho mảng ngẫu nhiên cần sắp xếp: ",arr_need_sort_ex2,"\n")
	print("Thuật toán bubble sort: \n")
	print("bai 1:")
	print(bubble_sort(arr_need_sort_ex1))
	print("---------------------------------")
	print("bai 2:")
	print(bubble_sort(arr_need_sort_ex2))
	print("---------------------------------")
	print("Thuật toán insertion sort: \n")
	print("bai 1:")
	print(insertion_sort(arr_need_sort_ex1))
	print("---------------------------------")
	print("bai 2:")
	print(insertion_sort(arr_need_sort_ex2))
	print("---------------------------------")	
	print("Thuật toán selection sort: \n")
	print("bai 1:")
	print(selection_sort(arr_need_sort_ex1))
	print("---------------------------------")
	print("bai 2:")
	print(selection_sort(arr_need_sort_ex2))