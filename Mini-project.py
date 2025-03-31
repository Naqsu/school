import json
import uuid

data_file = "libraries.json"

def load_data():
    try:
        with open(data_file, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_data(data):
    with open(data_file, "w") as file:
        json.dump(data, file, indent=4)

def create_library(name, pages):
    data = load_data()
    lib_uuid = str(uuid.uuid4())
    data[lib_uuid] = {"name": name, "pages": pages}
    save_data(data)
    print(f"Biblioteka utworzona! UUID: {lib_uuid}")

def delete_library(lib_uuid):
    data = load_data()
    if lib_uuid in data:
        del data[lib_uuid]
        save_data(data)
        print("Biblioteka usunięta.")
    else:
        print("Nie znaleziono biblioteki o podanym UUID.")

def edit_library(lib_uuid, name=None, pages=None):
    data = load_data()
    if lib_uuid in data:
        if name:
            data[lib_uuid]["name"] = name
        if pages:
            data[lib_uuid]["pages"] = pages
        save_data(data)
        print("Biblioteka zaktualizowana.")
    else:
        print("Nie znaleziono biblioteki o podanym UUID.")

def show_libraries():
    data = load_data()
    if data:
        for lib_uuid, details in data.items():
            print(f"UUID: {lib_uuid}, Nazwa: {details['name']}, Strony: {details['pages']}")
    else:
        print("Brak zapisanych bibliotek.")

def main():
    while True:
        command = input("Podaj komendę (create, delete, edit, show, exit): ").strip().lower()
        if command == "create":
            name = input("Podaj nazwę biblioteki: ")
            pages = int(input("Podaj liczbę stron: "))
            create_library(name, pages)
        elif command == "delete":
            lib_uuid = input("Podaj UUID biblioteki do usunięcia: ")
            delete_library(lib_uuid)
        elif command == "edit":
            lib_uuid = input("Podaj UUID biblioteki do edycji: ")
            name = input("Nowa nazwa (pozostaw puste, aby nie zmieniać): ") or None
            pages = input("Nowa liczba stron (pozostaw puste, aby nie zmieniać): ")
            pages = int(pages) if pages else None
            edit_library(lib_uuid, name, pages)
        elif command == "show":
            show_libraries()
        elif command == "exit":
            print("Zamykanie programu...")
            break
        else:
            print("Nieznana komenda.")

if __name__ == "__main__":
    main()