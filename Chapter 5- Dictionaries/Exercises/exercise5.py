pets = []

pet = {"animal type":"python","name":"john","owner":"waleed","weigh":"55","eats":"bugs",}
pets.append(pet)

pet = {"animal type":"chicken","name":"clarence","owner":"umer","weight":"5","eats":"seeds",}
pets.append(pet)

pet = {"animal type":"dog","name":"peso","owner":"abdullah","weight":"37","eats":"shoes",}
pets.append(pet)

for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")