class MyClass:
  
  var = None

  def __init__(self) -> None:
    var = 1

a = MyClass()
b = MyClass()
c = MyClass()
d = MyClass()

f = [a, c, d]
print(f)

c = d

if a in f: 
  print('a is in f')
else:
  print('a is not in f')

if b in f: 
  print('b is in f')
else:
  print('b is not in f')

if c in f: 
  print('c is in f')
else:
  print('c is not in f')