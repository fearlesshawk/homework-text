def people_name():
    #number_input = input('Укажите номер документа: ')
    for number in documents:
        if number.get('number') == number_input:
            return number.get('name')
    return ('Документа с таким номером нет')

def shelf_name():
    #number_input = input('Укажите номер документа: ')
    for number in directories:
        if number_input in directories.get(number):
            return number
    return ('Документа с таким номером нет')

def list_docs():
    for docs in documents:
        print(f'{docs["type"]} {docs["number"]} {docs["name"]}')

def add(docs, shelfs, shelf, type, number, name):
    doc = {'type': type, 'number': number, 'name': name}
    docs.append(doc)
    shelfs[shelf].append(doc['number'])
    return 'Документ добавлен'


documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []}

while True:
    print('Kоманды: p, s, l, a')
    command = input('Введите название команды ')
 
    if command == 'p':
        number_input = input('Укажите номер документа: ')
        print(people_name())
    
    elif command == 's':
        number_input = input('Укажите номер документа: ')
        print(shelf_name())
              
    elif command == 'l':
        list_docs(documents)
    
    elif command == 'a':
        shelf = input('Укажите номер полки куда положить документ. ')
        if shelf in directories.keys():
            type = input('Укажите тип документа: ')
            number = input('Укажите номер документа: ')
            name = input('Укажите имя владельца документа: ')        
            add(documents, directories, shelf, type, number, name)
        else:
            print('Такой полки не существует')