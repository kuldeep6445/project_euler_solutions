import time
t = time.time()

def check_empty_spaces(arr,l):
    for i in range(9):
        for j in range(9):
            if arr[i][j]==0:
                l[0] = i
                l[1] = j
                return True
    return False

def show(arr):
    for i in range(9):
        for j in range(9):
            print(arr[i][j],end=" ")
        print()

def column_check(arr,num,ypos):
    for i in range(9):
        if arr[i][ypos]==num:
            return False
    return True

def used_in_box(arr,row,col,num): 
	for i in range(3): 
		for j in range(3): 
			if(arr[i+row][j+col] == num): 
				return False
	return True

def row_check(arr,num,xpos):
    for i in range(9):
        if arr[xpos][i]==num:
            return False
    return True

def overall_check(arr,num,xpos,ypos):
    if row_check(arr,num,xpos) and column_check(arr,num,ypos) and used_in_box(arr,xpos-xpos%3,ypos-ypos%3,num):
        return True
    return False
        
def solve(arr):
    l = [0,0]
    if not check_empty_spaces(arr,l):
        show(arr)
        return True
    xpos = l[0]
    ypos = l[1]
    for num in range(1,10):
        if overall_check(arr,num,xpos,ypos):
            arr[xpos][ypos] = num
            if solve(arr):
                return True
            arr[xpos][ypos] = 0
    return False
    

def solution():
    arr = [[0 for j in range(9)]for i in range(9)]
    arr = [ [5,3,0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]]
    if not solve(arr):
        print('no solution possible')
solution()
print('time taken : ',time.time()-t)
