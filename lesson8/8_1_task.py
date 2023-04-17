# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для 
# изменения и удаления данных

from os import path

file_base = "base.txt"
last_id = 0
all_data = []

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def read_records():
    global last_id, all_data

    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split()[0])
            return all_data
    return []


def show_all():
    if all_data:
        print(*all_data, sep="\n")
    else:
        print("Empty data")


def add_new_contact():
    global last_id
    array = ["surname", "name", "patronymic", "phone_number"]
    string = ""
    for i in array:
        string += input(f"Enter {i} ") + " "
    last_id += 1

    with open(file_base, "a", encoding="utf-8") as f:
        f.write(f"{last_id} {string}\n")


def change_contact():
    global all_data
    name_to_change = input("Enter contact name or surname to change: ")
    found = False
    for i, record in enumerate(all_data):
        if name_to_change in record:
            found = True
            new_record = input(f"Enter new record for {record}: ")
            all_data[i] = f"{record.split()[0]} {new_record}"
            print(f"Record for {record} changed successfully.")
    if not found:
        print(f"No contact with {name_to_change} was found.")
    
    with open(file_base, "w", encoding="utf-8") as f:
        f.write("\n".join(all_data))


def delete_contact():
    global all_data
    name_to_delete = input("Enter contact name or surname to delete: ")
    found = False
    for i, record in enumerate(all_data):
        if name_to_delete in record:
            found = True
            del all_data[i]
            print(f"Record for {record} deleted successfully.")
            break
    if not found:
        print(f"No contact with {name_to_delete} was found.")

    with open(file_base, "w", encoding="utf-8") as f:
        f.write("\n".join(all_data))


def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all records\n"
                       "2. Add a record\n"
                       "3. Search a record\n"
                       "4. Change\n"
                       "5. Delete\n"
                       "6. Exp/Imp\n"
                       "7. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_new_contact()
            case "3":
                pass
            case "4":
                change_contact()
            case "5":
                delete_contact()
            case "6":
                pass
            case "7":
                play = False
            case _:
                print("Try again!\n")


main_menu()