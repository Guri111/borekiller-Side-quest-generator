import random

mind = [
    {
        "title": "🧠Smart one",
        "about": "Study for 30 minutes without interruption and with your phone in another room",
        "difficulty": "easy"
    },
    {
        "title": "♖ Chess boss",
        "about": "Play chess online until you win a game",
        "difficulty": "easy"
    },
        {
        "title": "🧠The smartest on the room",
        "about": "Read 15 pages of any book and take note about them",
        "difficulty": "mid"
    },
    {
        "title": "🔴🟢🔵⚪ Rubik cube",
        "about": "Learn how to solve a rubik cube and solve one",
        "difficulty": "hard"
    }
]
body = [
    {
        "title": " 💪Push-ups",
        "about": "Do as many push-ups as you can in the next 10 minutes",
        "difficulty": "mid"
    },
    {
        "title": " 💪Lil gymnast",
        "about": "Put on some music, do stretching exercises until 3 songs have played.",
        "difficulty": "easy"
    }
]
social = [
    {
        "title": "🚗Fast not furious",
        "about": "Go for a walk and give a compliment to at least 5 people",
        "difficulty": "mid"
    },
    {
        "title": "😇Local heroe",
        "about": "Learn the name of a cashier you see frequently.",
        "difficulty": "easy"
    }
]
all_quests= mind+body+social

def fileteredquestsget(quests, diff):
    filteredquests = []
    for quest in quests:
        if quest["difficulty"]== diff:
            filteredquests.append(quest)
    return(filteredquests)
def printrandomquest(quests,diff):
    filteredall = fileteredquestsget(quests, diff)
    
    if not filteredall:
        print("There is not quests available")
        return
    Rchoice = random.choice(filteredall)
    print("   ")
    print(f" {Rchoice['title']}")
    print(f"About: {Rchoice['about']}")
    print("----")
    print("    ")

print("Today you feel like:")

while True:
    
                answer = input("🧠Mind (1), 💪Body (2), 🤝Social (3), 🎲Random(4) o q para salir:")
                if answer == "q":
                    break
                elif answer == "1":
                    choosenlist = mind
                    
                elif answer == "2":
                    choosenlist = body
                    
                elif answer == "3":
                    choosenlist = social
                elif answer == "4":
                    therandomchoice = random.choice(all_quests)
                    print("    ")
                    print(f" {therandomchoice['title']}")
                    print(f"About: {therandomchoice['about']}")
                    print("----")
                    print("    ")
                    continue
                difficultychoice = input("Choose a difficulty: 🟢Easy(1), 🟡Mid(2), 🔴Hard(3)")
                
                if difficultychoice == "1":
                    diff = "easy"
                    
                elif difficultychoice == "2":
                    diff = "mid"
                elif difficultychoice == "3":
                    diff = "hard"
                else:
                    print("Invalid difficulty, choose another one")
                    continue
                printrandomquest(choosenlist, diff)