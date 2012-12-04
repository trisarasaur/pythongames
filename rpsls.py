import random

def number_to_name(number):
    values = ['rock', 'Spock', 'paper', 'lizard', 'scissors']
    return values[number]

    
def name_to_number(name):
    values = ['rock', 'Spock', 'paper', 'lizard', 'scissors']
    #{rock : 0, Spock : 1, paper : 2, lizard : 3, scissors : 4} 
    i = 0
    for item in values:
        if item == name:
    		return i
    	i += 1



def rpsls(guess): 
    player_number = name_to_number(guess)
    comp_number = random.randrange(4)
    difference = (player_number - comp_number)%5
    
    print "Player chooses " + guess
    print "Computer chooses " + str(number_to_name(comp_number))

    if difference == 0:
        print "Player and Computer tie!"
    elif difference == 1 or difference == 2:
        print "Player wins!"
    else: 
        print "Computer wins!"

    print ''
    return 

# print number_to_name(3)
# print name_to_number("Spock")


rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
