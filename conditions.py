# if statement
temperature = 17
if temperature > 25:
    print('it is hot!')
else:
    print('it is not hot!')

weather = 'rain'
if weather == 'rain':
    print('Wear a raincoat!')
else:
    print('No raincoat needed.')

# if, elif and else
if temperature > 0:
     print(temperature, 'degrees celsius is above freezing')
elif temperature == 0:
     print(temperature, 'degrees celsius is at the freezing point')
else:
     print(temperature, 'degrees celsius is below freezing')
temperature = -3
if temperature > 0:
     print(temperature, 'degrees celsius is above freezing')
elif temperature == 0:
     print(temperature, 'degrees celsius is at the freezing point')
else:
     print(temperature, 'degrees celsius is below freezing')


yesterday = 14
today = 10
tomorrow = 13

if yesterday <= today:
    print('A')
elif today != tomorrow:
    print('B')
elif yesterday > tomorrow:
    print('C')
elif today == today:
    print('D')
    
#Combining conditions
if (1 > 0) and (-1 > 0):
     print('Both parts are true')
else:
     print('At least one part is not true')
     
if (1 < 0) or (-1 < 0):
    print('At least one test is true')
        
weather = 'rain'
wind_speed = 9

# If it is windy or raining, print "stay at home", else print "go out and enjoy the weather!"
if (weather == 'rain') or (wind_speed >= 8):
    print('Just stay at home')
else:
    print('Go out and enjoy the weather! :)')

#Combining for-loops and conditional statements
temperatures = [0, 12, 17, 28, 30]
# For each temperature, if the temperature is greater than 25, print "..is hot"
for temperature in temperatures:
    if temperature > 25:
        print(temperature, 'is hot')
    else:
        print(temperature, 'is not hot')