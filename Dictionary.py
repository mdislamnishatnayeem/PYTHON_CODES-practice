
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
