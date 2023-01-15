fruit_dict = {}

with open('./data/fruits.txt', 'r') as f:
    fruits = f.readlines()
    for fruit in fruits:
        fruit = fruit.strip()
        if fruit not in fruit_dict:
            fruit_dict[fruit] = 1

        elif fruit in fruit_dict:
            fruit_dict[fruit] += 1

with open('./04.txt', 'w') as f:
    for fruit, count in fruit_dict.items():
        # print(fruit, count)
        f.write(f'{fruit} {count} \n')