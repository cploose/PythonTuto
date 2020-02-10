"""
file = open('./files/fruits.txt')
content = file.read()
file.close()

# meilleure façon de procéder , utilise la fonction close() automatiquement
with open('./files/fruits.txt') as myFiles:
    content2 = myFiles.read()


# print(content)
# print(content2)
"""
content3 = ''
with open('./files/file1.txt', 'a+') as file3:
    file3.seek(0)
    cont = file3.read()
    content3 = '\n' + cont + '\n' + cont

    file3.write(content3)
