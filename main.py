from deck import Deck
from game_controller import GameController
from blackjack import Blackjack
import pandas
from player import Player


def initialize_blackjack_game():
    for _ in range(2):
        user.hand.add_card_to_hand(blackjack.get_random_card_from_deck())
        dealer.hand.add_card_to_hand(blackjack.get_random_card_from_deck())


game_controller = GameController()
blackjack = Blackjack()
for card in blackjack.deck.cards:
    print(f"{card.value} {card.suit}")


user = Player()
dealer = Player()

initialize_blackjack_game()

print(user.hand)
user.score = game_controller.calculate_score(sorted(user.hand.cards, key=lambda cards: card.return_card_value()))
dealer.score = game_controller.calculate_score(sorted(dealer.hand.cards, key=lambda cards: card.return_card_value()))
if user.score == 21:
    user_won = True

while blackjack.is_user_turn and not blackjack.user_won and not blackjack.user_busted:
    print(f"This is your hand: {user.convert_hand_to_list()} with a score of: {user.score}")
    print(f"This is the dealer hand: {dealer.hand.cards[1].value}")
    player_decision = input(f"What do you want to do? 'hit', 'stand': ")
    if player_decision.lower() == "hit":
        random_card = blackjack.get_random_card_from_deck(deck.cards)
        user.hand.add_card_to_hand(random_card)
        deck.cards.remove(random_card)
    elif player_decision.lower() == "stand":
        blackjack.is_user_turn = False
    user.score = game_controller.calculate_score(sorted(user.hand.cards, key=lambda cards: card.return_card_value()))
    if user.score == 21:
        blackjack.is_user_turn = False
    if user.score > 21:
        user_busted = True

if dealer.score >= 17 or blackjack.user_won:
    blackjack.is_dealer_turn = False

while blackjack.is_dealer_turn and not blackjack.user_busted:
    random_card = game_controller.deal_cards(deck.cards)
    dealer.hand.append(random_card)
    deck.cards.remove(random_card)
    dealer.score = game_controller.calculate_score(sorted(dealer.hand, key=lambda cards: card.return_card_value()))
    if dealer.score >= 17:
        blackjack.is_dealer_turn = False

if blackjack.user_won:
    print(f"This is your hand: {user.convert_hand_to_list()} with a score of: {user.score}")
    print(f"This is the dealer's hand : {dealer.convert_hand_to_list()} with a score of: {dealer.score}")
    print("You won!")
elif not blackjack.user_busted and dealer.score > 21:
    print(f"This is your hand: {user.convert_hand_to_list()} with a score of: {user.score}")
    print(f"This is the dealer's hand : {dealer.convert_hand_to_list()} with a score of: {dealer.score}")
    print("You won!")
elif user.score > dealer.score and not blackjack.user_busted:
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
