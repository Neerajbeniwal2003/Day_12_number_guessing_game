#NAMESPACES:-
#Local scope
#suppose we have a function 
def drink_portion():
    portion_strength=2 #this is local variable
    print(portion_strength)
#if we call the function
drink_portion()
#and if we want to print the variable thet is inside the function
# print(portion_strength) #it will give an error

# the only difference between the local and the global scope that how we defined our function
 
#Global scope
player_health=10  #this is global variable

def drink_portion():
    portion_strength=2 #this is local variable
    print(player_health)
drink_portion()

#if we define a function in another function
def game():
    def drink_portion():# now this is the local fuction in the game function
        portion_strength=2 #this is local variable
        print(player_health)
    drink_portion() #now this will be right
# drink_portion()#it will not see in the game function this is wrong

#how to modify variable with global scope
enemies=1
player_health=10  #this is global variable

# def drink_portion():
#     """this is not use so often because this is bit confusing and error prone"""
#     global enemies #using this to modify global variable
#     enemies+=1
#     print(enemies)
# drink_portion()

#Or we can modify it by other way
def drink_portion(enemy):
    return enemy + 1
print(drink_portion(enemies))


#Global constants
"""global scope is very usefull specially if u define constants"""
"""global constant are variable that is defined to never modify ever again"""
PI=3.14
GOOGLE_URL="www.google.com"

def my_func():
    print(GOOGLE_URL)
my_func()
    


