
def testy():
    #Zadanie 1:
    
    s1 = Student("Lukasz", "Broda", 20004, "IIS")
    
    print(s1.imie)
    print(s1.nazwisko)
    print(s1.kierunek)
    print(s1)
    
    print()
     
    #Zadanie 2:
    
    s2 = Student("Jan", "Kowalski", 19992, "IKS")
    
    print(s1.__lt__(s2))
    print(s1.__eq__(s2))
    
    print()
    
    #Zadanie 3:
    
    s3 = Student("Grazyna","Kowalska",12321,"XDS")
    
    print("Licznik: %s"%(s3.getLicznik()))
    
    print()
    
    #Zadanie 4:
    
    s4 = StudentInformatyki("Marek", "Mocny", 45677, "", "Programowanie")
    
    print(s4)
    print(s4.specjalnosc)
    pass


    
    
class Student():
    __licznik = 0
    
    def __init__(self, imie, nazwisko, nr_indeksu, kierunek):
        Student.__licznik += 1
        self.imie = imie
        self.nazwisko = nazwisko
        self.__nr_indeksu = nr_indeksu
        self.kierunek = kierunek
            
    def __str__(self):
        return "Imie: %s\nnazwisko: %s\nnr ideksu: %s\nkierunek: %s"%(self.imie, self.nazwisko, self.__nr_indeksu, self.kierunek)
    
        
    def getLicznik(self):
        return self.__licznik
        
    def __lt__(self,other):
        if self.nazwisko < other.nazwisko:
            return True
        else:
            return False
        
    def __eq__(self,other):
        if self.nazwisko == other.nazwisko:
            return True
        else:
            return False
    
    def dekorator(obj):
        return obj
        
    @dekorator
    def rok_drugi(self):
        print("rok drugi")
      

class StudentInformatyki(Student):
    def __init__(self, imie, nazwisko, nr_indeksu, kierunek, specjalnosc):
        super(StudentInformatyki,self).__init__(imie, nazwisko, nr_indeksu, kierunek)
        self.kierunek = "IIS"
        self.specjalnosc = specjalnosc


if __name__ == "__main__":
    testy()