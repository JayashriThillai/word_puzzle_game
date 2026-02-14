import pygame  #import python for create the game
import random  #to import the random value
import time  #to give the time limits

pygame.init()  #initializes the pygame modules to run
# for screen and logo
WIDTH, HEIGHT = 900,500
screen = pygame.display.set_mode((WIDTH, HEIGHT))  #set the window dimensions
pygame.display.set_caption("Word Scramble")  #creates the window
logo=pygame.image.load("G:\My Drive\\WS.png")  #import the image
pygame.display.set_icon(logo)
WHITE = (255, 255, 255)  #rgb colour values
BLACK = (0, 0, 0)  #rgb colour value
RED = (255, 0, 0)
BLUE=(0,0,255)

FONT = pygame.font.Font(None, 50)  #for large font
SMALL_FONT = pygame.font.Font(None, 30)  #for smaller font
background_image = pygame.image.load("G:\My Drive\\ws back.png")  #for background
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT)) #fits into the window size
words = ["python","engineering","laptop","electronics","communication","explore","research","doubt"]
current_word = random.choice(words) #to select the random word in words
scrambled_word = ''.join(random.sample(current_word, len(current_word)))
pygame.mixer.music.load("C:\\Users\\Welcome\\Downloads\\WORD GAME- Scramble - Music Instruments.mp3")
pygame.mixer.music.play(-1,0.0)


# initialize the following values
typed_word = ""
score = 0
hint_shown = False
time_limit = 10
timer_start = time.time()
alert_message = ""  

#RENDERS THE TEXT COLOR IN THE SUITABLE POSITION
def draw_text(text, x, y, font, color=BLACK, center=False):
    surface = font.render(text, True, color) 
    rect = surface.get_rect(center=(x, y)) if center else (x, y)
    screen.blit(surface, rect)

#the rulebook
def show_instructions():
    screen.blit(background_image, (0, 0))
    draw_text("Welcome to the Scramble world!!!", WIDTH // 2, HEIGHT // 3, FONT, color=BLACK, center=True)
    draw_text("Game Rulebook:", WIDTH // 2, HEIGHT // 2 - 50, SMALL_FONT, color=BLACK, center=True)
    draw_text("1. Unscramble the word by typing it correct word.", WIDTH // 2, HEIGHT // 2, SMALL_FONT, color=BLACK, center=True)
    draw_text("2. You have 10 seconds to guess each word.", WIDTH // 2, HEIGHT // 2 + 40, SMALL_FONT, color=BLACK, center=True)
    draw_text("3. Correct answers will give you a 10 points.", WIDTH // 2, HEIGHT // 2 + 80, SMALL_FONT, color=BLACK, center=True)
    draw_text("4. Press '1' to reveal the first letter only once (3 points deducted).", WIDTH // 2, HEIGHT // 2 + 120, SMALL_FONT, color=BLACK, center=True)
    draw_text("Press Space to start the game", WIDTH // 2, HEIGHT - 100, FONT, color=RED, center=True)
    pygame.display.flip()  #to update the screen to the next

    #to quit and space key to start
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  
                    running = False
                    return  

# main game loop
def game_loop():
    global current_word, scrambled_word, typed_word, score, hint_shown, timer_start, alert_message
    current_word = random.choice(words)
    scrambled_word = ''.join(random.sample(current_word, len(current_word)))
    typed_word = ""
    score = 0
    hint_shown = False
    timer_start = time.time()
    #to repeat the infinitely
    running = True
    while running:
        screen.blit(background_image, (0, 0))  #to change the background by filling the before
        time_left = time_limit - int(time.time() - timer_start)  #calculate the time by subtrating from initial time
        if time_left <= 0:
            draw_text("Time's Up! Game Over!", WIDTH // 2, HEIGHT // 2, FONT, color=BLUE, center=True)
            pygame.display.flip()  #changes the new content
            pygame.time.delay(2000)
            running = False
            continue
        #hint showing and instruction
        draw_text("Press '1' for a hint (reveals the first letter).", WIDTH // 2, 50, SMALL_FONT, center=True)
        draw_text(f"Scrambled: {scrambled_word}", WIDTH // 2, 100, FONT, center=True)
        draw_text(f"Your Guess: {typed_word}", WIDTH // 2, 200, FONT, center=True)

        #penalty for hint showing
        if hint_shown:
            draw_text(f"Hint: {current_word[0]}", WIDTH // 2, 300, FONT, color=RED, center=True)
            draw_text("3 points deducted for hint.", WIDTH // 2, 350, SMALL_FONT, color=RED, center=True)

        #to display the given answer is wrong
        if alert_message:
            draw_text(alert_message, WIDTH // 2, HEIGHT // 2, SMALL_FONT, color=RED, center=True)
        
        #to display score and time
        draw_text(f"Time Left: {time_left}s", 10, 10, SMALL_FONT)
        draw_text(f"Score: {score}", WIDTH - 150, 10, SMALL_FONT)

        #conditions for pressing the key
        for event in pygame.event.get():
            pygame.mixer.music.play(-1,0.0)
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:   
                    if typed_word.lower() == current_word:
                        score += 10  
                        current_word = random.choice(words)
                        scrambled_word = ''.join(random.sample(current_word, len(current_word)))
                        typed_word = ""
                        hint_shown = False  
                        alert_message = ""
                        pygame.mixer.music.play(-1,0.0)
                        timer_start = time.time()
                    else:
                        draw_text("Wrong! Try Again.", WIDTH // 2, HEIGHT - 50, SMALL_FONT, color=BLUE, center=True)
                        pygame.display.flip()
                        pygame.time.delay(1000)
                # FOR USE THE BACKSPACE
                elif event.key == pygame.K_BACKSPACE:
                    typed_word = typed_word[:-1]
                #TO SHOW THE HINT
                elif event.key == pygame.K_1:
                    if not hint_shown:
                        hint_shown = True
                        score -= 3 
                        alert_message = ""
                #OTHER KEYS AND THEIR CHARACTERS
                else:
                    typed_word += event.unicode
        pygame.display.flip()  #UPDATE THE GAME WITH NEW SCREEN
show_instructions()
game_loop()
pygame.quit()