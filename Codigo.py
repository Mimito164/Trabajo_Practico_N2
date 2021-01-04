import time as t
import random as r
from textwrap import wrap

class pantallas():

    width = 100 #ancho de las cajas
    tituloPrincipal = r"""   █████████                                          ████                   
  ███░░░░░███                                        ░░███                   
 ███     ░░░  ████████   ██████   ████████    ██████  ░███   ██████   ██████ 
░███         ░░███░░███ ░░░░░███ ░░███░░███  ███░░███ ░███  ███░░███ ███░░███
░███    █████ ░███ ░░░   ███████  ░███ ░███ ░███████  ░███ ░███ ░░░ ░███ ░███
░░███  ░░███  ░███      ███░░███  ░███ ░███ ░███░░░   ░███ ░███  ███░███ ░███
 ░░█████████  █████    ░░████████ ████ █████░░██████  █████░░██████ ░░██████ 
  ░░░░░░░░░  ░░░░░      ░░░░░░░░ ░░░░ ░░░░░  ░░░░░░  ░░░░░  ░░░░░░   ░░░░░░  
"""
    tituloSecundario = r"""__  __          __                                                     
\ \/ /____     / /_ ___     _____ ____   ____   ____  ____  _____ ____ 
 \  // __ \   / __// _ \   / ___// __ \ / __ \ / __ \/_  / / ___// __ \
 / // /_/ /  / /_ /  __/  / /__ / /_/ // / / // /_/ / / /_/ /__ / /_/ /
/_/ \____/   \__/ \___/   \___/ \____//_/ /_/ \____/ /___/\___/ \____/

"""
    

    def print_granelco(self):
        print(pantallas.tituloPrincipal,end='')
    
    def print_yoTeConozco(self):
        print(pantallas.tituloSecundario,end='')

    def print_line(self):
        for i in range(self.width):
            print("═",end='')

    def print_upperBox(self):
        print("╔═",end='')
        self.print_line()
        print("═╗")

    def print_separator(self):
        print("╠═",end='')
        self.print_line()
        print("═╣")

    def print_lowerBox(self):
        print("╚═",end='')
        self.print_line()
        print("═╝")

    def print_left(self):
        print("║ ", end='')

    def print_right(self):
        print(" ║")

    def print_text(self, text):

        text = wrap(text, self.width)

        for string in self.mensajePrincipal:
            if string == self.mensajePrincipal[-1]:
                break
            else:
                print(string,end='')
                spaces = self.width - len(string)
                for i in range(spaces):
                    print(" ",end='')
                self.print_right()
                self.print_left()

        print(self.mensajePrincipal[-1],end='')
        
        spaces = self.width - len(self.mensajePrincipal[-1])

        for i in range(spaces):
            print(" ",end='')
        
        self.print_right()


class pantallaInicio(pantallas):
    
    
    mensajePrincipal = wrap("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer tellus magna, tempus eu arcu sed, molestie tempor magna. Ut accumsan erat nec nisi tempor egestas. Curabitur pulvinar accumsan magna sit amet euismod. Vivamus vitae fermentum ex. Duis vitae maximus ex. Suspendisse potenti. Nunc vitae suscipit augue. Ut laoreet tortor quis molestie tempor. Donec ultricies, erat quis maximus accumsan, mi lorem interdum metus, nec viverra ex velit vel justo. Cras ut cursus massa. Ut felis nibh, vulputate vel volutpat sit amet, consectetur ut tellus. Sed elementum pulvinar arcu a lacinia. Donec tristique, diam finibus efficitur volutpat, nulla urna posuere justo, et mattis diam nunc quis urna. Duis elit metus, facilisis id facilisis id, eleifend sit amet purus. Cras ullamcorper maximus libero, et tempus enim volutpat vel.", pantallas.width)
     

    def print_mensaje(self):

        self.print_upperBox()
        self.print_left()

        self.print_text("asdasdasd")   
        
        self.print_separator()


class granelco():

    def __init__(self, stockUsd, stockArs):
        self.stockUsd = stockUsd
        self.stockArs = stockArs


class usuario():
    
    def __init__(self, ide, pin, usd, ars, blk, arrFecha, arrMonto, arrDesc):
        self.ide = ide
        self.pin = pin

        self.cuenta = cuenta(usd, ars, blk, arrIDmov, arrFecha, arrMonto, arrDesc)

class cuenta():

    def __init__(self, usd, ars, blk, arrFecha, arrMonto, arrDesc):
        self.dineroUsd = usd
        self.dineroArs = ars
        self.bloqueada = blk
        
        self.mov1 = movimiento(arrFecha[0], arrMonto[0], arrDesc[0])
        self.mov2 = movimiento(arrFecha[1], arrMonto[1], arrDesc[1])
        self.mov3 = movimiento(arrFecha[2], arrMonto[2], arrDesc[2])
        self.mov4 = movimiento(arrFecha[3], arrMonto[3], arrDesc[3])
        self.mov5 = movimiento(arrFecha[4], arrMonto[4], arrDesc[4])

class movimiento():

    def __init__(self, fecha, monto, descripcion):
        self.fecha = fecha
        self.monto = monto
        self.descripcion = descripcion

class persona_juridica(usuario):
    
    def __init__(self, cuit):
        self.cuit = cuit

class persona_fisica(usuario):
    
    def __init__(self, dni):
        self.dni = dni



pInicio = pantallaInicio()

pInicio.print_granelco()
pInicio.print_yoTeConozco()
pInicio.print_mensaje()


input()