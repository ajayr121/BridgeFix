import os
import requests
import migrated_todos
from dotenv import load_dotenv


load_dotenv()

api_url = os.getenv("api_url")
new_api = os.getenv("new_api")
created_by = os.getenv("created_by")
modify_by = os.getenv("modify_by")


def migrate_todos():
    choice = ""
    while choice != "2":
        print("\n---API OPTIONS ARE---")
        print("1, for get Method")
        print("2, for post Method")

        choice = input("Enter the number:")

        if choice == "1":
            response = requests.get(new_api)
            print(response.json())

        elif choice == "2":
            add = input("do you add data in bulk:Y/N :")
            if add == "Y":
                for i in migrated_todos.bulk_data:
                    resp=requests.post(new_api, json=i)
                    print(resp.json())
                    ids = resp.json().get("id")
                    migrated_todos.api_id.append(ids)

                with open("migrated_todos.py", "w") as f:
                    f.write("bulk_data = " + str(migrated_todos.bulk_data) + "\n")
                    f.write("api_id = " + str(migrated_todos.api_id) + "\n")
                    print("All id add successfully")
            
            dele = input("do you delete all bulk id:Y/N :")
            if dele == "Y":
                print("IDs to delete:", migrated_todos.api_id)


                for i in migrated_todos.api_id:
                            response = requests.delete(f"{new_api}{i}/", json={"created_by": "ajay121"})
                            print(f"Deleted user {i}")
                            print("All id deleted successfully!")
                with open("migrated_todos.py", "w") as f:
                        f.write(f"bulk_data = {migrated_todos.bulk_data}\n")
                        f.write("api_id = []\n")
               
        

        else:
            title = input("Enter the title:")
            description = input("Enter the description:")
            todo_data = {"title":title,"description":description, "created_by":created_by,"modify_by": modify_by}
            response = requests.post(new_api, json = todo_data)

migrate_todos()




