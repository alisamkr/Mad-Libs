import random

random_story = random.randint(0,2)
if random_story == 0:
    story_template0 = "It was about {0} {1}s ago when I arrived at the hospital in a \
    {2}. The hospital is a/an {3} place, there are a lot of {4} {5}s here. There are \
    nurses here who have {6} {7}s. If someone wants to come into my room I told them \
    that they have to {8} first. I've decorated my room with {9} {10}. Today I talked to a \
    doctor and they were wearing a {11} on their {12}. I heard that all doctors {13} {14} \
    every day for breakfast. The most {15} thing about being in the hospital is the {16} {5}!"

#asking user inputs for the first story    

    number = input("Enter a number: ")
    measure = input("Enter a measure of time: ")
    transport = input("Enter a mode of transportation: ")
    adj1 = input("Enter an adjective: " )
    adj2 = input("Enter an adjective: " )
    color = input("Enter a color: ")
    body_part = input("Enter a body part: ")
    verb = input("Enter a verb: ")
    number2 = input("Enter a number: ")
    noun = input("Enter a noun: ")
    noun2 = input("ENter a noun: ")
    noun3 = input("Enter another noun: ")
    body_part2 = input("Enter a body part: ")
    noun4 = input("Enter a noun: ")
    adj3 = input("Enter an adjective: ")
    silly_word = input("Enter a silly word: ")

    print(story_template0.format(number, measure, transport, adj1, adj2, noun, color, body_part, verb, number2, noun2, noun3, body_part2, verb, noun4, adj3, silly_word))


elif random_story == 1: 
    story_template1 = " This weekend I am going camping with {0} {1}. \
    I packed my lantern, sleeping bag, and {2}. I am so {3} {4} to {5} in a \
    tent. I am {6} {7} we might see a(n) {8}, I hear they' re kind of \
    dangerous. While we' re camping, we are going to hike, fish, and {9}. I have heard \
    that the {10} lake is great for {11}ing. Then we will {12} \
    hike through the forest for {13} {14}. If I see \
    a {9} {8} while hiking, I am going to bring it home as a pet! At \
    night we will tell {13} {15} stories and roast {16} around the campfire!"
#asking user inputs for the second story    
    noun = input("Enter a noun: ")
    name = input("Enter a noun: ")
    noun2 = input("Enter a noun: ")
    noun3 = input("Enter a noun: ")
    adj1 = input("Enter an adjective: " )
    feeling = input("Enter a feeling: ")
    verb = input("Enter a verb: ")
    adj2 = input("Enter a adjective: ")
    noun = input("Enter a noun: ")
    feeling = input("Enter a feeling: ")
    animal = input("Enter an animal: ")
    color = input("Enter a color: ")
    verb2 = input("Enter a verb: ")
    adverb = input("Enter an adverb: ")
    number = input("Enter a number: ")
    measure = input("Enter a measure of time: ")
    silly_word = input("Enter a silly word: ")
    
    print(story_template1.format(noun, name, noun2, adj1, feeling, verb, adj2, feeling, animal, verb, color, verb2, adverb, number, measure, silly_word, noun3))

elif random_story == 2:
    story_template3 = "Dear {0} {1}, I am writing to you from a {2} \
    castle in an enchanted forest. I found myself here one day after going for a ride on a \
    {3} {4} in {5}. There are {6} {7} and {8} \
    {9} here! In the {10} there is a pool full of {0}. \
    I fall asleep each night on a {11} of {12} and dream of {13} \
    {14}. It feels as though I have lived here for {0} {15}. \
    I hope one day you can visit, although the only way to get here now is {16}ing\
    on a {17} {18}!!"
#asking user inputs for the third story
    
    noun = input("Enter a noun: ")
    name = input("Enter a name: ")
    adj1 = input("Enter an adjective: ")
    color = input("Enter a color: ")
    animal = input("Enter an animal: ")
    place = input("Enter a place: ")
    adj2 = input("Enter an adjective: ")
    creature = input("Enter a magical creature: ")
    adj3 = input("Enter an adjective: ")
    creature2 = input("Enter another magical creature: ")
    room = input("Enter a room in a house: ")
    noun2 = input("Enter a noun: ")
    noun3 = input("Enter a plural noun: ")
    adj4 = input("Enter an adjective: ")
    noun4 = input("Enter a noun: ")
    measure = input("Enter a measure of time: ")
    verb = input("Enter a verb: ")
    adj5 = input("Enter an adjective: ")
    noun5 = input("Enter a noun: ")



#printing the story and replacing the numbers with corresponding indexes inside the format    
    print(story_template3.format(noun, name, adj1, color, animal, place, adj2, creature, adj3, creature2, room, noun2,\
        noun3, adj4, noun4, measure, verb, adj5, noun5 ))
