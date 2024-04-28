def parse_input():
    start_str = input("Будь ласка, введіть команду ").lower().strip().split(' ')
    return start_str

def add_contact(telef_dict, name, number):
    telef_dict[name] = number
    save_contacts(telef_dict)  # Зберегти контакти у файл
    return "Контакт додано."

def change_contact(telef_dict, name, number):
    if name in telef_dict:
        telef_dict[name] = number
        save_contacts(telef_dict)  # Зберегти контакти у файл
        return "Контакт оновлено."
    else:
        return "Контакт не знайдено."

def show_phone(telef_dict, name):
    if name in telef_dict:
        return telef_dict[name]
    else:
        return 'Номер відсутній у списку'

def hello():
    return 'Як я можу допомогти вам?'

def show_all(telef_dict):
    if telef_dict:
        return telef_dict
    else:
        return "Список контактів порожній."

def load_contacts():
    try:
        with open("contacts.txt", "r") as file:
            lines = file.readlines()
            contacts = {}
            for line in lines:
                name, number = line.strip().split(":")
                contacts[name] = number
            return contacts
    except FileNotFoundError:
        return {}

def save_contacts(telef_dict):
    with open("contacts.txt", "w") as file:
        for name, number in telef_dict.items():
            file.write(f"{name}:{number}\n")

def main():
    telef_dict = load_contacts()  # Завантажити контакти з файлу
    
    while True:
        val = parse_input()
        
        if val[0] == "hello":
            print(hello())
        elif val[0] == "add" and len(val) == 3:
            print(add_contact(telef_dict, val[1], val[2]))
        elif val[0] == "change" and len(val) == 3:
            print(change_contact(telef_dict, val[1], val[2]))
        elif val[0] == "phone" and len(val) == 2:
            print(show_phone(telef_dict, val[1]))
        elif val[0] == "all":
            print(show_all(telef_dict))
        elif val[0] == "exit" or val[0] == "close":
            print("До побачення!")
            break
        else:
            print('Команда не існує')

if __name__ == "__main__":
    main()

