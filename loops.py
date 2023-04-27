

actual_password = 12345
password_from_user = 54321

password_incorrect = actual_password == password_from_user

run_count = 0
while True:
    print(1234)
    run_count += 1
    if run_count == 10:
        break


while run_count != 10:
    print(1234)
    run_count += 1


while password_incorrect:
    pass


users = [1,2,3,4,5]

for user in users:
    print(user)


for i in range(5):
    if i == 0:
        continue
    if i == 3:
        break

    print(i)
else:
    print('Когда я выполняюсь')


cities = ['Екатеринбург', 'Москва', 'Сочи']

print('/// ' * 5)

for i, city in enumerate(cities):
    print(f'{city} на {i+1} месте по чистоте')