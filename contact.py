def add_person():
    name = input('Name: ')
    age = int(input('age: '))
    email = input('email: ')

    person = {
      'name': 'name',
      'age': 'age',
      'email': 'email'
    }
    
    return person


def delete_people(people):
    for i, person in enumerate(person):
        print(i + 1, "-", person["name"], "|", person["age"], "|", person["email"])

    number = input("enter a number to delete: ")


# def delete_contact(people):