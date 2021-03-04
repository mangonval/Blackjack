from deck import Deck
from game_controller import GameController
import pandas
from player import Player


def initialize_blackjack_game():
    for _ in range(2):
        card_to_add = game_controller.deal_cards(deck.cards)
        user.hand.cards.append(card_to_add)
        deck.cards.remove(card_to_add)
        card_to_add = game_controller.deal_cards(deck.cards)
        dealer.hand.cards.append(card_to_add)
        deck.cards.remove(card_to_add)


game_controller = GameController()
deck_data = pandas.read_csv("blackjack_cards.csv")
deck = Deck(deck_data.values.tolist())
for card in deck.cards:
    print(f"{card.value} {card.suit}")

is_user_turn = True
is_dealer_turn = True
user_busted = False
user_won = False
user = Player()
dealer = Player()

initialize_blackjack_game()

print(user.hand)
user.score = game_controller.calculate_score(sorted(user.hand.cards, key=lambda cards: card.return_card_value()))
dealer.score = game_controller.calculate_score(sorted(dealer.hand.cards, key=lambda cards: card.return_card_value()))
if user.score == 21:
    user_won = True

while is_user_turn and not user_won and not user_busted:
    print(f"This is your hand: {user.convert_hand_to_list()} with a score of: {user.score}")
    print(f"This is the dealer hand: {dealer.hand.cards[1].value}")
    player_decision = input(f"What do you want to do? 'hit', 'stand': ")
    if player_decision.lower() == "hit":
        random_card = game_controller.deal_cards(deck.cards)
        user.hand.cards.append(random_card)
        deck.cards.remove(random_card)
    elif player_decision.lower() == "stand":
        is_user_turn = False
    user.score = game_controller.calculate_score(sorted(user.hand.cards, key=lambda cards: card.return_card_value()))
    if user.score == 21:
        is_user_turn = False
    if user.score > 21:
        user_busted = True

if dealer.score >= 17 or user_won:
    is_dealer_turn = False

while is_dealer_turn and not user_busted:
    random_card = game_controller.deal_cards(deck.cards)
    dealer.hand.append(random_card)
    deck.cards.remove(random_card)
    dealer.score = game_controller.calculate_score(sorted(dealer.hand, key=lambda cards: card.return_card_value()))
    if dealer.score >= 17:
        is_dealer_turn = False

if user_won:
    print(f"This is your hand: {user.convert_hand_to_list()} with a score of: {user.score}")
    print(f"This is the dealer's hand : {dealer.convert_hand_to_list()} with a score of: {dealer.score}")
    print("You won!")
elif not user_busted and dealer.score > 21:
    print(f"This is your hand: {user.convert_hand_to_list()} with a score of: {user.score}")
    print(f"This is the dealer's hand : {dealer.convert_hand_to_list()} with a score of: {dealer.score}")
    print("You won!")
elif user.score > dealer.score and not user_busted:
    print(f"This is your hand: {user.convert_hand_to_list()} with a score of: {user.score}")
    print(f"This is the dealer's hand : {dealer.convert_hand_to_list()} with a score of: {dealer.score}")
    print("You won!")
else:
    print(f"This is your hand: {user.convert_hand_to_list()} with a score of: {user.score}")
    print(f"This is the dealer's hand : {dealer.convert_hand_to_list()} with a score of: {dealer.score}")
    print("You lost!")

#
# game_controller = GameController()
# print(f"Score: {game_controller.calculate_score(sorted(deck.cards, key=lambda card: card.return_card_value()))}")
