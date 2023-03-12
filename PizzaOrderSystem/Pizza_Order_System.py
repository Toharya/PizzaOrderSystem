import csv
import datetime


# Pizza üst sınıfı
class Pizza:
    def __init__(self):
        self.description = "Pizza"
    
    def get_description(self):
        return self.description
    
    def get_cost(self):
        return 0

# Pizza alt sınıfları
#Tüm alt sınıflar için gerekli açıklamalar yapılacak.
class KlasikPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Klasik Pizza Malzemeleri: Sucuk, Salam, Kasar"
    
    def get_cost(self):
        return 70

class MargaritaPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Margarita Pizza Malzemeleri: Domates, Zeytin, Mozarella"
    
    def get_cost(self):
        return 90

class TurkPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Türk Pizza Malzemeleri: Sucuk, Zeytin, Pastirma, Parmesan, Kasar"
    
    def get_cost(self):
        return 120

class SadePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Sade Pizza Malzemeleri: Permasan, Kasar, Mozarella"
    
    def get_cost(self):
        return 60

# Decorator üst sınıfı
class Decorator(Pizza):
    def __init__(self, pizza):
        super().__init__()
        self.component = pizza
    
    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)
    
    def get_description(self):
        return self.component.get_description() + ' ' + Pizza.get_description(self)

# Decorator alt sınıfları
class Zeytin(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Zeytin"
    
    def get_cost(self):
        return self.component.get_cost() + 3
    
class Mantar(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Mantar"
    
    def get_cost(self):
        return self.component.get_cost() + 2
    
class KeciPeyniri(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Keci Peyniri"
    
    def get_cost(self):
        return self.component.get_cost() + 3
    
class Et(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Et"
    
    def get_cost(self):
        return self.component.get_cost() + 5
    
class Sogan(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Sogan"
    
    def get_cost(self):
        return self.component.get_cost() + 1

class Misir(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Misir"
    
    def get_cost(self):
        return self.component.get_cost() + 4

# Menu.txt dosyasını oluşturmak adına main foksiyonu:
def main():
    with open('Menu.txt', 'w') as file:
       file.write('* Lutfen Bir Pizza Tabani Seçiniz:\n')
       file.write('1: KlasikPizza\n')
       file.write('2: MargaritaPizza\n')
       file.write('3: TurkPizza\n')
       file.write('4: SadePizza\n') 
       file.write('5: Zeytin\n')
       file.write('6: Mantar\n')
       file.write('7: KeciPeyniri\n')
       file.write('8: Et\n')
       file.write('9: Sogan\n')
       file.write('10: Misir\n')
       file.write('* Tesekkur Ederiz!\n')
       
      
    with open("Menu.txt") as cust_menu:
        for i in cust_menu:
            print(i, end="")

    class_dict = {1: KlasikPizza, 
                  2: MargaritaPizza, 
                  3: TurkPizza, 
                  4: SadePizza, 
                  5: Zeytin, 
                  6: Mantar, 
                  7: KeciPeyniri, 
                  8: Et, 
                  9: Sogan, 
                  10: Misir}
    
    code = input("Lütfen Pizzanızı Seçiniz: ")
    while code not in ["1", "2", "3", "4"]:
        code = input("Yanlış Tuşlama Yaptınız: ")

    order = class_dict[int(code)]()

    while code != "*":
        code = input("Ek Malzeme Almak İçin Tuşlama Yapınız (Direkt Siparişinizi Onaylamak İçin '*' Tuşuna Basınız): ")
        if code in ["5","6","7","8","9","10"]:
            order = class_dict[int(code)](order)

    print("\n"+order.get_description().strip() +
          "; ₺" + str(order.get_cost()))
    print("\n")

#Sipariş Bilgi Kartı oluşturuyoruz.
    print("----------Sipariş Bilgileri----------\n")
    name = input("İsminiz: ")
    ID = input("TC Kimlik Numaranız: ")
    kk_no = input("Kredi Kartı Numaranızı Giriniz: ")
    kk_psw = input("Kredi Kartı Şifrenizi Giriniz: ")
    time_of_order = datetime.datetime.now()

    with open('Orders_Database.csv', 'a') as orders:
        orders = csv.writer(orders, delimiter=',')
        orders.writerow([name, ID, kk_no, kk_psw, order.get_description(), time_of_order])
    print("Siparişiniz Onaylandı!")







main()

