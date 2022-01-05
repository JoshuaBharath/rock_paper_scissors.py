import random

try:
    computer = random.choice([1, 2, 3])
    game_dictionary = {
        "1": "Rock",
        "2": "Paper",
        "3": "Scissors"
    }
    want_to_play = True
    while want_to_play:
        print("1. rock\n2. paper\n3. scissors")
        human = int(input("===> "))
        dictionary_computer = game_dictionary[str(computer)]
        dictionary_human = game_dictionary[str(human)]
        if human==computer:
            print("Its a draw")
        elif human == 1:
            if computer == 2:
                print(f"You Lose: {dictionary_computer}")
            if computer == 3:
                print(f"You Win: {dictionary_human}")
        elif human == 2:
            if computer == 1:
                print(f"You Wins: {dictionary_human}")
            if computer == 3:
                print(f"You Lose: {dictionary_computer}")
        elif human == 3:
            if computer == 1:
                print(f"You Lose: {dictionary_computer}")
            if computer == 2:
                print(f"you win: {dictionary_human}")
        else:
            print("can only use the numbers that are shown in the menu")
        print("=============================")
        print("Do you still want to play\n.. Yes\n2. No")
        still_want_to_play = int(input("==>"))
        if still_want_to_play == 2:
            want_to_play = False
except ValueError:
    print("must only type numbers, no alphabets")