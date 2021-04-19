class Cuenta:

    menu = {

        'Hamburguesa' : 250,
        'Gaseosa' : 100,
        'Cerveza' : 130,
        'Menu infantil' : 250,
        'Papas fritas' : 150,
        'Pastas' : 250,
        'Pescado' : 300,
        'Postres' : 150,

    }

    def __init__(self):
        self.total = 0
        self.objetos = []

    def añadir(self, objeto):
        self.objetos.append(objeto)
        self.total += self.menu[objeto]

    def print_factura(self, impuesto, servicio):

        impuesto(impuesto/100)*self.total
        servicio(impuesto/100)*self.total
        total = self.total + impuesto + servicio 

    for objeto in self.objetos:
        print(f'{objeto} ${self.menu[objeto]}')
        print(f'{"Total"} ${total:.2f}')
