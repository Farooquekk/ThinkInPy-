print('*** Hello, this is simple program where You can save your Friend names !!')

friend_list = []

n = int(input('Enter number of Friends you want to save : ' ))

for i in range(n):
    name = input('Enter Your Friends Names : ' )
    friend_list.append(name)


friend_list.sort()

print('Your Friend List : ' , friend_list)


