class Publication:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(f"Julkaisun: {self.name}")


class Book(Publication):
    def __init__(self, name, author, pagenum):
        super().__init__(name)
        self.author = author
        self.pagenum = pagenum

    def print_info(self):
        super().print_info()
        print(f"Kirjassa on {self.pagenum} sivua.")
        print(f"Kirjailia: {self.author}")


class Mag(Publication):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor

    def print_info(self):
        super().print_info()
        print(f"Päätoimittaja: {self.editor}")


mag1 = Mag("Aku Ankka", "Aki Hyppää")
mag1.print_info()
book1 = Book("Hytti n:o 6", "Rosa Liksom", 200)
book1.print_info()
