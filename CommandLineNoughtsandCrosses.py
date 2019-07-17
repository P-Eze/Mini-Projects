game = 1
count = 0
go = 0
import sys

row = ["","","","","","","","",""]
##########################################
while game == 1:
##MAIN WHILE LOOP##
	#####Player 1#####
	while go is not 1:
		move = int(input("Where would you like to place x?"))
		if row[move-1] == "":
			row[move-1] = "x"
			go = 1
			#in order to move on to next player
			count = count + 1
			

		else:
			print("Space Occupied...")
			#makes sure we dont move onto next player
			#until unoccupied space is filled
	if row[0] == "x" and row[1]=="x" and row[2] == "x":
	            print("Player x Wins !!")
	            sys.exit()
	elif row[3] == "x" and row[4] == "x" and row[5] == "x":
	            print("Player x Wins !!")
	            sys.exit()
	elif row[6] == "x" and row[7] == "x" and row[8] == "x":
	            print("Player x Wins !!")
	            sys.exit()
	elif row[1] == "x" and row[4] == "x" and row[7] == "x":
	            print("Player x Wins !!")
	            sys.exit()
	elif row[2] == "x" and row[5] == "x" and row[8] == "x":
	            print("Player x Wins !!")
	            sys.exit()
	elif row[0] == "x" and row[4] == "x" and row[8] == "x":
	            print("Player x Wins !!")
	            sys.exit()
	elif row[6] == "x" and row[4] == "x" and row[2] == "x":
	            print("Player x Wins !!")
	            sys.exit()

	print(row[0:3])
	print(row[3:6])
	print(row[6:])

	go = 0

	if count == 9:
		print('Game Over, Its a Draw')
		sys.exit

	#####Player 2#####

	#go becomes zero and while loop starts from scratch
	#including input, before grid prints again
	#signature of a new turn
	#is the while loop starting from scratch
	while go is not 1:
		move = int(input("Where would you like to place o?"))
		if row[move-1] == "":
			row[move-1] = "o"
			go = 1
			count = count + 1
		
		else:
			print("Space Occupied...")
			#makes sure we dont move onto next player
			#until unoccupied space is filled

	if row[0] == "o" and row[1]=="o" and row[2] == "o":
	            print("Player o Wins !!")
	            sys.exit()
	elif row[3] == "o" and row[4] == "o" and row[5] == "o":
	            print("Player o Wins !!")
	            sys.exit()
	elif row[6] == "o" and row[7] == "o" and row[8] == "o":
	            print("Player o Wins !!")
	            sys.exit()
	elif row[1] == "o" and row[4] == "o" and row[7] == "o":
	            print("Player o Wins !!")
	            sys.exit()
	elif row[2] == "o" and row[5] == "o" and row[8] == "o":
	            print("Player o Wins !!")
	            sys.exit()
	elif row[0] == "o" and row[4] == "o" and row[8] == "o":
	            print("Player o Wins !!")
	            sys.exit()
	elif row[6] == "o" and row[4] == "o" and row[2] == "o":
	            print("Player o Wins !!")
	            sys.exit()

#you win before your tuen is over
	print(row[0:3])
	print(row[3:6])
	print(row[6:])
	go = 0
	if count == 9:
		print('Game Over, Its a Draw')
		sys.exit
