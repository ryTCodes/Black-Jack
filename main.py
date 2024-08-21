import random
import os
from art import logo


def main():
    while input("Start Blackjack? Type 'y' or 'n': ").lower() == 'y':
        os.system('cls')
        blackjack()


def deal_card() -> int:
    cards: list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards) -> int:
    total: int = sum(cards)
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and total > 21:
        cards.remove(11)
        cards.append(1)
    return total


def compare_score(user_score, computer_score) -> None:
    if user_score == computer_score:
        return "It's a draw!"
    elif user_score > 21 and computer_score > 21:
        return "It's a draw, both went over 21!"
    elif user_score == 0:
        return "Win with a Blackjack!"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack!"
    elif user_score > 21:
        return "You went over. You lose!"
    elif computer_score > 21:
        return "Opponent went over. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"


def blackjack() -> None:
    print(logo)

    user_cards: list = []
    computer_cards: list = []
    game_is_on: bool = True

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while game_is_on:

        user_score: int = calculate_score(user_cards)
        computer_score: int = calculate_score(computer_cards)

        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_is_on = False
        else:
            user_input = input("Type 'y' to get another card, Type 'n' to pass: ")
            if user_input == 'y':
                game_is_on = True
                user_cards.append(deal_card())
            else:
                game_is_on = False

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare_score(user_score, computer_score))


if __name__ == "__main__":
    main()
