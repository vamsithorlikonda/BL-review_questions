import random



def play_guessing_game():

    while True:

        try:

            min_value = int(input('Enter the minimum number: '))

            max_value = int(input('Enter the maximum number: '))



            if max_value > min_value:

                break

            else:

                print('The maximum number should be greater than the minimum number.')

                

        except ValueError:

            print('Please enter valid integers.')

    

    target_number = random.randint(min_value, max_value)

    print('Try to guess the number!')



    attempt_count = 0

    max_tries = 10  



    while attempt_count < max_tries:

        try:

            player_guess = int(input(f'Enter your guess ({min_value} - {max_value}): '))

            attempt_count += 1

        

            if player_guess < target_number:

                print('Too low! Try again.')

                

            elif player_guess > target_number:

                print('Too high! Try again.')

                

            else:

                print(f'Great job! You guessed the number {target_number} in {attempt_count} attempts.')

                break

                

        except ValueError:

            print('Invalid input! Please enter an integer.')

    else:     

        print(f'Out of attempts! The correct number was {target_number}.')

       

play_guessing_game()
