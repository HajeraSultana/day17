from getpass import getpass as input

print("🪨Rock 📄Paper ✂️Scissors! the ultimate game of chance")
print()
print("""Get ready for the ultimate battle of wits...and luck!
Let's play!""")
print()
player1counter = 0
player2counter = 0
while True:
  print("Make your move (R, P or S)")
  print()
  player1Move = input("Player 1 >")
  player2Move = input("player 2 >")
  if player1Move == "R" and player2Move == "R":
     print("You both picked Rock, draw!")
  elif player1Move == "S" and player2Move == "S":
      print("Ka-Shing! Scissors bounce off each other like a dodgy sword fight! Draw.")
  elif player1Move == "P" and player2Move == "P":
      print("Two bits of paper flap at each other. Dissapointing. Draw.")
  elif player1Move == "R" and player2Move == "P":
      print("Player1's Rock is smothered by Player2's Paper!")
      player2counter += 1
  elif player1Move == "R" and player2Move == "S":
      print("Player1 smashed Player2's Scissors into dust with their Rock!")
      player1counter += 1
  elif player1Move == "P" and player2Move == "R":
      print("Player1 wins! Paper beats rock!")
      player1counter += 1 
  elif player1Move == "P" and player2Move == "S":
      print("Player1's Paper is cut into tiny pieces by Player2's Scissors!")
      player2counter += 1
  elif player1Move == "S" and player2Move == "R":
      print("Player2 beats player1 wiht rock!")
      player2counter += 1
  elif player1Move == "S" and player2Move == "P":
      print("Scissors beats paper! Player1 is the winner.")
      player1counter += 1
  else:
      print("Thanks for playing! PLayer 1 score:", player1counter, "Player 2 score:", player2counter)
      break
  if player1counter == 3 or player2counter == 3:
    print("Thanks for playing! Player 1 scored", player1counter, "and Player 2 scored", player2counter)
    exit()
  else:
    continue