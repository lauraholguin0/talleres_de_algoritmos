diccionario={'Mikel': 3, 'Ane': 8, 'Amaia': 12, 'Unai': 5, 'Jon': 8, 'Ainhoa': 7,
'Maite': 5}
a=[]
for key in diccionario:
    if(not(diccionario[key] in a)):
        a.append(diccionario[key])
print(a)