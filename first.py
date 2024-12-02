list1 = [1, 4, 6, 8, 4, 3, 6]

list1.append(7)
popped = list1.pop(-2)
print(popped)
print(list1)
# for item in list1:
#     print(item)

# set1 = {1, 4, 6, 8, 4, 3, 6} #Removes duplicates
set1 = set(list1)
print(set1)

list2 = list(set1)
print(list2)

# print(set1[2]) #impossible

for item in set1:
    print(item)

dict1 = {'K': 'Katherine', 'L': 'Liri', 4: 'Daniel', 2: 123}

#print(dict1['k']) #Error
print(dict1['L'])
print(dict1[4])
print(dict1[2])

print(dict1)

for key in dict1:
    print(key, dict1[key])

d1k = dict1.keys()
print(d1k)
d1v = dict1.values()
print(d1v)
d1kl = list(d1k)
print(d1kl)
d1vl = list(d1v)
print(d1vl)

dict1[6] = 456

print(dict1)

tp1 = (1, 2, 3)
tp2 = ()

str1 = "Hello, World!"
print(str1)

str1 += "\nHello back"
print(str1)
# for char in str1:
#     print(char)
#
# print(str1[5])

str1[-4].upper()

str1 = str1[:-4] + str1[-4].upper() + str1[-3:]

print(str1)
s_count = str1.count('s')
print(s_count)

print("I am out of ideas")
# s_index = str1.index('s')
