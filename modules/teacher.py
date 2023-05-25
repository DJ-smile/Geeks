data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
data_tuple = list(data_tuple)
letters = []
numbers = []

for i in data_tuple:
    if type(i) == str:
        letters.extend(i)
    elif type(i) == int or float:
        numbers.append(i)

numbers.pop(0)
numbers[0], numbers[2] = numbers[2], numbers[0]
numbers.insert(1,2)
changed_numbers = [n ** 2 for n in numbers]
changed_numbers = tuple(changed_numbers)
print(changed_numbers)

letters.reverse()
letters[0] = 'G'
letters[-2] = 'c'
letters = tuple(letters)
print(letters)