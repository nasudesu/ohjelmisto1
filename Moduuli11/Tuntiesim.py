class Publication:
    def __init__(self, name, ):
        self.name = name
    def print_info(self):
        print(f"Julkaisun nimi: {self.name}")


class Book(Publication):
    def __init__(self, name, pagenum):
        self.pagenum = pagenum
        super().__init__(name)

    def print_info(self):
        super(Book, self).print_info()
        print(f"Olen {self.pagenum} sivuinen lehti")

class Mag(Publication):
    def __init__(self, name, editor):
        self.editor = editor
        super(Mag, self).__init__(name)

    def print_info(self):
        super(Mag, self).print_info()
        print(f"Kirjailia on {self.editor}")

pub1 = Book("Paras kirja", 200)
pub2 = Mag("Paras lehti", "Antti")
pub1.print_info()
pub2.print_info()