
#   The game is a board game that with 15 * 15 board. 
# 	There are 2 players in total, player_one and player_two, the player_one will play with pieces of 'X' and player_two will play with pieces of 'O'.
# 	The player who has 5 same pieces in a row will win the game.
# 	The class below including the initial setting of the board and the current player. The player will begin from the player with 'X' pieces.
# 	The initial setting of the finish variable is False, once the finish turned to True, game finished.

from Project_check import check
from termcolor import colored
from colorama import init
import os

class GameFiveRow:
	def __init__(self, size = 15):
		print("Welcome to the game:Gomoku - Five in a row")
		self.size = size
		self.board = []
		self.current_player = "player_one"

		for i in range(self.size):
			self.board.append(['-'] * self.size)

		self.print_board()

		self.finish = False


#   The print function including the setting of the board.
#   The rows have been labeled with number 1 - 15.
#   The columns have been labeled with upper case of alphabet letters A to 0

	def print_board(self):
		print("      A  B  C  D  E  F  G  H  I  J  K  L  M  N  O")


		for column_num in range(1, self.size + 1):

			colored_lst = map(lambda x: colored(x, 'red',attrs=['bold']) if x == 'O' else colored(x, 'blue',attrs=['bold']) if x == 'X' else x, self.board[column_num - 1])

			if column_num >= 10:
				s = str(column_num) + '    ' + '  '.join(colored_lst) + '\n'
			else:
				s = str(column_num) + '     ' + '  '.join(colored_lst) + '\n'
			
			print(s)

#   The add piece function including the parameter with the row and column of the board.
#   The function will indetify who is the current player, if the current player is player_one, 'X' will be placed to the board, otherwise 'O' will be placed.


	def add_piece(self, row, col):

		if self.current_player == "player_one":
			self.board[row][col] = 'X'
		else:
			self.board[row][col] = 'O'

		check_result = check(self.board, row, col)

		if check_result == True:
			self.print_board()
			print(self.current_player,"Win")
			self.finish = True
		else:
			self.print_board()


#   The file save function will save the current player and current board to a txt file.
#   The data type of txt file is string.


	def file_save(self):
		f = open("gomoku.txt","w")
		f.write(str(self.current_player)+'\n')

		for l in self.board:
			f.write(' '.join(l) + '\n')

		f.close()


#   The file load function will load the saved file and update the current player and board with the current player and board save in the file.
#   The data type of the board and current file is string, the file load function will format it to list.



	def file_load(self):
		file = open("gomoku.txt","r")

		lines = file.readlines()

		self.board = []
		
		for line in range(len(lines)):
			if line == 0:
				self.current_player = lines[line].strip()
			else:
				l = lines[line].split()
				self.board.append(l)
		
		self.print_board()

		file.close()


#   The start function is the main function of the game.

#   The main function includes the add pieces,save, load and restart sub-function, the filter will call the function depends on the input.
#    - If the input is stop, the function will stop
#    - If the input is save, the function will call the save function
#    - If the input is load, the function will call the file load function
#    - If the input is restart, the function will reset the board and current player to initial and restart the whole game.
#    - If the input is the position, the function will check the boardary of the input to make sure the poistion is not out of range. Then call the function of adding pieces to place the piece on the board.

#   The while loop started with the initial setting of the variable finish is False, if the checking function find out the winning player, variable finish will change to True, then the whole loop will stop.


	def start(self):

		while not self.finish:

			enter_the_position = input("Please enter the position:" + str(self.current_player) + ':')

			if enter_the_position.lower() != "stop" and enter_the_position.lower() != "save" and enter_the_position.lower() != "load" and enter_the_position.lower() != "restart":
				if int(ord(enter_the_position[-1])) >= 65 and int(ord(enter_the_position[-1])) <= 79\
				and int(enter_the_position[:-1]) >= 1 and int(enter_the_position[:-1]) <= 15:

					row = int(enter_the_position[:-1]) - 1
					col = int(ord(enter_the_position[-1])) - 65

					if self.board[row][col] == '-':
						self.add_piece(row, col)
						# self.check(row,col)
					else:
						print("Please enter the right position")
						game.start()

					if self.current_player == "player_one":
						self.current_player = "player_two"
					else:
						self.current_player = "player_one"
				else:
					print("Please enter the right position")

			#Calling the function of save the file
			elif enter_the_position.lower() == "save":
				try:
					filename = "gomoku.txt"
					if os.path.isdir(filename):
						print("This is not a file")
					elif os.path.exists(filename):
						answer = input("Do you want to replace the file(y/n):")
						if answer == "y":
							self.file_save()
						else:
							game.start()
				except PermissionError:
					print("You do not have the permission")
				except OSError:
					print("Could not find the file")


			#Calling the function of load the file 
			elif enter_the_position.lower() == "load":
				self.file_load()
				game.start()


			#Calling the function of restart the game
			elif enter_the_position.lower() == "restart":
				current_player = "player_one"
				self.board = []
				for i in range(self.size):
					self.board.append(['-'] * self.size)
				self.print_board()
				game.start()

			else:
				self.finish = True


game = GameFiveRow()
game.start()













