x = 100
print(isinstance(x, int))
True
y = 100.9
print
<built-in function print>
print(isinstance(y, int))
False
z = 1.002
print(isinstance(x, float))
False
z=1.003
print
<built-in function print>
print(isinstance(z, float))
True
print(isinstance(y, int))
False
student id = 14459
SyntaxError: invalid syntax
student_id = 14459
print(isinstance(student_id, float))
False
class_id = 1.0459
print(isinstance(class_id, int))
False
print(isinstance(student_id, int))
True
print(isinstance(class_id, float))
True
work_id = -1.4459
print(isinstance(work_id, int))
False
print(isinstance(work_id, float))
True
country_id = 0.11594
print(isinstance(country_id, float))
True
food_id = pizza
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    food_id = pizza
NameError: name 'pizza' is not defined
food_id = "pizza"
print(isinstance(food_id, str))
True
class_id = true
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    class_id = true
NameError: name 'true' is not defined. Did you mean: 'True'?
class_id = 'true'
print(isinstance(class_id, bool))
False
class_id = True
print(isinstance(class_id, bool))
True
