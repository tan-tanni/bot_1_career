
import math
from flask import Flask, render_template, request, redirect, url_for

import matplotlib.pyplot as plt
# import install matplotlib.pyplot as plt 

app = Flask(__name__)

with open ('questions.json', 'r', encoding = 'uft-8') as f:

professions = { "Psychologist": "Working with people's emotions and behavior, helping to solve personal problems",
"Programmer": "Creating and developing software, working with code.  Information technology (IT) software development, systems analysis, cybersecurity, etc. ",
"Designer":  "Fashion, animation, video and audio production, interior design, clothing, urban environment and even  applications app",
"Journalist": "Searching for and covering events, creating articles and reports Journalism and media content creation, news reporting, blogging, PR..",
"Teacher": "Teaching children or adults, developing educational materials. Education and pedagogy teaching, upbringing, organizing the educational process.",
"Actor": "Creating an artistic image, participating in plays and films. graphic design, fashion, animation, video and audio production.",
"Business Trainer": "Training and developing skills of company employees", 
"Ecologist": "Studying and preserving the natural environment. Finance and banking managing capital, investments, accounting, corporate finances.", 
"Agronomist": "Growing plants, caring for soil and . Agriculture and farming growing plants, raising animals, processing products.", 
"Doctor": "Treating patients, diagnosing diseases. Medicine and healthcare treatment, diagnostics, pharmaceuticals, psychology.",
"SalesManager": "Developing a client base, concluding deals. Marketing and advertising promoting goods and services, working with a brand, digital marketing.", 
"Lyer": "Legal protection of interests, drafting contracts. Jurisprudence legal protection, consulting, litigation.", 
"Artist": "You are a creative person, so create) Creating paintings, graphics, writer. Design and creative industries graphic design, fashion, animation, video and audio production.", 
"Engineer": "Designing and creating technical devices. Manufacturing and engineering industrial production, automation, mechanical engineering.", 
"Marketer": "Promotion of goods and services, market analysis",
"Tourism" : "Tourism and hospitality  travel organization, work in hotels, excursion services."
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

    # Clarifying que. for "extrovert + humanities"
    {
        'text': 'What role do you want to play in the project?',
        'options': ['Host', 'Writer', 'Organizer'],
        'type': ['extro', 'human'],
        'mapping': {
        'Host': 'Actor',
        'Writer': 'Journalist',
        'Organizer': 'Business coach'}
    },
    {
        'text': 'What do you find more interesting to read?',
        'options': ['Novels', 'Biographies', 'Fashion magazines'],
        'type': ['extro', 'human'],
        'mapping': {'Novels': 'Writer',
        'Biographies': 'Journalist',
        'Fashion Magazines': 'Designer'
        }
    }, 
    {
        'text': 'What do you like to read?',
        'options': ['Novels', 'Biographies', 'Fashion magazines'],
        'type': ['extro', 'human'],
        'mapping': {
        'Novels': 'Writer',
        'Biographies': 'Journalist',
        'Fashion magazines': 'Interface designer'
    }
    },

    # que "extrovert + techie"
    {
        'text': 'Which tool do you prefer?',
        'options': ['Book', 'Hammer', 'Laptop'],
        'type': ['extro', 'tech'],
        'mapping': {
        'Book': 'Manager sales',
        'Hammer': 'Engineer',
        'Laptop': 'Programmer'
        }
    },
    {
        'text': 'Which tool do you prefer?',
        'options': ['Hammer', 'Computer', 'Microscope'],
        'type': ['intro', 'tech'],
        'mapping': {
        'Hammer': 'Engineer',
        'Computer': 'Programmer',
        'Microscope': 'Ecologist' , 'Agronomist'}
    },
        # Clarifying questions for "introvert + techie"
    {
        'text': 'What would you do with pleasure?',
        'options': ['Create a diagram', 'Command and other', 'Study the documentation'],
        'type': ['intro', 'tech'],
        'mapping': {
        'Create a diagram': 'Engineer',
        'Command and other': 'Business Trainer',
        'Study the documentation': 'Programmer'
        }
    },
    {
        'text' : 'What gives you strength? Choose one option that is closer to you:'
        'options': ['When I solve a difficult problem',
        'When I help someone understand themselves', 'When I create something new',
        'When I feel stability and control',
        'When I am appreciated and accepted'],
        'mapping': [
        'When I solve a difficult problem': 'Engineer'and 'Ecologist',
        'When I help someone understand themselves': 'Psychologist' and 'Teacher',
        'When I create something new': 'Artist' and 'Designer',
        'When I feel stability and control': 'Lyer',
        'When I am appreciated and accepted': 'Tourism' and 'Agronomist'
        ]
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


if __name__ == '__main__':
    app.run(debug = True)

'''
d
    '''