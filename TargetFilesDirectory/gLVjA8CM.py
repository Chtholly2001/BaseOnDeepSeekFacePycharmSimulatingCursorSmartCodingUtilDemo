import sys

class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def __str__(self):
        return f"ID: {self.user_id}, Name: {self.name}, Email: {self.email}"

class UserManager:
    def __init__(self):
        self.users = []
        self.next_id = 1

    def add_user(self, name, email):
        user = User(self.next_id, name, email)
        self.users.append(user)
        self.next_id += 1
        print(f"User added: {user}")

    def list_users(self):
        if not self.users:
            print("No users found.")
        else:
            for user in self.users:
                print(user)

    def update_user(self, user_id, name=None, email=None):
        for user in self.users:
            if user.user_id == user_id:
                if name:
                    user.name = name
                if email:
                    user.email = email
                print(f"User updated: {user}")
                return
        print(f"User with ID {user_id} not found.")

    def delete_user(self, user_id):
        for i, user in enumerate(self.users):
            if user.user_id == user_id:
                del self.users[i]
                print(f"User with ID {user_id} deleted.")
                return
        print(f"User with ID {user_id} not found.")

    def find_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                print(user)
                return
        print(f"User with ID {user_id} not found.")

def main():
    manager = UserManager()
    while True:
        print("\nUser Management System")
        print("1. Add User")
        print("2. List Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Find User")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            manager.add_user(name, email)
        elif choice == '2':
            manager.list_users()
        elif choice == '3':
            try:
                user_id = int(input("Enter user ID to update: "))
                name = input("Enter new name (leave blank to keep current): ")
                email = input("Enter new email (leave blank to keep current): ")
                name = name if name.strip() else None
                email = email if email.strip() else None
                manager.update_user(user_id, name, email)
            except ValueError:
                print("Invalid ID. Please enter a number.")
        elif choice == '4':
            try:
                user_id = int(input("Enter user ID to delete: "))
                manager.delete_user(user_id)
            except ValueError:
                print("Invalid ID. Please enter a number.")
        elif choice == '5':
            try:
                user_id = int(input("Enter user ID to find: "))
                manager.find_user(user_id)
            except ValueError:
                print("Invalid ID. Please enter a number.")
        elif choice == '6':
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()