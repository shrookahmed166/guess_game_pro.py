import random
import time

print("="*40)
print("    WELCOME TO THE GUESSING GAME!")
print("           FOR KIDS 8-12 YEARS")
print("="*40)
time.sleep(1)

secret_number = random.randint(1, 20)  # 
tries = 5  # 
score = 0

print(f"\nI have a secret number between 1 and 20")
print(f"You have {tries} tries to guess it!")
print("---------------------------------------")

for attempt in range(1, tries + 1):
    try:
        guess = int(input(f"\nTry {attempt}/{tries}: Enter your guess: "))
    except:
        print("Please enter a number only!")
        continue

    if guess == secret_number:
        score = (tries - attempt + 1) * 20  # 
        print(f"\n🎉 CONGRATULATIONS! YOU WON! 🎉")
        print(f"Your Score: {score} points")
        break
    elif guess < secret_number:
        print("📈 Too Low! Try a BIGGER number")
    else:
        print("📉 Too High! Try a SMALLER number")
    
    tries_left = tries - attempt
    if tries_left > 0:
        print(f"You have {tries_left} tries left")
else:
    print(f"\n😢 GAME OVER!")
    print(f"The secret number was: {secret_number}")

print("\nThanks for playing!")
print("="*40)