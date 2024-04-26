# Original list of numbers
nums = [2, 34, 32, 45, 5, 6, 43, 34]

# Storing all the odd elements using a loop
odd = []
for num in nums:
    if num % 2 == 1:
        odd.append(num)

print("Odd numbers (using loop):", odd)

# Storing all the odd elements using list comprehension
# Syntax: [expression for item in iterable if condition]
odds = [i for i in nums if i % 2 == 1]
print("Odd numbers (using list comprehension):", odds)

# 2D
# List of players and their ages
players = ['Sarafat', 'Shihab', 'Tasfi']
ages = [23, 24, 21]

# Storing combinations of players and ages using nested loops
Player_age_comb_I = []
for player in players:
    for age in ages:
        Player_age_comb_I.append([player, age])

print("Player-age combinations (using nested loops):", Player_age_comb_I)

# Storing combinations of players and ages using list comprehension
# Syntax: [expression for item1 in iterable1 for item2 in iterable2]
Player_age_comb_II = [[player, age] for player in players for age in ages] # will make the comb as list
# Player_age_comb_II = [[player, age] for player in players for age in ages] # will make the comb as tuple
print("Player-age combinations (using list comprehension):", Player_age_comb_II)

