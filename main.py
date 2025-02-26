import random

def number_guessing_game():
    secret_number = random.randint(1, 10)
    attempts = 0
    
    while True:
        guess = int(input("1부터10중에아무거나써보라노: "))
        attempts += 1
        
        if guess < secret_number:
            print("더큰수고맨라잌마이딕")
        elif guess > secret_number:
            print("더작은 수고")
        else:
            print(f"오이{attempts}번이나걸렷누 ㅋ")
            break

if __name__ == "__main__":
    number_guessing_game()
