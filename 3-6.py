math = list()
total = 0
avg=0
n = input('How many people in this class?')
n = int(n)
for i in range(n):
    name = input('Please input the name:')
    score = input('Please input the score:')
    score = int(score)
    oneperson = list()
    oneperson.append(name)
    oneperson.append(score)
    math.append(oneperson)
for item in math:
    total = total+item[1]
high = 0
person=''
for item in math:
    if item[1]>high:
        high=item[1]
        person=item[0]
print(person, "got the highest score", high)
low = 100
peerson=''
for item in math:
    if item[1]<low:
        low=item[1]
        person=item[0]
print(person,"got the lowest score", low)