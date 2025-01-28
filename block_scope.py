game_level=3
enemies=["skeleton","zombies","aliens"]

if game_level<5:
    new_enemy=enemies[0]
print(new_enemy)#if we want to print without and indentation here it will not give an error

#but if 
def create_enemy():
    if game_level<5:
        new_enemy=enemies[0]
    print(new_enemy)
#print(new_enemy)#it will give an error

#if you create a variable within a function it will only available within that fuction



        
