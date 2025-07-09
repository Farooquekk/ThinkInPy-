result = {
    'farooque':3.84,
    'talha':3.66,
    'arbab':3.97,
    'ada dogesh':4.001
}

print(' ****** Check Your GPA : ******')
name = input('Enter name : ')

for nam in result:
    if name.lower() == nam:
        print(f'{name} : {result[nam]} 🎓')
        break
else:
    print('🚫 Your Name is not in the List.')
    