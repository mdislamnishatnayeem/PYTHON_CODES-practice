
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
