import inspect


class Rectangulo:
    def __init__(self, largo, ancho, costo=0):
        self.largo = largo
        self.ancho = ancho
        self.costo = costo

    def obt_area(self):
        return self.largo * self.ancho

    def calcular_costo(self):
        area = self.obt_area()
        return area * self.costo


class Laptop:
    def __init__(self, company, model):
        self.compania = company
        self.modelo = model


class Lactop:
    def __init__(otro_self, company, model, colors):
        otro_self.compania = company
        otro_self.modelo = model
        otro_self.color = colors

    def lap_disponible(otro_otro_self, color):
        return color in otro_otro_self.color


r = Rectangulo(160, 120, 2000)
print("Area del rectangulo: %s unidades cuadradas" % (r.obt_area()))
print("Costo del campo es: %s pesos" % (r.calcular_costo()))


def laptops(marca, modelo):
    laptop = Laptop(marca, modelo)
    print(f"Compañia: {laptop.compania}")
    print(f"Modelo: {laptop.modelo}")


laptops("Lenovo", "thinkpad")

lap = Lactop('Dell', 'inspiron 7000', ['Silver', 'Black'])

print("Disponible") if lap.lap_disponible('Silver') else print("No disponible")
print("Disponible") if lap.lap_disponible('White') else print("No disponible")
