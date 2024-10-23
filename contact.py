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


def display_people(people):
    for i, person in enumerate(person):
        print(i + 1, "-", person[])