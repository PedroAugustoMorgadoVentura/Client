from models.product import Product
from repo.product import ProductRepo
import os

ProductRepo.create_table("cls")


def insert_product():

    print("Inserting product")
    print("-----------------")
    name = input("Name: ")
    price = float(input("Price:"))
    description = input("Description: ")
    product = Product(None, name, price, description)
    ProductRepo.insert(product)


def list_products():
    print("listing product")
    print("---------------")
    print("ID|NAME")
    products = ProductRepo.get_all()
    for p in products:
        print(f"{p.id:02d} | {p.name}")

def update_product():
    print("updating product")
    print("----------------")
    id = int(input("Product Id: "))
    original_product = ProductRepo.get_one(id)
    new_name = input(f"New name ({original_product.name}): ")
    new_price = input(f"New price ({original_product.price}): ")
    new_description = input(f"New description ({original_product.description}): ")
    updated_product = Product(id, new_name, new_price, new_description)
    ProductRepo.update(updated_product)


def delete_product():
    print("delete product")
    print("----------------")
    id = int(input("product id: "))
    product = ProductRepo.get_one(id)
    answer = input(f"Are you sure to delete the product {product.name}? (Y,N): ")
    if answer.upper() == "Y":
        ProductRepo.delete(id)

def show_product():
    print("showing product")
    print("---------------")
    id = int(input("Product Id: "))
    product = ProductRepo.get_one(id)
    print(f"name: {product.name}")
    print(f"price: {product.price:.2f}")
    print(f"description: {product.description} ")

def show_menu():
    print("SuperHigherSkyIsTheLimit System")
    print("----------------------------")
    print("1. insert_product")
    print("2. list_products")
    print("3. update_product")
    print("4. delete_product")
    print("5. show_product")
    print("6. exit")

def get_user_option() -> int:
    option = int(input("Desired Option: "))
    return option    
def clear_screen():
    os.system("cls")
def wait_return_key():
    print("-----------------------------")
    print("Press RETURN to continue...")
    input()


while True:
    clear_screen()
    show_menu()
    option = get_user_option()
    clear_screen()
    match(option):
        case 1: insert_product()
        case 2: list_products()
        case 3: update_product()
        case 4: delete_product()
        case 5: show_product()
        case 6: break
        case _: print("Invalid option!")
    wait_return_key()
print("Thanks for using this program1")


# Customer: id, name, phone, email, address, password