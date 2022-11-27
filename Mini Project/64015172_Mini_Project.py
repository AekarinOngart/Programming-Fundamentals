import random
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game():
  user_cards = []
  computer_cards = []
  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  is_game_over = False
  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      while True:
        user_action = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_action == "y" or user_action == "Y":
          user_cards.append(deal_card())
          break
        elif user_action == "n" or user_action == "N":
          is_game_over = True
          break
        else:
          print("Please try again, Type 'y' or 'n' only.")
  while computer_score != 0 and computer_score < 16:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

while True:
  start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  if start_game == "y" or start_game == "Y":
    play_game()
  elif start_game == "n" or start_game == "N":
    break
  else:
    print("Please try again, Type 'y' or 'n' only.")
