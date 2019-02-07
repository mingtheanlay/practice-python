print("WELCOME TO TEXT STORY MODE")
print("By: Mingthean Lay")
print("A Night Before Exam")
print("you stay in your room")
print("what you want to do?")
user_choice = input("play game || review || prepare cheat for exam || chit chatting: ")
if user_choice == 'play game':
    what_game = input('Dota || PUBG || Fortnite: ')
    if what_game == 'Dota':
        print('Chat to the squad to join Discord.')
        print(
            "WangDer joined."
            "KhonJir joined."
            "Doro joined."
            "Guang joined."
        )
        game_mode = input("What do we play?|| ranked || turbo || all pick || :")
        if game_mode == 'ranked':
            print("WangDer rafes but he still agree to play")
            print("You start the game.")
            print("Hero Selection")
            khonjir = input("KhonJir pick || Storm || PA || ")
