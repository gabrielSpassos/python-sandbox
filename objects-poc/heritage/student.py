from person import Person


class Student(Person):
    def study(self):
        print(f'{self.name} is studying...')
