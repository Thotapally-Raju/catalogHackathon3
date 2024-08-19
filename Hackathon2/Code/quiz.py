import random
statesAndCapitals = {
    'Andhra Pradesh': 'Amaravati',
    'Arunachal Pradesh': 'Itanagar',
    'Assam': 'Dispur',
    'Bihar': 'Patna',
    'Chhattisgarh': 'Raipur',
    'Goa': 'Panaji',
    'Gujarat': 'Gandhinagar',
    'Haryana': 'Chandigarh',
    'Himachal Pradesh': 'Shimla',
    'Jharkhand': 'Ranchi',
    'Karnataka': 'Bengaluru',
    'Kerala': 'Thiruvananthapuram',
    'Madhya Pradesh': 'Bhopal',
    'Maharashtra': 'Mumbai',
    'Manipur': 'Imphal',
    'Meghalaya': 'Shillong',
    'Mizoram': 'Aizawl',
    'Nagaland': 'Kohima',
    'Odisha': 'Bhubaneswar',
    'Punjab': 'Chandigarh',
    'Rajasthan': 'Jaipur',
    'Sikkim': 'Gangtok',
    'Tamil Nadu': 'Chennai',
    'Telangana': 'Hyderabad',
    'Tripura': 'Agartala',
    'Uttar Pradesh': 'Lucknow',
    'Uttarakhand': 'Dehradun',
    'West Bengal': 'Kolkata'
}
def getQuestionWithOptions():
    state = random.choice(list(statesAndCapitals.keys()))
    correctCapital = statesAndCapitals[state]
    allCapitals = list(set(statesAndCapitals.values()) - {correctCapital})
    incorrectCapitals = random.sample(allCapitals, 3)
    options = incorrectCapitals + [correctCapital]
    random.shuffle(options)
    return state, correctCapital, options
def runQuiz():
    name=input("Enter your Name : ")
    
    
    start=int(input("Enter 1 to start Quiz : "))
    if(start!=1):
        print("Ignored to start quiz")
        return
    score = 0
    numQuestions = 5 
    for _ in range(numQuestions):
        state, correctCapital, options = getQuestionWithOptions()
        print(f"What is the capital of {state}?")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        try:
            answerIndex = int(input("Choose the correct option (1-4): "))
            if options[answerIndex - 1].lower() == correctCapital.lower():
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is {correctCapital}.")
        except (IndexError, ValueError):
            print("Invalid option! Please choose a number between 1 and 4.")
    
    print(f"Hi there {name } Your final score is {score}/{numQuestions}.")
runQuiz()
