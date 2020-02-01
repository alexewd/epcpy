L = ['zero', 'one', 'two', 'three', 'four', 'five', 'six']
Y = []
for item in L:
	Y.append(item+'U')

print(Y)

numbers = range(10)
new_dict_for = {}

# Add values to `new_dict` using for loop
for n in numbers:
    if n%2==0:
        new_dict_for[n] = n**2

print(new_dict_for)
# Use dictionary comprehension
new_dict_comp = {n:n**2 for n in numbers if n%2 == 0}

print(new_dict_comp)
# 
# Initialize `fahrenheit` dictionary 
fahrenheit = {'t1':-30, 't2':-20, 't3':-10, 't4':0}

#Get the corresponding `celsius` values
celsius = list(map(lambda x: (float(5)/9)*(x-32), fahrenheit.values()))

#Create the `celsius` dictionary
celsius_dict = dict(zip(fahrenheit.keys(), celsius))

print(celsius_dict)
# 

# ********************
a = {'one': 1, 'two': 'to', 'three': 3.0, 'four': [4,4.0]}
print(a.keys())
print(a.values())
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# Double each value in the dictionary
double_dict1 = {k:v*2 for (k,v) in dict1.items()}
print(double_dict1)
# print(a)
# # a.clear()
# # del a # 
# # Update a dictionary
# a['one'] = 1.0 
# # 
# # Delete a single element
# del a['one'] 
# print(a)


