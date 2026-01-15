import random
import time

QUESTIONS: dict[str, list[tuple[int, str, list[str]]]] = { # Question set
    "Science": [
        (2, "Which planet is known as the Red Planet?", ["Venus", "Mars", "Jupiter", "Saturn"]),
        (3, "What is the chemical symbol for gold?", ["Go", "Gd", "Au", "Ag"]),
        (2, "How many bones are in the adult human body?", ["196", "206", "216", "226"]),
        (4, "What is the hardest natural substance on Earth?", ["Gold", "Iron", "Diamond", "Platinum"]),
        (1, "Which gas do plants absorb from the atmosphere?", ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"]),
        (3, "What is H2O commonly known as?", ["Hydrogen Peroxide", "Heavy Water", "Water", "Hydroxide"]),
    ],
    "History": [
        (2, "Who was the first president of the United States?", ["Thomas Jefferson", "George Washington", "Abraham Lincoln", "John Adams"]),
        (1, "In which year did World War II end?", ["1945", "1939", "1950", "1941"]),
        (3, "Which ancient civilization built the pyramids?", ["Romans", "Greeks", "Egyptians", "Mayans"]),
        (4, "Who discovered penicillin?", ["Marie Curie", "Albert Einstein", "Isaac Newton", "Alexander Fleming"]),
        (2, "Which year did the Titanic sink?", ["1905", "1912", "1920", "1898"]),
        (1, "Who painted the Mona Lisa?", ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Michelangelo"]),
    ],
    "Geography": [
        (4, "What is the largest ocean on Earth?", ["Atlantic", "Indian", "Arctic", "Pacific"]),
        (3, "Which country has the most population?", ["India", "USA", "China", "Indonesia"]),
        (2, "What is the capital of Japan?", ["Beijing", "Tokyo", "Seoul", "Bangkok"]),
        (1, "Which desert is the largest in the world?", ["Sahara", "Arabian", "Gobi", "Kalahari"]),
        (3, "Mount Everest is located in which mountain range?", ["Andes", "Rockies", "Himalayas", "Alps"]),
        (4, "Which river flows through London?", ["Thames", "Seine", "Danube", "Nile"]),
    ],
    "Movies": [
        (3, "Who directed the movie 'Inception'?", ["Steven Spielberg", "James Cameron", "Christopher Nolan", "Martin Scorsese"]),
        (4, "Which movie won Best Picture Oscar in 2020?", ["1917", "Joker", "Once Upon a Time...", "Parasite"]),
        (1, "Which actor played Iron Man in the MCU?", ["Robert Downey Jr.", "Chris Evans", "Chris Hemsworth", "Mark Ruffalo"]),
        (2, "In which year was the first Toy Story movie released?", ["1993", "1995", "1998", "2000"]),
        (4, "Which movie features the quote 'You talking to me?'", ["Scarface", "Godfather", "Goodfellas", "Taxi Driver"]),
        (1, "How many Harry Potter books are there?", ["7", "6", "8", "5"]),
    ],
    "Sports": [
        (2, "Which country won the 2018 FIFA World Cup?", ["Germany", "France", "Brazil", "Argentina"]),
        (1, "How many players are on a basketball team on the court?", ["5", "6", "7", "8"]),
        (3, "Which sport uses a shuttlecock?", ["Tennis", "Squash", "Badminton", "Table Tennis"]),
        (4, "In which city were the 2012 Summer Olympics held?", ["Beijing", "Rio", "London", "Athens"]),
        (2, "How many points is a touchdown worth in American football?", ["5", "6", "7", "8"]),
        (1, "Which country invented baseball?", ["USA", "UK", "Canada", "Japan"]),
    ],
    "Music": [
        (4, "Who is known as the 'King of Pop'?", ["Elvis Presley", "Prince", "Michael Jackson", "Madonna"]),
        (2, "Which band wrote 'Bohemian Rhapsody'?", ["The Beatles", "Queen", "Rolling Stones", "Led Zeppelin"]),
        (3, "How many strings does a standard guitar have?", ["4", "5", "6", "7"]),
        (1, "Which instrument has black and white keys?", ["Piano", "Guitar", "Violin", "Drums"]),
        (4, "Who sang 'Rolling in the Deep'?", ["Taylor Swift", "Beyonce", "Adele", "Lady Gaga"]),
        (2, "In which decade did The Beatles become famous?", ["1950s", "1960s", "1970s", "1980s"]),
    ],
    "Technology": [
        (3, "What does 'CPU' stand for?", ["Central Processing Unit", "Computer Processing Unit", "Central Processor Unit", "Computer Processor Unit"]),
        (1, "Which company created the iPhone?", ["Apple", "Samsung", "Google", "Microsoft"]),
        (4, "What year was Google founded?", ["1995", "1997", "1996", "1998"]),
        (2, "What does 'HTTP' stand for?", ["Hyper Transfer Text Protocol", "Hypertext Transfer Protocol", "Hyper Text Transfer Process", "Hyper Transfer Text Process"]),
        (3, "Which programming language is known for web development?", ["C++", "Java", "JavaScript", "Python"]),
        (1, "How many bits are in a byte?", ["8", "4", "16", "32"]),
    ],
    "General Knowledge": [
        (2, "How many colors are in a rainbow?", ["6", "7", "8", "5"]),
        (4, "Which animal is known as the 'ship of the desert'?", ["Horse", "Elephant", "Llama", "Camel"]),
        (1, "What is the fastest land animal?", ["Cheetah", "Lion", "Gazelle", "Horse"]),
        (3, "How many continents are there?", ["5", "6", "7", "8"]),
        (2, "Which fruit is associated with Isaac Newton?", ["Orange", "Apple", "Pear", "Banana"]),
        (4, "What is the smallest country in the world?", ["Monaco", "San Marino", "Liechtenstein", "Vatican City"]),
    ]
}

def border(): # Function to draw an ASCII line of specified width
    print("=" * 50)

def show_question(category, q_num, total_q, score, streak): # Function to display a question and then list the options
    correct, text, options = QUESTIONS[category][q_num]
    
    border()
    print(f"{category} - Question {q_num+1}/{total_q}") # Display category and question number
    print(f"Score: {score} | Streak: {streak}") # Display current score and streak
    border()
    print(text)
    border()
    
    for i, opt in enumerate(options, 1): # List the options
        print(f"{i}. {opt}")
    
    return correct, options

def ask_question(category, q_num, total_q, score, streak): # Function to handle asking a question and processing the answer
    correct, options = show_question(category, q_num, total_q, score, streak) # Show the question
    
    start_time = time.time()
    time_limit = 15
    
    while True: # Loop until valid answer or time runs out
        elapsed = time.time() - start_time
        time_left = max(0, time_limit - elapsed)
        
        if time_left <= 0: # Time's up
            print("\nTime's up!")
            return score, 0, False
        
        print(f"\nTime left: {int(time_left)} seconds")
        print("Your answer (1-4), or press Enter to see timer: ", end="")
        
        try:
            ans = input() # Get user input
            if ans in ["1", "2", "3", "4"]:
                answer = int(ans)
                break
        except:
            pass
    
    if answer == correct: # Correct answer
        streak += 1
        points = 10 + min(streak, 5)
        score += points
        print(f"\nCorrect! +{points} points")
        print(f"Streak: {streak} {'*' * min(streak, 5)}")
        return score, streak, True
    else: # Wrong answer
        print(f"\nWrong! Correct: {correct}. {options[correct-1]}")
        return score, 0, False

def classic_mode(): # Classic mode function
    score = 0
    streak = 0
    total_q = 10  # Now 10 questions
    
    for i in range(total_q): # Loop through 10 questions
        category = random.choice(list(QUESTIONS.keys()))
        q_num = random.randint(0, len(QUESTIONS[category])-1)
        
        score, streak, _ = ask_question(category, q_num, total_q, score, streak)
    
    print(f"\n{border()}")
    print(f"GAME OVER! Final Score: {score}")
    print(border())
    return score

def timed_mode(): # Timed mode function
    score = 0
    streak = 0
    questions = 0
    end_time = time.time() + 90  # 90 seconds now
    
    while time.time() < end_time: # Loop until time runs out
        time_left = int(end_time - time.time())
        if questions > 0:  # Don't print on first question
            print(f"\nTime left: {time_left}s | Score: {score} | Questions: {questions}")
        
        category = random.choice(list(QUESTIONS.keys())) # Random category
        q_num = random.randint(0, len(QUESTIONS[category])-1) # Random question number
        
        score, streak, _ = ask_question(category, q_num, 999, score, streak)
        questions += 1
        
        if time.time() >= end_time: # Check if time's up
            break
    
    print(f"\n{border()}")
    print(f"TIME'S UP! Final Score: {score} | Questions: {questions}")
    print(border())
    return score

def survival_mode(): # Survival mode function
    score = 0
    streak = 0
    lives = 3
    questions = 0
    
    while lives > 0: # Loop until no lives left
        category = random.choice(list(QUESTIONS.keys())) # Random category
        q_num = random.randint(0, len(QUESTIONS[category])-1) # Random question number
        
        score, streak, correct = ask_question(category, q_num, 999, score, streak)
        questions += 1
        
        if not correct: # Wrong answer
            lives -= 1
            if lives > 0:
                print(f"\nYou lost a life! {lives} lives remaining")
    
    print(f"\n{border()}")
    print(f"GAME OVER! Final Score: {score} | Questions: {questions}")
    print(border())
    return score

def category_mode(): # Category mode function
    score = 0
    streak = 0
    
    print("\nAvailable categories:")
    categories = list(QUESTIONS.keys())
    for i, cat in enumerate(categories, 1): # List categories
        print(f"{i}. {cat} ({len(QUESTIONS[cat])} questions)")
    
    try: # Get user choice
        choice = int(input("\nChoose category number: ")) - 1
        if 0 <= choice < len(categories): # Valid choice
            category = categories[choice] # Selected category
            total_q = len(QUESTIONS[category]) # Total questions in category
            
            print(f"\nPlaying {category} category ({total_q} questions)")
            
            for q_num in range(total_q): # Loop through all questions in category
                score, streak, _ = ask_question(category, q_num, total_q, score, streak)
            
            print(f"\n{border()}")
            print(f"{category.upper()} COMPLETE! Final Score: {score}")
            print(border())
        else:
            print("Invalid choice!")
    except:
        print("Invalid input!")

def main(): # Main function to run the trivia game
    while True:
        border()
        print("TRIVIA CHALLENGE".center(50))
        border()
        
        print("\n1. Classic Mode (10 questions)")
        print("2. Timed Challenge (90 seconds)")
        print("3. Survival Mode (3 lives)")
        print("4. Category Mode (pick a category)")
        print("5. Exit")
        
        choice = input("\nChoose mode (1-5): ").strip()
        
         # Handle user choice
        if choice == "1":
            classic_mode()
        elif choice == "2":
            timed_mode()
        elif choice == "3":
            survival_mode()
        elif choice == "4":
            category_mode()
        elif choice == "5":
            print("\nThanks for playing!")
            break
        else:
            print("Invalid choice!")
        
        if choice in ["1", "2", "3", "4"]: # Ask to play again
            play = input("\nPlay again? (y/n): ").lower()
            if play != 'y':
                print("\nThanks for playing!")
                break

main()
