# # Scope Local and Global
# enemies = 1

# def increase_enemies():
#     global enemies

#     enemies = 2
#     print(f"Increase enemies inside function {enemies}")

# increase_enemies()
# print(f"Increase enemies outside function {enemies}")

# Local Scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
# Cant print potion strength since it is local
# print(potion_strength)

# No such thing as Block scope

if 3>2:
    a_var = 10 
# var above is only within it's own function block
    
game_level = 3
def create_enemy():
    enemies = ['a', 'b', 'c']

    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)

create_enemy()

# Modify Global vars
# Avoid modifying global scopes directly
enemies = 2

def decrease_enemies():
    print(f"decrease enemies {enemies}")
    return enemies - 1

# Call the function to decrease the var, instead of changing it from it's original value!
enemies = decrease_enemies()
print(enemies)

# Global Constants - SCREAMING_SNAKECASE
PI = 3.14159
