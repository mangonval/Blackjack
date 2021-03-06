from blackjack import Blackjack
from dealer import Dealer
from human_player import HumanPlayer


def initialize_blackjack_game():
    for _ in range(2):
        player.hand.add_card_to_hand(blackjack.get_random_card_from_deck())
        dealer.hand.add_card_to_hand(blackjack.get_random_card_from_deck())


blackjack = Blackjack()
player = HumanPlayer()
dealer = Dealer()
initialize_blackjack_game()
if player.hand.score == 21:
    user_won = True
while blackjack.is_user_turn and not blackjack.user_won and not blackjack.user_busted:
    print(f"This is your hand: {player.convert_hand_to_list()} with a score of: {player.hand.score}")
    print(f"This is the dealer hand: {dealer.hand.cards[1].value}")
    player_decision = input(f"What do you want to do? 'hit', 'stand': ")
    if player_decision.lower() == "hit":
        player.hand.add_card_to_hand(blackjack.get_random_card_from_deck())
    elif player_decision.lower() == "stand":
        blackjack.is_user_turn = False
    if player.hand.score == 21:
        blackjack.is_user_turn = False
    if player.hand.score > 21:
        blackjack.user_busted = True

if dealer.dealer_has_to_stand() or blackjack.user_won:
    blackjack.is_dealer_turn = False

while blackjack.is_dealer_turn and not blackjack.user_busted:
    dealer.hand.add_card_to_hand(blackjack.get_random_card_from_deck())
    if dealer.dealer_has_to_stand():
        blackjack.is_dealer_turn = False

if blackjack.user_won:
    print(f"This is your hand: {player.convert_hand_to_list()} with a score of: {player.hand.score}")
    print(f"This is the dealer's hand : {dealer.convert_hand_to_list()} with a score of: {dealer.hand.score}")
    print("You won!")
elif not blackjack.user_busted and dealer.hand.score > 21:
    print(f"This is your hand: {player.convert_hand_to_list()} with a score of: {player.hand.score}")
    print(f"This is the dealer's hand : {dealer.convert_hand_to_list()} with a score of: {dealer.hand.score}")
    print("You won!")
elif player.hand.score > dealer.hand.score and not blackjack.user_busted:
    print(f"This is your hand: {player.convert_hand_to_list()} with a score of: {player.hand.score}")
    print(f"This is the dealer's hand : {dealer.convert_hand_to_list()} with a score of: {dealer.hand.score}")
    print("You won!")
else:
    print(f"This is your hand: {player.convert_hand_to_list()} with a score of: {player.hand.score}")
    print(f"This is the dealer's hand : {dealer.convert_hand_to_list()} with a score of: {dealer.hand.score}")
    print("You lost!")
