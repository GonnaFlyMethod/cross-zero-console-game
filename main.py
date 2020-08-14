import time
import os


class Game:

	def __init__(self):
		self.figures = {0:'11', 2: '12', 4: '13',
		   7:'21', 9: '22', 11: '23',
		   14: '31', 16: '32', 18: '33'}

		self.barrier = ('-' + "+" + '-' + "+" + "-") + '\n'
		self.game_field = [' ' , '|', ' ', '|', ' ', '\n', self.barrier,
			  ' ' , '|', ' ', '|', ' ', '\n', self.barrier,
			  ' ' , '|', ' ', '|', ' ', '\n']

		self.game_field_elements = ' ' , '|', ' ', '|', ' ', '\n', self.barrier,

		self.X_and_O = {0: ' ', 2: ' ', 4: ' ',
		   7: ' ', 9: ' ', 11: ' ',
		   14: ' ', 16: ' ', 18: ' '}


	def clean_gamefield(self):
		self.game_field = [' ' , '|', ' ', '|', ' ', '\n', self.barrier,
			  ' ' , '|', ' ', '|', ' ', '\n', self.barrier,
			  ' ' , '|', ' ', '|', ' ', '\n']

		self.X_and_O = {0: ' ', 2: ' ', 4: ' ',
		   7: ' ', 9: ' ', 11: ' ',
		   14: ' ', 16: ' ', 18: ' '}

	def instruction(self):
		os.system('clear')
		print("Welcome to the game!") 
		print("1) I'm new here :-/\n2) I'm pro in this game :-)")
		while True:
			player_input = int(input('Choice: '))

			if player_input == 1:
				os.system('clear')
				print("Hi! I will be your guide (: !")
				time.sleep(3)
				self.draw_field()
				print("This is your game field!")
				time.sleep(3)
				self.draw_field()
				print('X starts first!')
				time.sleep(3)
				self.draw_field()
				print("To set the 'X' on the game field you need to set the")
				print("coordinates, for example: 1,2 or 3,3")
				time.sleep(10)
				self.draw_field()
				print("Ok, let me show you how does it work :)")
				time.sleep(6)
				self.game_field[2] = "X"
				self.draw_field()
				print("I've chosen coordinates 1,2. 1 means the row and 2")
				print("means the column")
				time.sleep(10)
				self.draw_field()
				print("Then 'O' is choosing the position on the game field")
				time.sleep(6)
				self.game_field[9] = "O"
				self.draw_field()
				print('Center? Not bad, buddy!')
				time.sleep(2)
				print('- Thanks c:')
				time.sleep(5)
				self.clean_gamefield()
				self.game_field[7] = "X"
				self.game_field[9] = "X"
				self.game_field[11] = "X"
				self.draw_field()
				print("You will be the winner of the game if you'll set 3 'X'\n"
				"figures in one row (or 'O' figures if you're playing for 'O')")
				time.sleep(10)
				self.clean_gamefield()
				self.game_field[0] = "X"
				self.game_field[7] = "X"
				self.game_field[14] = "X"
				self.draw_field()
				print("It also works with columns! ;)")
				time.sleep(4)
				self.clean_gamefield()
				self.game_field[4] = "X"
				self.game_field[9] = "X"
				self.game_field[14] = "X"
				self.draw_field()
				print("And diagonals!")
				time.sleep(4)
				os.system('clear')
				print("You can challenge your friend and play together c:")
				time.sleep(5)
				os.system('clear')
				print("Or you can play with yourself, it's also cool they say")
				time.sleep(5)
				os.system('clear')
				print("That's all! Good luck and have fun!")
				self.clean_gamefield()
				time.sleep(5)
				break
			else:
				break

	def draw_field(self):	
		os.system('clear')
		for element in self.game_field:
			print(element, end='')

		time.sleep(0.5)

	def get_coord_of_X(self):
		all_right = False
		warning = False
		while not all_right:

			if warning:
				print("Wrong coordinates. Try again!")
			print('')
			player_input = str(input('X: '))

			coords = ''
			for i in player_input:
				if i.isdigit():
					coords += i

			if coords not in self.figures.values():
				warning = True
				continue

			pos_of_new_element_X = None
			for k, v in self.figures.items():
				if coords == v and self.X_and_O[k] == " ":
					pos_of_new_element_X = k
					all_right = True
					break
				elif coords == v and self.X_and_O[k] != " ":
					warning = True

		self.game_field[pos_of_new_element_X] = "X"
		self.X_and_O[pos_of_new_element_X] = "X"

		os.system('clear')

	def get_coord_of_O(self):
		all_right = False
		warning = False
		while not all_right:
			if warning:
				print("Wrong coordinates. Try again!")

			print('')
			player_input = str(input('O: '))

			coords = ''
			for i in player_input:
				if i.isdigit():
					coords += i

			if coords not in self.figures.values():
				warning = True
				continue

			pos_of_new_element_O = None
			for k, v in self.figures.items():
				if coords == v and self.X_and_O[k] == " ":
					pos_of_new_element_O = k
					all_right = True
					break
				elif coords == v and self.X_and_O[k] != " ":
					warning = True

		self.game_field[pos_of_new_element_O] = "O"
		self.X_and_O[pos_of_new_element_O] = "O"
		os.system('clear')

	def arbitrage(self):
		X_PLAYER_WINS = False
		O_PLAYER_WINS = False

		horizontals = [[0, 2, 4], [7, 9, 11], [14, 16, 18]]
		for i in horizontals:
			checker_for_X = 0
			checker_for_O = 0
			for j in i:
				if self.X_and_O[j] == "X":
					checker_for_X += 1
				elif self.X_and_O[j] == "O":
					checker_for_O += 1
				else:
					checker_for_X = 0
					checker_for_O = 0

				if checker_for_X == 3:
					return "X won the game!"
				elif checker_for_O == 3:
					return "O won the game!"

		verticals = [[0, 7, 14], [2, 9, 16], [4, 11 , 18]]
		for i in verticals:
			checker_for_X = 0
			checker_for_O = 0
			for j in i:
				if self.X_and_O[j] == "X":
					checker_for_X += 1
				elif self.X_and_O[j] == "O":
					checker_for_O += 1
				else:
					checker_for_X = 0
					checker_for_O = 0

				if checker_for_X == 3:
					return "X won the game!"
				elif checker_for_O == 3:
					return "O won the game!"

		if (self.X_and_O[0] == "X" and self.X_and_O[9] == "X" and 
		   self.X_and_O[18] == "X"):
			return "X won the game!"

		elif (self.X_and_O[0] == "O" and self.X_and_O[9] == "O" and 
		     self.X_and_O[18] == "O"):
		 	return "O won the game!"

		if (self.X_and_O[4] == "X" and self.X_and_O[9] == "X" and 
		   self.X_and_O[14] == "X"):
			return "X won the game!"
		elif (self.X_and_O[4] == "O" and self.X_and_O[9] == "O" and 
		     self.X_and_O[14] == "O"):
			return "O won the game!"

		checker = 0
		for i in self.X_and_O.values():
			if i != " ":
				checker +=1

		if checker == 9:
			return "Draw"
		return None

	def __call__(self):
		self.instruction()

		while True:
			self.draw_field()
			self.get_coord_of_X()
			check_1 = self.arbitrage()
			if check_1== "X won the game!":
				self.draw_field()
				print("X won the game!")
				time.sleep(3)
				os.system('clear')
				print('1) Play one more time\n2) Exit')
				while True:
					player_input = int(input('Choice: '))
					if player_input == 1:
						self.clean_gamefield()
						break
					elif player_input == 2:
						os.system('clear')
						exit()
					else:
						continue
				continue
			elif check_1 == "O won the game!":
				self.draw_field()
				print("O won the game!")
				time.sleep(3)
				os.system('clear')
				print('1) Play one more time\n2) Exit')
				while True:
					player_input = int(input('Choice: '))
					if player_input == 1:
						self.clean_gamefield()
						break
					elif player_input == 2:
						os.system('clear')
						exit()
					else:
						continue
				continue
			elif check_1 == "Draw":
				self.draw_field()
				print("Draw")
				time.sleep(3)
				os.system('clear')
				print('1) Play one more time\n2) Exit')
				while True:
					player_input = int(input('Choice: '))
					if player_input == 1:
						self.clean_gamefield()
						break
					elif player_input == 2:
						os.system('clear')
						exit()
					else:
						continue
				continue
			self.draw_field()
			self.get_coord_of_O()

			check_2 = self.arbitrage() 
			if check_2 == "X won the game!":
				self.draw_field()
				print("X won the game!")
				time.sleep(3)

				os.system('clear')
				print('1) Play one more time\n2) Exit')
				while True:
					player_input = int(input('Choice: '))
					if player_input == 1:
						self.clean_gamefield()
						break
					elif player_input == 2:
						os.system('clear')
						exit()
					else:
						continue
				continue

			elif check_2 == "O won the game!":
				self.draw_field()
				print("O won the game!")
				time.sleep(3)
				os.system('clear')
				print('1) Play one more time\n2) Exit')
				while True:
					player_input = int(input('Choice: '))
					if player_input == 1:
						self.clean_gamefield()
						break
					elif player_input == 2:
						os.system('clear')
						exit()
					else:
						continue
				continue

			elif check_2 == "Draw":
				self.draw_field()
				print("Draw")
				time.sleep(3)
				os.system('clear')

				print('1) Play one more time\n2) Exit')
				while True:
					player_input = int(input('Choice: '))
					if player_input == 1:
						self.clean_gamefield()
						break
					elif player_input == 2:
						os.system('clear')
						exit()
					else:
						continue
				continue

X_and_O_GAME = Game()

X_and_O_GAME()
os.system('clear')
