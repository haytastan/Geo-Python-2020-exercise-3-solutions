# Dr. Hayati TAŞTAN
# 30.08.2021

# =================
#Introducing the for loop
european_cities = ['Amsterdam', 'Brussels', 'Lisbon', 'Reykjavik'] 
for city in european_cities:
    print(city)
print('--------------------')

#for loops and the range() function
for i in range(2,9,3):
    print(i)
print('--------------------')

# Looping over the length of lists using index values
numbers = [5, 6, 7]
for i in range(len(numbers)):
    print('Value of i:', i)
    print('Value of numbers[i] before addition:', numbers[i])
    numbers[i] = numbers[i] + i
    print('Value of numbers[i] after addition:', numbers[i])
    print('')
print(numbers)
print('--------------------')

cities = ['Helsinki', 'Stockholm', 'Oslo', 'Reykjavik', 'Copenhagen']
countries = ['Finland', 'Sweden', 'Norway', 'Iceland', 'Denmark']
for i in range(len(cities)):
    print(cities[i], 'is the capital of', countries[i])
print('--------------------')

odd_numbers = [1, 3, 5]
even_numbers = [2, 4, 6]
for i in range(len(odd_numbers)):
    print(odd_numbers[i] + even_numbers[i])

