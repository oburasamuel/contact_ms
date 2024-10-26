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


    while True:
        number = input("enter a number to delete: ")

        try:
            if number <= 0:
                print("Out of range")
            elif number > people:
                print("Out of range!")
                break
        
        except: 
               if


# def delete_contact(people):