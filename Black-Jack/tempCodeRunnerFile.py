    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards are {user_cards}, current score: {user_score}")
    print(f"Computer's first cards: {computer_cards[0]}")

    if user_score==0 or computer_score == 0 or user_score>21:
        is_game_over=True
    else:
        user_should_deal = input("type 'y' to get another cards, type 'n' to pass")
        if user_should_deal == "y":
            user_cards.append(deal_card())
        else:
            is_game_over=True