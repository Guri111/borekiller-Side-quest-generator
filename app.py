import random

mind = [
    {
        "title": "Smart one",
        "about": "Study for 30 minutes without interruption and with your phone in another room",
        "difficulty": "easy",
        "xp": 5
    },
    {
        "title": "Chess boss",
        "about": "Play chess online until you win a game",
        "difficulty": "easy",
        "xp": 5
    },
        {
        "title": "The smartest on the room",
        "about": "Read 15 pages of any book and take note about them",
        "difficulty": "mid",
        "xp": 10
    },
    {
        "title": "Rubik cube",
        "about": "Learn how to solve a rubik cube and solve one",
        "difficulty": "hard",
        "xp":15
    }
]
body = [
    {
        "title": "Push-ups",
        "about": "Do as many push-ups as you can in the next 10 minutes",
        "difficulty": "mid",
        "xp": 10
    },
    {
        "title": "Lil gymnast",
        "about": "Put on some music, do stretching exercises until 3 songs have played.",
        "difficulty": "easy",
        "xp": 5
    }
]
social = [
    {
        "title": "Fast not furious",
        "about": "Go for a walk and give a compliment to at least 5 people",
        "difficulty": "mid",
        "xp": 10
    },
    {
        "title": "Local heroe",
        "about": "Learn the name of a cashier you see frequently.",
        "difficulty": "easy",
        "xp": 5
    }
]
mindeasyones = []
mindmidones = []
mindhardones = []
all_quests= mind+body+social

print("Today you feel like:")

while True:
    
        answer = input("Mind (1), Body (2), Social (3), Random(4) o q para salir:")
        if answer == "q":
            break
    #mind answers
        if answer == "1":
            difchoice = input("Easy (1), Mid(2), Hard(3), Exit(q): ")
            if difchoice == "q":
                break
            
            elif difchoice == "1":
                diff="easy"
            elif difchoice == "2":
                diff="mid"
            elif difchoice == "3":
                diff="hard"
            else:
                print("No my friend")
                continue
    #filter so user can choose between easy mid and hard quests:
            filteredquests = []
            for quest in mind:
                if quest["difficulty"]== diff:
                    filteredquests.append(quest)
                    
            random_choice = random.choice(filteredquests)
            
            print(f"- {random_choice['title']}")
            print(f"about: {random_choice['about']}")
            print(f"xp: {random_choice['xp']}")
            print("----")
        #TERMINAR DE AÑADIR FILTRO DE DIFICULTAD AL RESTO DE MISIONES, AÑADIR QUE TE PERMITA DECIR SI HAS TERMINADO O NO
        #LA MISION Y SI LA HAS TERMINADO TE AÑADE LA XP CORRESPONDIENTE
        
        
        #    random_choice = random.choice(mind)
        #    print("- "+random_choice["title"])
        #    print(" "+random_choice["about"])
        #    print("----")
        #if answer == "2":
        #    random_choice = random.choice(body)
        #    print("- "+random_choice["title"])
        #    print("  "+random_choice["about"])
        #    print("----")
        #if answer == "3":
        #    random_choice = random.choice(social)
        #    print("- "+random_choice["title"])
        #    print(" "+random_choice["about"])
        #    print("----")
        #if answer == "4":
        #    random_choice = random.choice(all_quests)
        #    print("- "+random_choice["title"])
        #    print(" "+random_choice["about"]) """