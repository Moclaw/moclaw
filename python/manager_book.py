print("bài 2: ")
array=[]
num=int(input("Nhập tổng số các phần tử trong mảng: "))
for i in range(num):
	array.append(int(input("Nhập dữ liệu số: ")))
	array.sort()
print(array)
key = int(input("Nhập số người dùng muốn tìm: "))
def tuyen_tinh(array,key,n):
	i=0
	for i in range(0,n):
		if key==array[i]:
			return i,"Tìm thấy"
	return "Không tìm thấy"
n=len(array)
print('result:',tuyen_tinh(array,key,n))
print("####################################")
def binary_search(array,key):
	mid=0
	left=0
	right=len(array)
	i=0
	while(left<=right):
		i=i+1
		mid=(left+right)//2
		if key==array[mid]:
			return mid
		if key<array[mid]:
			right=mid-1
		else:
			left=mid+1
	return -1
print("Phần tử được tìm thấy tại vị trí: ",binary_search(array,key))
print("########################################################\n")
print("bài 2: ")
list_books = []
def add_books():
	print("*** THÊM SÁCH ***")
	infor = {
		'id' : '',
		'name' : '',
		'price' :''
	}
	print("Nhập mã sách kiểm tra:")
	id = int(input())

	while True:
		book = add_books(id)
		if book != False:
			print("ID này đã tồn tại, vui lòng nhập lại:")
			id = int(input())
		else:
			break

	infor['id'] = id

	print("Nhập tên sách:")
	infor['name'] = input()

	print("Nhập giá sách:")
	infor['price'] = float(input())

	list_books.append(infor)
def find_book(id):
	for i in range(0, len(list_books)):
		if list_books[i]['id'] == id:
			# Trả về mảng gồm 2 phần tử,
			# 0 là vị trí tìm thấy và 1 là dữ liệu
			return [i, list_books[i]]
	return False
def show_books():
	print("*** DANH SÁCH SÁCH HIỆN TẠI ***")
	for i in range(0, len(list_books)):
		print("[",list_books[i]['id'],"]", "[",list_books[i]['name'],"]","[",list_books[i]['price'],"]",)
#Thêm sách
n = int(input("Nhập số quyển sách cầm thêm:"))
for i in range (0,n):
	add_books()

show_books()

kt = False
x = int(input("Nhập id cuốn sách cần tìm:"))
for i in range(0, len(list_books)):
	if x == list_books[i]['id']:
		print("Cuốn sách cần tìm là:",end='')
		print("[",list_books[i]['id'],"]", "[",list_books[i]['name'],"]","[",list_books[i]['price'],"]",)
		print("Tìm kiếm tuyến tính")
		print("Ở vị trí là:",i,)
		kt = True
		break
if kt == False :
	print("Không có sách cần tìm.")

lst= []
print("-----------------")
print("Tìm kiếm nhị phân")
for i in range (0,n):
	lst.append(list_books[i]['id'])
def binary_search(lst, x):
	low = 0
	high = len(lst) - 1
	mid = 0
	while low <= high:
		mid = (high + low) // 2
		if lst[mid] < x:
			low = mid + 1
		elif lst[mid] > x:
			high = mid - 1
		else:
			return mid
	return -1
result = binary_search(lst, x)

if result != -1:
	print("Sách có vị trí là", str(result))
else:
	print("Không có sách cần tìm")

g = int(input("Nhập giá trị G:"))
for i in range(0, len(list_books)):
	if g < list_books[i]['price']:
		print("Cuốn sách cần tìm là:",end='')
		print("[",list_books[i]['id'],"]", "[",list_books[i]['name'],"]","[",list_books[i]['price'],"]",)

max = list_books[0]['price']
for i in range(0,len(list_books)):
	if max <= list_books[i]['price']:
		max = list_books[i]['price']
print("Cuốn sách giá cao nhất là:",end='')
for i in range(0, len(list_books)):
	if max == list_books[i]['price']:
		print("[",list_books[i]['id'],"]", "[",list_books[i]['name'],"]","[",list_books[i]['price'],"]",)
