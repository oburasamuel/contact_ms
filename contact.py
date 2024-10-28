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

def delete_contact(people):
    for i, person in enumerate(people):
        print(i + 1, person["name"], "|", person["age"], "|", person["email"])


    number = input("Enter a number to be deleted: ")

    while True:
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

    if name in people:
        print(f"{results}")
        results.append(name)