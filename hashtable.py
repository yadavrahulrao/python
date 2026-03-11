list = [[],[],[],[],[],[],[],[],[],[],]

# each element is a bucket 


# create a hash function 
def hash_table(value):
  s = 0
  for char in value:
    s += ord(char)
  return s % 10

print(hash_table('Bob'))



# insert a element in a hash table 
def add(name):
  index = hash_table(name)
  list[index].append(name)
  # list[index] = name   -- this will add only one element at a position

add('Bob')
print(list)

add('Lisa')
add('Stuart')
add('Vipin')
add('Deepak')
print(list)

def contain(name):
  index = hash_table(name)
  return list[index] == name
print(contain('Vipin'))

print(hash_table('Vipin'))