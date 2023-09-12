"""
Namespaces: Local Vs Global Scope
"""

enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope
def drink_potion():
    potion_strength = 100
    print(f"potion strength: {potion_strength}")
    
""" 
NameError: name 'potion_strength' is not defined
print(f"potion strength: {potion_strength}")
""" 

#Global Scope

player_health = 100

def game():
    def drink_potion1():
        potion_strength = 10
        print(f"Player health: {player_health}")

    drink_potion1()
    
    
print(f"Player health: {player_health}")