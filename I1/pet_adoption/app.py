from flask import Flask, render_template, request

app = Flask(__name__)

# Expanded data for pets with image paths
pets = [
    {"id": 1, "name": "Buddy", "type": "dog", "activity_level": "high", "home_environment": "large", "age": "young", "allergy_friendly": "no", "image": "d1.jpeg","email":"owner1@gmail.com"},
    {"id": 2, "name": "Mittens", "type": "cat", "activity_level": "low", "home_environment": "small", "age": "adult", "allergy_friendly": "yes", "image": "c1.jpeg","email":"owner2@gmail.com"},
    {"id": 3, "name": "Goldie", "type": "fish", "activity_level": "low", "home_environment": "medium", "age": "adult", "allergy_friendly": "yes", "image": "f1.jpeg","email":"owner3@gmail.com"},
    {"id": 4, "name": "Charlie", "type": "dog", "activity_level": "medium", "home_environment": "medium", "age": "senior", "allergy_friendly": "no", "image": "d2.jpg","email":"owner4@gmail.com"},
    {"id": 5, "name": "Whiskers", "type": "cat", "activity_level": "high", "home_environment": "large", "age": "young", "allergy_friendly": "no", "image": "c2.jpeg","email":"owner5@gmail.com"},
    {"id": 6, "name": "Nemo", "type": "fish", "activity_level": "low", "home_environment": "small", "age": "young", "allergy_friendly": "yes", "image": "f2.jpeg","email":"owner6@gmail.com"},
    {"id": 7, "name": "Bella", "type": "dog", "activity_level": "high", "home_environment": "large", "age": "young", "allergy_friendly": "yes", "image": "d3.jpeg","email":"owner7@gmail.com"},
    {"id": 8, "name": "Luna", "type": "cat", "activity_level": "medium", "home_environment": "medium", "age": "adult", "allergy_friendly": "yes", "image": "c3.jpeg","email":"owner8@gmail.com"},
    {"id": 9, "name": "Bubbles", "type": "fish", "activity_level": "medium", "home_environment": "large", "age": "adult", "allergy_friendly": "no", "image": "f3.jpeg","email":"owner9@gmail.com"},
    {"id": 10, "name": "Max", "type": "dog", "activity_level": "low", "home_environment": "small", "age": "senior", "allergy_friendly": "no", "image": "d4.jpeg","email":"owner10@gmail.com"}
]

# Expanded set of questions for the quiz
questions = [
    {"question": "What type of pet are you looking for?", "key": "preferred_pet_type", "options": ["dog", "cat", "fish"]},
    {"question": "What activity level can you handle?", "key": "activity_level", "options": ["high", "medium", "low"]},
    {"question": "What is your home environment like?", "key": "home_environment", "options": ["small", "medium", "large"]},
    {"question": "Do you prefer a young or senior pet?", "key": "age", "options": ["young", "adult", "senior"]},
    {"question": "Do you need a pet that is allergy-friendly?", "key": "allergy_friendly", "options": ["yes", "no"]},
    {"question": "Do you have any other pets?", "key": "other_pets", "options": ["yes", "no"]},
    {"question": "Do you have children at home?", "key": "children_at_home", "options": ["yes", "no"]},
    {"question": "How much time can you dedicate to your pet daily?", "key": "time_dedication", "options": ["1-2 hours", "3-4 hours", "5+ hours"]},
    {"question": "Are you looking for a pet with specific training?", "key": "trained_pet", "options": ["yes", "no"]},
    {"question": "What is your experience level with pets?", "key": "experience_level", "options": ["beginner", "intermediate", "expert"]},
    {"question": "Do you have a preference for pet size?", "key": "pet_size", "options": ["small", "medium", "large"]},
    {"question": "Are you okay with a pet that requires special care?", "key": "special_care", "options": ["yes", "no"]},
    {"question": "Do you prefer a male or female pet?", "key": "pet_gender", "options": ["male", "female", "no preference"]},
    {"question": "Are you open to adopting a pet with a medical condition?", "key": "medical_condition", "options": ["yes", "no"]},
    {"question": "What is your ideal pet's personality?", "key": "pet_personality", "options": ["playful", "calm", "protective", "independent"]}
]

def match_adopter_with_pet(preferences):
    matches = []
    for pet in pets:
        score = 0
        if preferences['preferred_pet_type'] == pet['type']:
            score += 1
        if preferences['activity_level'] == pet['activity_level']:
            score += 1
        if preferences['home_environment'] == pet['home_environment']:
            score += 1
        if preferences['age'] == pet['age']:
            score += 1
        if preferences['allergy_friendly'] == pet['allergy_friendly']:
            score += 1
        matches.append((pet, score))
    # Sort by score and return top 5 matches
    matches.sort(key=lambda x: x[1], reverse=True)
    return [match[0] for match in matches[:5]]

@app.route('/')
def index():
    return render_template('index.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form
    preferences = {q['key']: data.get(q['key']) for q in questions}
    matched_pets = match_adopter_with_pet(preferences)
    return render_template('results.html', pets=matched_pets)

if __name__ == '__main__':
    app.run(debug=True)
