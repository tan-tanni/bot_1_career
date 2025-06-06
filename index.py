
import math

import matplotlib.pyplot as plt
# import install matplotlib.pyplot as plt 

professions = { "Psychologist": "Working with people's emotions and behavior, helping to solve personal problems",
"Programmer": "Creating and developing software, working with code",
"Designer":  "Interior design, clothing, urban environment and even  applications app",
"Journalist": "Searching for and covering events, creating articles and reports",
"Teacher": "Teaching children or adults, developing educational materials",
"Actor": "Creating an artistic image, participating in plays and films",
"Business Trainer": "Training and developing skills of company employees", "Ecologist": "Studying and preserving the natural environment", 
"Agronomist": "Growing plants, caring for soil and climate", "Doctor": "Treating patients, diagnosing diseases","SalesManager": "Developing a client base, concluding deals", "Lyer": "Legal protection of interests, drafting contracts",  "Artist": "Creating paintings, graphics, illustrations", "Engineer": "Designing and creating technical devices and systems", "Marketer": "Promotion of goods and services, market analysis"

}

scores = {p: 0 for p in professions}

questions = [
    {
        'text': 'choose a more comfortable place for you',
        'options': ['concert hall', 'quiet empty room', 'small company in nature'],
        'mapping': {'concert hall': 'extro', 'quiet empty room':'intro', 'small company in nature':'ambi'}
    },

    {   
        'text': "what kind of vacation will you choose?",
        'options': ['party with friends(you have them 0_0)', 'reading at home or walking the dog', 'walking with a friend'],
        'mapping'; {'party with friends(you have them 0_0)'; 'extro', 'reading at home or walking the dog': 'intro',
        'walkinfrieng with a d': 'ambi'}
    },

    # humanities or techie or natural sciences
    {   'text': 'Which subject is easier for you?',
        'options': ['history', 'physics', 'biology', 'geomertia', 'languages'],
        'mapping': {'history': 'human', 'physics':'tech', 'biology': 'natural', 'geomertia':'tech', 'languages':'human'}, 
    },
    {   'text':'choose what interests you more',
        'options': ['know how everything works', 'how to create something beautiful and unique', 'how to make money', 'how to help people and the world']
        'mapping': {'know how everything works': 'Engineer' and 'Journalist'}
        'how to create something beautiful and unique': 'Actor' and 
        'how to make money':'Business Trainer' and 'SalesManager'
        'how to help people and the worl':'Lyer' and 'Psychologist'
    }
]


#diogram
def show_results(scores):
    result = {k: v for k, v in scores.items() if v > 0}
    sorted_result = dict(sorted(result.items(), key = lambda x: x[1], reverse = True))

    print("Your results:")
    for profession, score in sorted_result.items():
        print(f"{profession} - {score} points")
        print("  ", professions[profession])

    plt.figure(figsize = (10, 6))
    plt.barh(list(sorted_result.keys()),list(sorted_result.values()))
    plt.tittle(' your proffesions')
    plt.xlabel('points')
    plt.grid(axis ='x', linestyle = '--')
    plt.tight_layout()
    plt.show()


# main funktion test
def run_test():
    history = []
    index = 0
    current_type = None
    
    while index < len (questions):
        q = questions[index]
        print(f"\n{q['text']}")
        for i, opt in enumerate(q['options'], 1):
            print(f"{i}. {opt}")

        print("b. return to previous question")

        choise = input("Choose  the most suitable option")

        if choise =='b':
            if history:
                history.pop()
                index -= 1
                if index < 0:
                    index = 0
                continue
            else:
                print("there is no way to return.")
                continue

        try:
            choise_idx = int(choise) - 1
            selected = q['options'] [choise_idx]
        except (ValueError, IndexError):
            print("incorrect choice.")
            continue

        # save
        mapping = q.get('mapping', {})
        if not hasattr(mapping, 'items'):
            print("error in data")
            continue

        category = mapping[selected]
        if isinstance(category, str) and category in ['intro', 'extro','ambi', 'natural','human', 'tech']:
            current_type = [category] if 'type' not in q else q ['type']
        elif isinstance (category, str):
            scores[category] += 1
        elif isinstance(category, dict):
            pass #mass questions

        history.append(selected)
        index += 1

    show_results(scores)
run_test()



'''

def  main:
    qwestions()
    show_results()
    '''