
my_dict=dict({1:'apple', 2:'ball'})
print(my_dict)
my_dict=dict([(1,'apple'),(2,'ball')])
print(my_dict)
my_result={'bangla':98,'Math':99,'English':88}
print(my_result)

#get keywork টি ব্যবহার করে Math key এর ভ্যালু বের করছি।
print(my_result.get('Math'))

#pop keyword use kore English key take soray ba remove jore dici.Keywork deletemane value o gayeb ba reomove.
print(my_result.pop('English'))
print(my_result)
# popitem diye random item remove korchi ami nijeo jani na konta remove hoye jabe
print(my_result.popitem())
print(my_result)



person={'name':'Masud Alam','age':22,'Salary':3500.0}
print(person.keys())
print(person.items())

squares={1:1,2:4,3:9,4:16,5:25}
print(squares.clear())
del squares
print(squares)


keys={'a','e','i','o','u'}
vowels=dict.fromkeys(keys)
print(vowels)




squares={}
for i in range(6):
	squares[i]=i*i
print(squares)

squares={i:i*i for i in range(100)}
print(squares)

squares={i:i*i for i in range(100) if(i%2==1)}
print(squares)



squares={1:1,3:9,5:25,7:49,9:81}
print(1 in squares)
print(2 not in squares)

for i in squares:
	print(squares[i])
print(len(squares))
print(sorted(squares))






people = {1: {'name': 'Borhan', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Nahida', 'age': '22', 'sex': 'Female'}}
 
print(people)

people = {1: {'name': 'Borhan', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Nahida', 'age': '22', 'sex': 'Female'}}
 
print(people[1]['name'])
print(people[1]['age'])
print(people[1]['sex'])


people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}
 
people[3] = {}
 
people[3]['name'] = 'Farhana'
people[3]['age'] = '24'
people[3]['sex'] = 'Female'
people[3]['married'] = 'No'



people = {1: {'name': 'Borhan', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Moumita', 'age': '22', 'sex': 'Female'},
          3: {'name': 'Farhana', 'age': '24', 'sex': 'Female', 'married': 'No'}}
 
people[4] = {'name': 'Polash', 'age': '29', 'sex': 'Male', 'married': 'Yes'}
print(people[4])



people = {1: {'name': 'Borhan', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Farhana', 'age': '22', 'sex': 'Female'},
          3: {'name': 'Moumita', 'age': '24', 'sex': 'Female', 'married': 'No'},
          4: {'name': 'Polash', 'age': '29', 'sex': 'Male', 'married': 'Yes'}}
 
del people[3]['married']
del people[4]['married']
 
print(people[3])
print(people[4])



people = {1: {'name': 'Borhan', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Farhana', 'age': '22', 'sex': 'Female'},
          3: {'name': 'Moumita', 'age': '24', 'sex': 'Female'},
          4: {'name': 'Peter', 'age': '29', 'sex': 'Male'}}
 
del people[3], people[4]
print(people)





people = {1: {'Name': 'Jahir', 'Age': '27', 'Sex': 'Male'},
          2: {'Name': 'Moumita', 'Age': '22', 'Sex': 'Female'}}
 
for p_id, p_info in people.items():
    print("\nPerson ID:", p_id)
     
    for key in p_info:
    	print(key+':',p_info[key])
    	
a={3:45,6:677,6:78}
print(a.items())
