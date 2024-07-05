import random

def computer_guess():
    low = 1
    high = 100
    feedback = ""

    while feedback != "c":
        guess = random.randint(low, high)
        feedback = input(f"Computer: Is {guess} too high (H), too low (L), or correct (C): ")
        if feedback.lower() == "h":
            high = guess - 1
        elif feedback.lower() == "l":
            low = guess + 1
        else:
            print("Computer: Yay I won!")
            exit()
    
def main():
    print("Computer: Hello! My name is Bulias and I want to play guess the number with you. You pick the number and I have to guess it.")
    user_input = input("""Computer: Would you like to play?
You: """)
    if user_input.lower() == "yes":
        print("Computer: Hooray! Pick a number! I won't look.")
        computer_guess()
    else: 
        print("Computer: Alrighty :(")
        exit()

main()