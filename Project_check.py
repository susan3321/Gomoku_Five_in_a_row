'''
The check function including the parameter with the row and column of the board.
The function will run after any player placed the piece on the board to check whether there exists five pieces in a row for the player.
If the result is "Yes", the initial variable of finish will turn to True, that will stop the while loop in the main function.

'''
def check(board,row,col):

	i = 1
	count = 1

	#check the up and down
	while row - i >= 0 and count <= 5:
		if board[row-i][col] == board[row][col]:
			count +=1
			i +=1
		else:
			break
	i = 1

	while row + i <= 14 and count <= 5:
		if board[row+i][col] == board[row][col]:
			count +=1
			i +=1
		else:
			break

	if count >= 5:
		return True
	
	i =1
	count = 1

	#check the left and right

	while col - i >=0 and count <=5:
		if board[row][col-i] == board[row][col]:
			count +=1
			i +=1
		else:
			break
	i = 1

	while col + i <=14 and count <=5:
		if board[row][col+i] == board[row][col]:
			count +=1
			i +=1
		else:
			break

	if count >= 5:
		return True
	
	i = 1
	count = 1

	#check the right up and left down

	while col - i >=0 and row - i >=0 and count <=5:
		if board[row-i][col-i] == board[row][col]:
			count +=1
			i +=1
		else:
			break
	i = 1

	while col + i <=14 and row + i <=14 and count <=5:
		if board[row+i][col+i] == board[row][col]:
			count +=1
			i +=1
		else:
			break

	if count >= 5:
		return True

	i = 1
	count = 1

	#check the left up and right down

	while col - i>=0 and row + i <=14 and count <=5:
		if board[row+i][col-i] == board[row][col]:
			count +=1
			i +=1
		else:
			break

	while col + i <=14 and row - i >=0 and count <=5:
		if board[row-i][col+i] == board[row][col]:
			count +=1
			i +=1
		else:
			break

	if count >= 5:
		return True

	return False