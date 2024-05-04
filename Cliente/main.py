from models.client import Client
from repo.client import ClientRepo
import os
from time import sleep


ClientRepo.create_table_client("cls")

def insert_client1():
    print("Inserting client")
    print("-----------------")
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("email: ")
    address = input("address: ")
    password = input("password: ")
    client = Client(None, name, phone, email, address, password)
    ClientRepo.insert_client(client)


def list_client1():
    print("listing client")
    print("---------------")
    print("ID|NAME")
    clients = ClientRepo.get_all_client()
    for c in clients:
        print(f"{c.id:02d} | {c.name}")
def update_client1():
    print("updating client")
    print("----------------")
    id = int(input("client id: "))
    original_client = ClientRepo.get_one_client(id)
    new_name = input(f"New name ({original_client.name}): ")
    new_phone = int(input(f"New phone ({original_client.phone}): "))
    new_email = input(f"New email ({original_client.email}): ")
    new_address = input(f"new Address ({original_client.address}): ")
    new_password = input(f"New password ({original_client.password}): ")
    updated_client = Client(id, new_name, new_phone, new_email, new_address, new_password)
    ClientRepo.update_client(updated_client)

def delete_client1():
    print("delete client")
    print("-------------")
    id = int(input("client id: "))
    client = ClientRepo.get_one_client(id,)
    answer = input(f"Are you sure to delete the client {client.name}? (Y/N)")
    if answer.upper() == "Y":
        ClientRepo.delete_client(id)

def show_client1():
    print("showing client")
    print("--------------")
    id = input("Client Id: ")
    client = ClientRepo.get_one_client(id,)
    print(f"name: {client.name}")
    print(f"phone: {client.phone}")
    print(f"email: {client.email}")
    print(f"address: {client.address}")
    print(f"password: {client.password}")

def show_menu_client1():
    print("SuperHigherSkyIsTheLimit System")
    print("----------------------------")
    print("1 - insert_client")
    print("2 - list_client")
    print("3 - update_client")
    print("4 - delete_client")
    print("5 - show_client")
    print("6 - exit")

def get_user_option_client1() -> int:

    option = int(input("Desired option: "))
    return option
def clear_screen1():
    os.system("cls")
def wait_return_key1():
    print("---------------------------")
    sleep(2)
    print("Press RETURN to continue...")
    input()
while True:
    clear_screen1()
    show_menu_client1()
    option = get_user_option_client1()
    clear_screen1()
    match(option):
        case 1: insert_client1()
        case 2: list_client1()
        case 3: update_client1()
        case 4: delete_client1()
        case 5: show_client1()
        case 6: break
        case _: print("Invalid option")
    
    wait_return_key1()
print("Thanks for using program")



