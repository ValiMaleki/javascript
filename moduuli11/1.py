class Publication:
    def __init__(self, name):
        self.name = name

    def print_information(self):
        print(f"Name: {self.name}")


class Book(Publication):
    def __init__(self, name, author, page_count):
        self.author = author
        self.page_count = page_count
        super().__init__(name)

    def print_information(self):
        super().print_information()
        print(f"name of the book is {self.author} and {self.page_count} pages")


class Magazine(Publication):
    def __init__(self, name, chef_editor):
        self.chef_editor = chef_editor
        super().__init__(name)

    def print_information(self):
        super().print_information()
        print(f"Magazin: {self.chef_editor}  {self.name}")


donald_duck = Magazine("Donald Duck", "Aki Hyyppä")
compartment = Book("Compartment No. 6", "Rosa Liksom", 192)

donald_duck.print_information()
compartment.print_information()
