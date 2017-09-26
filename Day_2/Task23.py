from random import randint

def play_again_question():
    while True:
        print()
        answer = input('Czy chcesz zagrać od nowa? ')
        if answer == 'tak':
            game()
        elif answer == 'nie':
            print('Zakończyłeś grę. Dziękujemy za zabawę!')
            return False
        else:
            print('Odpowiedź w złym formacie. Dostępne formy odpowiedzi: tak/nie')

def game():
    print()
    print('Komputer wylosował jedną liczbę całkowitą z zakresu 1 do 100. Spróbuj zgadnąć jaką.')
    computer_number = randint(1,100)

    game_count = 1
    while game_count <= 3:
        while True:
            print()
            user_number = input('Wybierz liczbę: ')
            try:
                int(user_number)
            except ValueError:
                print('Błąd. Pamiętaj żeby wprowadzić liczbę całkowitą.')
                break
            if int(user_number) == computer_number:
                print('Zgadłeś, jesteś super!')
                return False
            else:
                while True:
                    if game_count == 3:
                        print('Podałeś trzy błędne odpowiedzi. Koniec gry.')
                        return False
                    else:
                        print()
                        answer = input('To nie ta liczba. Czy chcesz spróbować jeszcze raz? ')
                        if answer == 'tak':
                            game_count += 1
                            break
                        elif answer == 'nie':
                            print('Zakończyłeś grę. Dziękujemy za zabawę!')
                            return False
                        else:
                            print('Odpowiedź w złym formacie. Dostępne formy odpowiedzi: tak/nie')

game()
play_again_question()

