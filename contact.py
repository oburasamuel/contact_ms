# person attribute
# add person function
# create an empty list to store the number of people
# Delete person function
# loop through the people for the person to be deleted
# search person function(an algorithm to loop through the people results)


def add_person():
    name = input("Name: ")
    age = input("age: ")
    email = input("email: ")

    person = {
    'name': 'name',
    'age': 'age',
    'email': 'email'
    }

    return person


def display_people(people):
    for i, person in enumerate(people):
        print(i + 1, person["name"], "|", person["age"], "|", person["email"])


def delete_contact(people):
    display_people(people)


    while True:
        number = input("Enter a number to be deleted: ")

        try:
            number = int(number)
            if number <= 0 or number > len(people):
                print("Invalid range!")

            else:
                break
        except:
               print("Invalid number!")
    people.pop(number - 1)
    print("Person deleted.")


def search(people):
    name = input("search for a name: ")
    results = []

    if person in people:
        search_name = person["name"]
        if search_name in name.lower():
            results.append(Person)

    display_people(results)


print("Hi, welcome to your contact manager.")
print()

with open("contact.json", "r") as f:


while True:
    print()
    print("Contact list size:", len(people))

    command = input("You can 'Add', 'Delete', or 'Search' and 'Q' for quit: ").lower()

    if command == "add":
        person = add_person()
        people.append(person)
        print("Person added!")
    
    elif command == "delete":
        delete_contact(people)
    
    elif command == "search":
         search(people)

    elif command == "q":
        break

    else:
         print("Invalid command")