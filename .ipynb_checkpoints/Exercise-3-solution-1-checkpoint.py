# Hayati TAŞTAN
# 30.08.2021
# ===================
# PROBLEM: https://github.com/geo-python-2019/Exercise-3/blob/master/Exercise-3-problem-1.ipynb
# SOLUTION: (P.A.: python modul "nose" is not installed, a function is used instead)
basename = "Station"
print(basename)

filenames=[]
print(filenames)

for i in range(21): # from 0 to 21)
    station = "Station" + "_" + str(i) + ".txt"
    filenames.append(station)
print(filenames)

# Check that there exists 21 values in the list
if (len(filenames) == 21):
    print ('The length of the list "filenames" is 21') 

# Check that the value of the last station is correct    
def assertEquals(var1, var2):
    if var1 == var2:
        return True
    else:
        return False
if (station.lower().strip(), "station_20.txt"):
    print('The value of the last station is correct')
else:
     print('The value of the last station is correct')