from csv import DictReader, DictWriter

DATABASE_FILE = "login_database.csv"

def read_database():
    """Reads from the database file and returns a python list of users. Uses DictReader

    Returns:
        List[Dict]: A list of python dictionaries. E.g.,: [{"username": "Jane", "passwords": bats}, {"username": "John", "passwords": cats}]
    """
    with open(DATABASE_FILE, 'r') as f:
        list_of_users = list(DictReader(f))    
    return list_of_users

def write_database(list_of_users):
    """Will write the list of users as a CSV file into "login_database.csv". Uses DictWriter.

    Args:
        list_of_users (List[Dict]): A list of python dictionaries. E.g.,: [{"username": "Jane", "passwords": bats}, {"username": "John", "passwords": cats}]
    """    
    # TODO Please fill this out!
    pass

def login(list_of_users):
    """Will login to a list of users. Will ask the user for their login information and check it against list_of_users.

    Args:
        list_of_users (List[Dict]): A list of python dictionaries.

    Returns:
        bool: Return True if login was successful, False if not successful. 
    """    
    username = input("Enter username: ")
    password = input("Enter password: ")

    valid_login = False
    for user in list_of_users:
        if username == user['username'] and user['password'] == password:
            valid_login = True
            break
    
    return valid_login

def register(list_of_users):
    """Prompts user for their credentials and creates a new user that is added to list_of_users

    Args:
        list_of_users (List[Dict]): A list of python dictionaries.

    Returns:
        bool: Returns True if the registration was successful, False otherwise
    """    
    # TODO Please fill this out!
    return True

def main():
    """This is the main function. It has three main components
    1. Reading the database
    2. A while loop taking user commands
    3. Saving the new database
    """    
    # 1. Read database from "login_database.csv" here
    list_of_users = read_database()
    print(list_of_users)
    # 2. User Commands
    while(True):
        command = input("Please enter your command (login, register, quit): ")
        # TODO please finish the rest of the commands!
        if command == "quit":
            break
        elif command == "login":
            result = login(list_of_users)
            if result:
                print("Valid Login!")
            else:
                print("Invalid Login!")
        else:
            print("Invalid command, try again!")

    # 3. write database to file, (saving the database)
    write_database(list_of_users)

if __name__ == "__main__":
    main()