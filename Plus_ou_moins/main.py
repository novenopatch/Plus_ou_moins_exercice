import random
import sys


def jeu_plus_ou_moins(points=50,start=1,end=100):
    print(f"Vous avez {points} points de départ.")
    print("Bienvenue dans le jeu Plus ou Moins!")

    consecutive_wins_and_losses = [0, 0]

    while points > 0:
        random_int = random.randint(start, end)
        print(random_int)

        for _ in range(3):
            try:
                user_input_value = input("Devinez le nombre : ")
                if user_input_value == "exit":
                    sys.exit()
                user_input_value = int(user_input_value)
                if user_input_value == random_int:
                    points += 10
                    consecutive_wins_and_losses[0] += 1
                    consecutive_wins_and_losses[1] = 0
                    print(consecutive_wins_and_losses)
                    print(f"Félicitations ! Vous avez deviné le nombre. Vous gagnez {points} points.")
                    break
                elif user_input_value < random_int:
                    print("Trop bas. Essayez encore.")
                else:
                    print("Trop élevé. Essayez encore.")
            except ValueError:
                print("Veuillez entrer un nombre entier valide.")

        else:
            print(f"Désolé, vous n'avez pas deviné le nombre. Le nombre était {random_int}. Vous perdez 15 points.")
            points -= 15
            consecutive_wins_and_losses[1] += 1
            consecutive_wins_and_losses[0] = 0
            print(f"Vous avez maintenant {points} points.")

        if consecutive_wins_and_losses[0] == 2:
            points *= 2
            consecutive_wins_and_losses[0] = 0
            print(f"Vous avez gagné deux parties consécutives ! Votre mise est maintenant de {points} points.")
        elif consecutive_wins_and_losses[1] == 2:
            points = points // 2
            consecutive_wins_and_losses[1] = 0
            print(f"Vous avez perdu deux parties consécutives. Votre mise est maintenant de {points} points.")
    print("Le jeu est terminé. Votre mise est épuisée.")


if __name__ == '__main__':
    jeu_plus_ou_moins()
