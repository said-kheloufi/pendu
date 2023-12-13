import pygame
import math
import random
import sys

pygame.init()

# setup display
WIDTH, HEIGHT = 1200, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")

# button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)

# load images.
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

# game variables
hangman_status = 0
words = []
word = ""

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def charger_mots():
    try:
        with open("mots.txt", "r") as file:
            mots = file.read().splitlines()
        return mots
    except FileNotFoundError:
        print("Le fichier 'mots.txt' n'a pas été trouvé.")
        return []
    

def initialiser_fichier_mots():
    try:
        with open("mots.txt", "r") as file:
            pass  # Le fichier existe déjà
    except FileNotFoundError:
        with open("mots.txt", "w") as file:
            pass  # Créer un nouveau fichier


def menu():
    print("Menu:")
    print("1. Jouer")
    print("2. Insérer un mot dans le fichier")

    choix = input("Choisissez une option (1/2): ")
    return choix


def inserer_mot():
    mot = input("Entrez un mot à insérer dans le fichier 'mots.txt': ")
    with open("mots.txt", "a") as file:
        file.write(mot + "\n")


def handle_key_press(key):
    global hangman_status, guessed

    if key.isalpha() and key.islower():
        if key not in guessed:
            guessed.append(key)
            if key not in word:
                hangman_status += 1


def draw():
    win.fill(WHITE)

    # draw title
    text = TITLE_FONT.render("DEVELOPER HANGMAN", 1, BLACK)
    win.blit(text, (WIDTH / 2 - text.get_width() / 2, 20))

    # draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))
   
    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()


def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(3000)


def main():
    global hangman_status, word, guessed
run = True
while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()



        choix = menu()

        if choix == '1':
            # Choix aléatoire d'un mot depuis la liste
            words = charger_mots()
            if not words:
                print("Le fichier 'mots.txt' ne contient aucun mot. Veuillez insérer un mot.")
                continue

            word = random.choice(words)
        elif choix == '2':
            # Insérer un mot dans le fichier
            inserer_mot()
            continue
        else:
            print("Option invalide. Veuillez choisir une option valide.")
            continue

        # Réinitialiser le jeu
        hangman_status = 0
        guessed = []

        FPS = 60
        clock = pygame.time.Clock()
        
        
        while y:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    y = False
                elif event.type == pygame.KEYDOWN:
                    handle_key_press(event.unicode.lower())

            draw()

            won = all(letter in guessed for letter in word)
            if won:
                display_message("You WON!")
                break

            if hangman_status == 6:
                display_message("You LOST!")
                break


            


if __name__ == "__main__":
    main()
pygame.quit()
