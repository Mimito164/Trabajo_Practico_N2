# coding=utf-8
from datetime import datetime
import datetime as dt
import random
from textwrap import wrap
import msvcrt
import os
import time


# // --------------------------------- Pantallas --------------------------------- //

class pantalla:

    width = 70 #ancho de las cajas
    
    tituloPrincipal = "\n     █████████                                          ████                   \n    ███░░░░░███                                        ░░███                   \n   ███     ░░░  ████████   ██████   ████████    ██████  ░███   ██████   ██████ \n  ░███         ░░███░░███ ░░░░░███ ░░███░░███  ███░░███ ░███  ███░░███ ███░░███\n  ░███    █████ ░███ ░░░   ███████  ░███ ░███ ░███████  ░███ ░███ ░░░ ░███ ░███\n  ░░███  ░░███  ░███      ███░░███  ░███ ░███ ░███░░░   ░███ ░███  ███░███ ░███\n   ░░█████████  █████    ░░████████ ████ █████░░██████  █████░░██████ ░░██████ \n    ░░░░░░░░░  ░░░░░      ░░░░░░░░ ░░░░ ░░░░░  ░░░░░░  ░░░░░  ░░░░░░   ░░░░░░  "

    tituloSecundario = "  __  __          __                                                     \n  \ \/ /____     / /_ ___     _____ ____   ____   ____  ____  _____ ____ \n   \  // __ \   / __// _ \   / ___// __ \ / __ \ / __ \/_  / / ___// __ \\\n   / // /_/ /  / /_ /  __/  / /__ / /_/ // / / // /_/ / / /_/ /__ / /_/ /\n  /_/ \____/   \__/ \___/   \___/ \____//_/ /_/ \____/ /___/\___/ \____/ \n"

    error = ""

    dataType = ""


    def print_granelco(self):
        print(pantallas.tituloPrincipal,end='')
    
    def print_yoTeConozco(self):
        print(pantallas.tituloSecundario,end='')

    def print_line(self):
        for i in range(self.width):
            print("═",end='')

    def print_upperBox(self):
        print(" ╔═",end='')
        self.print_line()
        print("═╗")

    def print_separator(self):
        print(" ╠═",end='')
        self.print_line()
        print("═╣")

    def print_lowerBox(self):
        print(" ╚═",end='')
        self.print_line()
        print("═╝")

    def print_left(self):
        print(" ║ ", end='')

    def print_right(self):
        print(" ║")

    def print_text(self, text):

        text = wrap(text, self.width)

        self.print_left()

        for string in text:
            if string == text[-1]:
                break
            else:
                print(string,end='')
                spaces = self.width - len(string)
                for i in range(spaces):
                    print(" ",end='')
                self.print_right()
                self.print_left()

        print(text[-1],end='')
        
        spaces = self.width - len(text[-1])

        for i in range(spaces):
            print(" ",end='')
        
        self.print_right()

class pantallaInicio(pantalla):

    def print_pantalla(self):
        print(self.tituloPrincipal)
        print(self.tituloSecundario)
        self.print_upperBox()
        self.print_text("Bienvenido a Granelco, en que lo podemos ayudar?")
        self.print_separator()
        self.print_text("1) Ingrese su Tarjeta Granelco y coloque su PIN.")
        self.print_text("2) Ingrese su DNI/CUIT y coloque su PIN.")
        self.print_text("3) Salir.")
        if self.error != "":
            self.print_separator()
            self.print_text(self.error)
        self.print_lowerBox()

class pantallaIngeso(pantalla):
    usuario = ""

    r1 = "Usuario:"

    def set_r1(self):
        self.r1 = "Usuario: " + self.usuario

    def print_pantalla(self):
        print(self.tituloPrincipal)
        print(self.tituloSecundario)


        self.print_upperBox()
        if self.dataType == "tarjeta":
            self.print_text("Ingrese su numero de tarjeta. Puede ingresar \"1\" para volver a la pantalla de inicio.")
        elif self.dataType == "dnicuit":
            self.print_text("Ingrese su numero de DNI/CUIT. Puede ingresar \"1\" para volver a la pantalla de inicio.")
        else:
            self.print_text("Ingrese su PIN. Puede ingresar \"1\" para volver a la pantalla de inicio.")
        self.print_separator()
        self.set_r1()
        self.print_text(self.r1)
        self.print_text("Pin: ")
        
        if self.error != "":
            self.print_separator()
            self.print_text(self.error)
        self.print_lowerBox()

class pantallaPrincipal(pantalla):

    opcion1 = "1) Deposito en Pesos."
    opcion2 = "2) Deposito en Dolares."
    opcion3 = "3) Extraccion en Pesos."
    opcion4 = "4) Extraccion en Dolares."
    opcion5 = "5) Consultar Saldo."
    opcion6 = "6) Ver ultimos movimientos."
    opcion7 = "7) Cambiar PIN."
    opcion8 = "8) Desloguearse."

    def print_pantalla(self):
        print(self.tituloPrincipal)
        print(self.tituloSecundario)
        self.print_upperBox()
        self.print_text("Seleccione la operacion a realizar.")
        self.print_separator()
        self.print_text(self.opcion1)
        self.print_text(self.opcion2)
        self.print_text(self.opcion3)
        self.print_text(self.opcion4)
        self.print_text(self.opcion5)
        self.print_text(self.opcion6)
        self.print_text(self.opcion7)
        self.print_text(self.opcion8)
        
        if self.error != "":
            self.print_separator()
            self.print_text(self.error)
        self.print_lowerBox()   

class pantallaDep(pantalla):

    verdes = False
    end = False
    
    def print_pantalla(self):
        print(self.tituloPrincipal)
        print(self.tituloSecundario)
        self.print_upperBox()
        if self.verdes == True:
            if self.end == False:
                self.print_text("Ingrese la cantidad de dolares que desea depositar.")
            else:
                self.print_text("Se ha depositado satisfactoriamente la cantidad de Dolares ingresada, muchas gracias por confiar en Granelco.")

        else:
            if self.end == False:
                self.print_text("Ingrese la cantidad de Pesos que desea depositar.")
            else:
                self.print_text("Se ha depositado satisfactoriamente la cantidad de Pesos ingresada, muchas gracias por confiar en Granelco.")

        if self.error != "":
            self.print_separator()
            self.print_text(self.error)
        self.print_lowerBox()

class pantallaExtra(pantalla):

    end = False
    plata = ""
    verdes = False
    def print_pantalla(self):
        print(self.tituloPrincipal)
        print(self.tituloSecundario)
        self.print_upperBox()
        if self.end == False:
            if self.verdes == True:
                self.print_text("Ingrese la cantidad de dolares que desea extraer. Puede escribir 'salir' para volver atras.")
            else:
                self.print_text("Ingrese la cantidad de pesos que desea extraer. Puede escribir 'salir' para volver atras.")

        else:
            if self.verdes == True:
                self.print_text(f"Se ha entregado {self.plata} dolare(s)")
            else:
                self.print_text(f"Se ha entregado {self.plata} peso(s)")

        if self.error != "":
            self.print_separator()
            self.print_text(self.error)
        self.print_lowerBox()

class pantallaSaldo(pantalla):

    r1 = "Dinero en Pesos: "
    r2 = "Dniero en Dolares: " 
    opcion1 = "Presione cualquier tecla para volver al inicio"

    def print_pantalla(self):
        print(self.tituloPrincipal)
        print(self.tituloSecundario)
        self.print_upperBox()
        self.print_text("El saldo acutal de su cuenta es:")
        self.print_separator()
        self.set_r1()
        self.set_r2()
        self.print_text(self.r1)
        self.print_text(self.r2)
        self.print_separator()
        self.print_text(self.opcion1)
        self.print_lowerBox()

    def set_r1(self):
        self.r1 = self.r1 + str(P.cuenta.dineroPesos)
    
    def set_r2(self):
        self.r2 = self.r2 + str(P.cuenta.dineroDolares)

class pantallaMovimientos(pantalla):
    textoInicio = "Estos son sus ultimos 5 movimientos"
    opcion1 = "1) Desea realizar otra operacion? [S/n]"

    def print_pantalla(self):
        print(self.tituloPrincipal)
        print(self.tituloSecundario)

        self.print_upperBox()
        if len(P.cuenta.movimientos) == 0:
            self.print_text("Esta cuenta aun no ha realizado movimientos...")
        else:
            self.print_text("Estos son sus ultimos movimientos.")
            
            y = -1
            if len(P.cuenta.movimientos) < 5:
                c = len(P.cuenta.movimientos)
            else:
                c = 5
            
            while c > 0:
                self.print_separator()
                testo = f"{P.cuenta.movimientos[y].fecha} {P.cuenta.movimientos[y].monto} {P.cuenta.movimientos[y].descripcion}"
                self.print_text(testo)
    
                y -= 1
                c -= 1
            
        self.print_lowerBox()

class pantallaPin(pantalla):
    estados = "inicio"
    posPin = ""
    r1 = ""

    def print_pantalla(self):
        self.set_r1()
        print(self.tituloPrincipal)
        print(self.tituloSecundario)
        self.print_upperBox()
        if self.estados == "inicio":
            self.print_text("Ingrese un nuevo PIN.")
        elif self.estados == "confirmacion":
            self.print_text("Confirme el pin")
            self.print_separator()
            self.print_text(self.r1)
            
        else:
            self.print_text("El PIN ha sido modificado correctamente. Nuevo PIN estalecido. Presione cualquier tecla para volver a la pantalla principal.")

        if self.error != "":
            self.print_separator()
            self.print_text(self.error)
    
        self.print_lowerBox()
    def set_r1(self):
        self.r1 = "PIN: " + self.posPin
    
class pantallaBloqueo(pantalla):
    
    def print_pantalla(self):
        print(self.tituloPrincipal)
        print(self.tituloSecundario)
        self.print_upperBox()
        self.print_text("Numero de intentos fallidos alcanzado. Su cuenta ha sido bloqueada, por favor dirijase a la sucursal para desbloquearla. Presione cualquier tecla para continuar.")
        self.print_lowerBox()

class pantallaAdmin(pantalla):

    textoInicio = "Seleccione la operacion a realizar."
    opcion1 = "1) Crear Usuario."
    opcion2 = "2) Desbloquear Usuario."
    opcion3 = "3) Resetear Stock de Billetes."
    opcion4 = "4) Salir."

    def print_pantalla(self):
        print(self.tituloPrincipal)
        print(self.tituloSecundario)
        self.print_upperBox()
        self.print_text(self.textoInicio)
        self.print_separator()
        self.print_text(self.opcion1)
        self.print_text(self.opcion2)
        self.print_text(self.opcion3)
        self.print_text(self.opcion4)
        
        if self.error != "":
            self.print_separator()
            self.print_text(self.error)
        self.print_lowerBox()

class pantallaNewUser(pantalla):

    # funcion que genera numero random
    # funcion qu

    nroTarjeta = "Numero de Tarjeta: "
    pin = "PIN: 0000"
    dni = "DNI: "
    identificacion = ""
    Tcuit = "CUIT: "

    PersonaFisica = False

    textoFinal = "Desea realizar otra operacion? [S/n]"

    estado = "inicio"

    def print_pantalla(self):
        print(self.tituloPrincipal)
        print(self.tituloSecundario)

        self.print_upperBox()
        if self.estado == "inicio":
            self.print_text("Elija el tipo de persona.")
            self.print_separator()
            self.print_text("1) Persona Fisica.")
            self.print_text("1) Persona Juridica.")
        
        elif self.estado == "Juridica":
            self.print_text("Ingrese el CUIT del nuevo usuario.")
        
        elif self.estado == "Fisica":
            self.print_text("Ingrese el DNI del nuevo usuario.")
        
        elif self.estado == "final":
            self.print_text("Datos del Usuario:")
            self.print_separator()
            if len(self.identificacion) > 8:
                self.print_text(self.dni + self.identificacion)
            else:
                self.print_text(self.Tcuit + self.identificacion)
            tarjeta = "".join(str(n) for n in (random.randint(0,9) for i in range(16)))
            self.print_separator()
            self.print_text("Tarjeta: " + str(tarjeta))
            self.print_separator()
            self.print_text(self.pin)
        
        if self.error != "":
            self.print_separator()
            self.print_text(self.error)
        
        self.print_lowerBox()

class desblUser(pantalla):
    end = False

    def print_pantalla(self):
        print(self.tituloPrincipal)
        print(self.tituloSecundario)
        self.print_upperBox()
        if self.end == False:
            self.print_text("Ingrese el usuario que desea desbloquear.")
        else:
            self.print_text("Presione cualquier tecla para continuar.")

        if self.error != "":
            self.print_separator()
            self.print_text(self.error)
        
        self.print_lowerBox()

class resetStock(pantalla):

    def print_pantalla(self):
        print(self.tituloPrincipal)
        print(self.tituloSecundario)
        self.print_upperBox()
        self.print_text("Se ha actualizado el stock de billetes satifactoriamente. Presione una tecla para continuar.")
        self.print_lowerBox()

# // --------------------------------- Maquina de Estados --------------------------------- //

class maquinaEstados():
    state = "Inicio"
    entrada = ""
    intentos = 3
    posibleIngreso = ""


    def checkInput(self):
        if msvcrt.kbhit(): # si detecta un input entonces guardalo, si no, no.
            character = str(msvcrt.getch())
            self.entrada = character[-2]
        else:
            self.entrada = ""

    def udpMachine(self):
        if self.state == "Inicio":
        # ESTOY EN INICIO

            if self.entrada == "1": # Ingresar con tarjeta
                pI.error = ""
                pIng.dataType = "tarjeta"
                self.state = "Ingreso"
                os.system('cls')
                pIng.print_pantalla()
    
            elif self.entrada == "2": # Ingresar con cuit o dni
                pI.error = ""
                pIng.dataType = "dnicuit"
                self.state = "Ingreso"
                os.system('cls')
                pIng.print_pantalla()
            
            elif self.entrada == "3":
                exit()

            else:
                pI.error = "No elegiste ninguna de las opciones presentada, por favor vuelva a elegir"
                os.system('cls')
                pI.print_pantalla()
        # FIN INICIO

        elif self.state == "Ingreso":
        # ESTOY EN INGRESO
            lineaAdmin = ""
            with open(bD.direccionAdmin, "r+") as ad:
                lineaAdmin = ad.read().splitlines()

            if self.entrada == "1":
                self.state = "Inicio"
                pIng.usuario = ""
                pIng.error = ""
                pIng.dataType = ""
                self.intentos = 3
                os.system('cls')
                pI.print_pantalla()
            
            elif lineaAdmin[0] == self.entrada: # coincide con el admin
                pIng.usuario = lineaAdmin[0]
                pIng.error = ""
                pIng.dataType = "pin"
                os.system('cls')
                pIng.print_pantalla()

            elif pIng.dataType == "pin" and pIng.usuario == lineaAdmin[0]:
                if self.entrada == lineaAdmin[1]:
                    self.state = "Admin"
                    pIng.error = ""
                    pIng.dataType = ""
                    pA.estado = "inicio"
                    os.system('cls')
                    pA.print_pantalla()

                else:
                    pIng.error = "El pin que ha ingresado no es correcto. Por favor, vuelva a intentarlo."
                    os.system('cls')
                    pIng.print_pantalla()


            elif pIng.dataType == "tarjeta" or pIng.dataType == "dnicuit": # estoy buscando por dni/cuit
                positionUser = bD.search(pIng.dataType,self.entrada)
                if positionUser == None and pIng.dataType == "tarjeta": # no se encontro el dato
                    pIng.error = "No se ha encontrado su tarjeta en nuestra base de datos. Por favor vuelva a escribir su tarjeta o dirijase a una sucursal para Registrarse en Granelco."
                    os.system('cls')
                    pIng.print_pantalla()

                elif positionUser == None and pIng.dataType == "dnicuit": # no se encontro el dato
                    pIng.error = "No se ha encontrado su DNI/CUIT en nuestra base de datos. Por favor vuelva a escribir su DNI/CUIT o dirijase a una sucursal para Registrarse en Granelco."
                    os.system('cls')
                    pIng.print_pantalla()

                else: # se encontro el dato
                    
                    pIng.usuario = self.entrada
                    usuarioBloqueado = bD.search_line(positionUser,"estado", "b") # busco si esta bloqueado
                    if usuarioBloqueado == True: #esta bloqueada
                        pIng.error = ""
                        pIng.dataType = ""
                        pIng.usuario = ""
                        self.state = "Bloqueado"
                        os.system('cls')
                        pB.print_pantalla()

                    else: # no esta bloqueado
                        self.posibleIngreso = positionUser
                        pIng.usuario = self.entrada
                        pIng.error = ""
                        pIng.dataType = "pin"
                        os.system('cls')
                        pIng.print_pantalla()

            else: # estoy buscando el pin
                if bD.search_line(self.posibleIngreso,pIng.dataType,self.entrada) == False: # no coincide el pin
                    self.intentos -= 1
                    if self.intentos == 0: # se acabaron los intentos
                        pIng.usuario = ""
                        self.intentos = 3
                        pIng.error = ""
                        bD.modifyUser(self.posibleIngreso, "estado", "b")
                        bD.usuariosBloqueados.append(self.posibleIngreso)
                        self.state = "Bloqueado"
                        os.system('cls')
                        pB.print_pantalla()
                    else: # quedan intentos
                        pIng.error = f"El pin que ha ingresado no es correcto. Le quedan {self.intentos} intento(s). Por favor, vuelva a intentarlo."    
                        os.system('cls')
                        pIng.print_pantalla() 

                else: # coincide el pin del usuario
                    self.state = "Principal"
                    self.intentos = 3
                    pIng.usuario = ""
                    pIng.error = ""
                    global P
                    if len(pIng.usuario) > 8: # es una persona juridica
                        P = PersonaJuridica(self.posibleIngreso)
                    else: # es una persona fisica
                        P = PersonaFisica(self.posibleIngreso)
                    os.system('cls')
                    pP.print_pantalla()
        # FIN INGRESO

        elif self.state == "Bloqueado":
        # ESTOY EN BLOQUEO
            self.state = "Inicio"
            os.system('cls')
            pI.print_pantalla()
        # FIN BLOQUEO

        elif self.state == "Principal":
        # ESTOY EN PRINCIPAL
            if self.entrada == "1": # deposito en pesos
                pD.verdes = False
                self.state = "Deposito"
                pP.error = ""
                os.system("cls")
                pD.print_pantalla()
            elif self.entrada == "2": # deposito en dolares
                pD.verdes = True
                self.state = "Deposito"
                pP.error = ""
                os.system("cls")
                pD.print_pantalla()
            elif self.entrada == "3": # extraccion en pesos
                self.state = "Extraccion"
                pE.verdes = False
                os.system("cls")
                pE.print_pantalla()
            elif self.entrada == "4": # extraccion en dolares
                self.state = "Extraccion"
                pE.verdes = True
                os.system("cls")
                pE.print_pantalla()
            elif self.entrada == "5": # consultar saldo
                self.state = "Saldo"
                os.system('cls')
                pS.print_pantalla()
            elif self.entrada == "6": # ver ultimos movimientos
                self.state = "Movimientos"
                os.system("cls")
                pM.print_pantalla()
            elif self.entrada == "7": # cambiar pin
                self.state = "Pin"
                self.error = ""
                os.system("cls")
                pPi.print_pantalla()
            elif self.entrada == "8": # desloguarse
                self.state = "Inicio"
                self.error = ""
                del P
                os.system('cls')
                pI.print_pantalla()
            else: # puso cualquier cosa
                pP.error = "No elegiste ninguna de las opciones presentada, por favor vuelva a elegir una."
                os.system('cls')
                pP.print_pantalla()
        # FIN PRINCIPAL

        elif self.state == "Saldo":
            self.state = "Principal"
            pS.r1 = "Dinero en Pesos: "
            pS.r2 = "Dinero en Dolares: "
            os.system('cls')
            pP.print_pantalla()
        
        elif self.state == "Pin":
            if pPi.estados == "inicio":
                if len(self.entrada) == 4:
                    pPi.posPin = self.entrada
                    pPi.estados = "confirmacion"
                    pPi.error = ""
                    os.system("cls")
                    pPi.print_pantalla()
                else:
                    pPi.error = "El pin debe ser de 4 (cuatro) digitos, por favor, vuelva a ingresar su nuevo pin que cumpla con estas caracteristicas."
                    pPi.posPin = ""
                    os.system("cls")
                    pPi.print_pantalla()

            elif pPi.estados == "confirmacion":
                if self.entrada != pPi.posPin:
                    pPi.error = "El pin difiere del ingresado anteriormente, por favor vuelva a ingresar el pin y confirmarlo."
                    pPi.posPin = ""
                    pPi.estados = "inicio"
                    os.system("cls")
                    pPi.print_pantalla()
                else:
                    pPi.error = ""
                    pPi.estados = "final"
                    P.pin = pPi.posPin
                    pPi.posPin = ""
                    bD.modifyUser(P.posicion,"pin",P.pin)
                    os.system("cls")
                    pPi.print_pantalla()

            else:
                pPi.posPin = ""
                pPi.estados = "inicio"
                pPi.error = ""
                self.state = "Principal"
                os.system("cls")
                pP.print_pantalla()

        elif self.state == "Deposito":
            if pD.end == False:
                if self.entrada.isdigit() == True:
                    pD.error = ""
                    pD.end = True
                    if pD.verdes == True:
                        monto = int(bD.get_line(P.posicion,"plataDolares"))
                        monto += int(self.entrada) 
                        bD.modifyUser(P.posicion, "plataDolares", str(monto))
                        P.cuenta.dineroDolares = int(monto)
                        fecha = gR.get_today()
                        fecha = f"{fecha[0]}/{fecha[1]}/{fecha[2]}"
                        descripcion = "Se ingresaron dolares."
                        with open(bD.movimientos, "a") as m:
                            m.write(f"{P.tarjeta} {fecha} {self.entrada} {descripcion} \n")
                        descripcion = ['Se', 'ingresaron', 'dolares.','\n']
                        P.cuenta.movimientos.append(movimiento(P.tarjeta, fecha, str(self.entrada), descripcion))
                    else:
                        monto = int(bD.get_line(P.posicion,"plataPesos"))
                        monto += int(self.entrada) 
                        bD.modifyUser(P.posicion, "plataPesos", str(monto))
                        P.cuenta.dineroPesos = int(monto)
                        fecha = gR.get_today()
                        fecha = f"{fecha[0]}/{fecha[1]}/{fecha[2]}"
                        descripcion = "Se ingresaron pesos."
                        with open(bD.movimientos, "a") as m:
                            m.write(f"{P.tarjeta} {fecha} {self.entrada} {descripcion} \n")
                        descripcion = ['Se', 'ingresaron', 'pesos.','\n']
                        P.cuenta.movimientos.append(movimiento(P.tarjeta, fecha, str(self.entrada), descripcion))
                    os.system("cls")
                    pD.print_pantalla()

                else:
                    pD.error = "El monto que desea ingresar no es un numero, por favor ingrese un numero."
                    os.system("cls")
                    pD.print_pantalla()
            else:
                self.state = "Principal"
                pD.error = ""
                pD.end = False
                os.system("cls")
                pP.print_pantalla()

        elif self.state == "Extraccion":
            if self.entrada == "salir":
                self.state = "Principal"
                pE.error = ""
                os.system("cls")
                pP.print_pantalla()
                
            elif pE.end == False:

                if self.entrada.isnumeric() == False:
                    pE.error = "Por favor ingrese un numero"
                    os.system("cls")
                    pE.print_pantalla()
                else:
                    pE.error = ""
                    if pE.verdes == True:
                        gR.extraccion("dolares", self.entrada)
                        pE.end = True
                        os.system("cls")
                        pE.print_pantalla()
                    else:
                        gR.extraccion("pesos", self.entrada)
                        pE.end = True
                        os.system("cls")
                        pE.print_pantalla()
            else:
                self.state = "Principal"
                pE.error = ""
                pE.end = False
                os.system("cls")
                pP.print_pantalla()

        elif self.state == "Movimientos":
            self.state = "Principal"
            os.system("cls")
            pP.print_pantalla()

        elif self.state == "Admin":
            if self.entrada == "4":
                self.state = "Inicio"
                os.system("cls")
                pI.print_pantalla()
            
            elif self.entrada == "1":
                self.state = "NUser"
                os.system("cls")
                pN.print_pantalla()

            elif self.entrada == "3":
                self.state = "rStock"
                gR.resetStock()
                os.system("cls")
                pR.print_pantalla()
            
            elif self.entrada == "2":
                self.state = "desbloquear"
                os.system("cls")
                pDes.print_pantalla()

            else:
                pA.error = "No eligio ninguna de las opciones peresentadas."
                os.system("cls")
                pA.print_pantalla()
        
        elif self.state == "rStock":
            self.state = "Admin"
            os.system("cls")
            pA.print_pantalla()
            
        elif self.state == "NUser":
            if pN.estado == "inicio":
                if self.entrada == "1":
                    pN.estado = "Fisica"
                    pA.error = ""
                    os.system("cls")
                    pN.print_pantalla()
                elif self.entrada == "2":
                    pN.estado = "Juridica"
                    pA.error = ""
                    os.system("cls")
                    pN.print_pantalla()
                else:
                    pA.error = "No eligio ninguna de las opciones presentadas"
                    os.system("cls")
                    pA.print_pantalla()
            elif pN.estado =="Juridica":
                if len(self.entrada) != 11:
                    pN.error = "El cuit debe tener 11 digitos, vuelva a ingresarlo."
                    os.system("cls")
                    pN.print_pantalla()
                elif self.entrada.isnumeric() == False:
                    pN.error = "Ha ingresado mal el CUIT, por favor vuelva a ingresarlo."
                    os.system("cls")
                    pN.print_pantalla()
                else:
                    pN.estado = "final"
                    pN.identificacion = self.entrada
                    os.system("cls")
                    pN.error = ""
                    pN.print_pantalla()
                    bD.add_user(self.entrada,pN.identificacion,"0000","0","0","d")
                    pN.estado = "inicio"
                    pN.identificacion = ""
                    
            elif pN.estado == "Fisica":
                if len(self.entrada) != 8:
                    pN.error = "El dnii debe tener 8 digitos, vuelva a ingresarlo."
                    os.system("cls")
                    pN.print_pantalla()
                elif self.entrada.isnumeric() == False:
                    pN.error = "Ha ingresado mal el DNI, por favor vuelva a ingresarlo."
                    os.system("cls")
                    pN.print_pantalla()
                else:
                    pN.estado = "final"
                    pN.error = ""
                    pN.identificacion = self.entrada
                    os.system("cls")
                    pN.print_pantalla()
                    bD.add_user(self.entrada,pN.identificacion,"0000","0","0","d")
                    pN.identificacion = ""
            elif pN.estado == "final":
                self.state = "Admin"
                os.system("cls")
                pA.error = ""
                pA.print_pantalla()

        elif self.state == "desbloquear":
            if pDes.end == False:
                r = bD.search("dnicuit", self.entrada)
                if r == None:
                    pDes.error = "Este usuario no existe"
                    os.system("cls")
                    pDes.print_pantalla()
                else:
                    bD.modifyUser(r, "estado", "d")
                    pDes.error = ""
                    pDes.end = True
                    os.system("cls")
                    pDes.print_pantalla()
            
            else:
                pDes.end = False
                self.state = "Admin"
                os.system("cls")
                pA.print_pantalla()




            

                
# // --------------------------------- Objetos --------------------------------- //

class Granelco():
    stockPesos = []
    stockDolares = []

    def __init__(self):
        self.get_stock()  
    
    def get_stock(self): # toma el dinero que hay en el txt
        with open(bD.stockGranelco, "r+") as sG:
            buffer = sG.readline().rstrip()
            buffer = buffer.split(" ")

            plata = buffer[1: ]
            
            for i in range(len(plata)):
                plata[i] = int(plata[i])
            
            self.stockPesos = plata[ :7]
            self.stockDolares = plata[7: ]

    def get_today(self):
        dd = int(datetime.now().day)
        mm = int(datetime.now().month)
        yy = int(datetime.now().year)
        hour = int(datetime.now().hour)
        return [dd,mm,yy,hour]

    def resetStock(self):
        today = self.get_today()
        with open(bD.stockGranelco, "r+") as sG:
            buffer = sG.readline()
            buffer = buffer.split(" ")
            buffer.pop(0)
            print(buffer)

            for i in range(len(buffer)):
                print(buffer[i])
                b = int(buffer[i])
                print(b)
                b += 10
                print(b)
                b = str(b)
                buffer[i] = b
                
            buffer.insert(0,f"{today[0]}/{today[1]}/{today[2]}")

            buffer = " ".join(buffer)
            sG.seek(0)
            sG.truncate(0)
            sG.write(buffer)

    def extraccion(self, moneda, cantidad):
        cantidad = int(cantidad)
        plataPesos  = 0
        plataDolares = 0
        diccionarioPesos = {0:10, 1:20, 2:50, 3:100, 4:200, 5:500, 6:1000}
        diccionarioDolares = {0:1 , 1:2 , 2:5 , 3:10 , 4:20 , 5:50 , 6:100}


        with open(bD.direccionBaseDatos, "r"):
            if moneda == "pesos":
                suPlata = int(bD.get_line(P.posicion, "plataPesos"))
            else:
                suPlata = int(bD.get_line(P.posicion, "plataDolares"))
            if suPlata > cantidad:
                with open(bD.stockGranelco, "r+") as gr:
                    linea = gr.readline()
                    billetes = linea.split(" ")
                    fecha = billetes.pop(0)

                    for i in range(len(billetes)):
                        billetes[i] = int(billetes[i])

                    billetesPesos = billetes[ :7]
                    billetesDolares = billetes[7: ]
                    billetesEntrega = []
                    plataEntrega = 0

                    for i in range(7):
                        plataPesos += billetesPesos[i] * diccionarioPesos[i]
                        plataDolares += billetesDolares[i] * diccionarioDolares[i]
                            
                    if moneda == "pesos":
                        if cantidad > plataPesos:
                            return "Lamentablemente Granelco no cuenta con esa clantidad de dinero, por favor, vuelva en otro momento"
                        else:
                            for i in range(6,-1,-1):
                                if diccionarioPesos[i] > cantidad: # si mi billete es mas grande que la cantidad de plata que pide paso a uno de valor mas bajo
                                    billetesEntrega.insert(0, 0)
                                    pass
                                else:
                                    ticket = cantidad//diccionarioPesos[i]
                                    if ticket > billetesPesos[i]:
                                        cantidad = cantidad - billetesPesos[i] * diccionarioPesos[i]
                                        billetesEntrega.insert(0,billetesPesos[i])
                                        billetesPesos[i] = 0
                                        
                                    else:
                                        cantidad = cantidad - ticket * diccionarioPesos[i]
                                        billetesPesos[i] -= ticket
                                        billetesEntrega.insert(0,ticket)

                    else:
                        if cantidad > plataDolares:
                            return "Lamentablemente Granelco no cuenta con esa clantidad de dinero, por favor, vuelva en otro momento"
                        else:
                            for i in range(6,-1,-1):
                                if diccionarioDolares[i] > cantidad: # si mi billete es mas grande que la cantidad de plata que pide paso a uno de valor mas bajo
                                    billetesEntrega.insert(0, 0)
                                    pass
                                else:
                                    ticket = cantidad//diccionarioDolares[i]
                                    if ticket > billetesDolares[i]:
                                        cantidad = cantidad - billetesDolares[i] * diccionarioDolares[i]
                                        billetesEntrega.insert(0,billetesDolares[i])
                                        billetesPesos[i] = 0   
                                    else:
                                        cantidad = cantidad - ticket * diccionarioDolares[i]
                                        billetesDolares[i] -= ticket
                                        billetesEntrega.insert(0,ticket)

                    for i in range(7):
                        if moneda == "pesos":
                            plataEntrega += billetesEntrega[i] * diccionarioPesos[i]
                        else:
                            plataEntrega += billetesEntrega[i] * diccionarioDolares[i]
                    
                    billetesTotales = billetesPesos + billetesDolares

                    nuevoStock = fecha
                    
                    for i in range(14):
                        billetesTotales[i] = str(billetesTotales[i])
                        nuevoStock = nuevoStock + " " + billetesTotales[i]
                    
                    gr.seek(0)
                    gr.truncate(0)
                    gr.write(nuevoStock)

                if moneda == "pesos":
                    plataUsuario = int(bD.get_line(P.posicion,"plataPesos"))
                    plataUsuario = plataUsuario - plataEntrega
                    bD.modifyUser(P.posicion,"plataPesos",str(plataUsuario))
                else:
                    plataUsuario = int(bD.get_line(P.posicion,"plataDolares"))
                    plataUsuario = plataUsuario - plataEntrega
                    bD.modifyUser(P.posicion,"plataDolares", str(plataUsuario))

                pE.plata = plataEntrega
                monto = f"-{plataEntrega}"
                descripcion = f"Se retiraron {moneda}."
                fecha = gR.get_today()
                fecha = f"{fecha[0]}/{fecha[1]}/{fecha[2]}"
                with open(bD.movimientos, "a") as m:
                    m.write(f"{P.tarjeta} {fecha} -{pE.plata} {descripcion} \n")
                if moneda == "pesos":
                    descripcion = ['Se', 'retiraron', 'pesos.', '\n']
                else:
                    descripcion = ['Se', 'retiraron', 'dolares.', '\n']
                P.cuenta.movimientos.append(movimiento(P.tarjeta, fecha, str(-pE.plata), descripcion))
            else:
                pE.error = "Fondos insuficientes."

    def updStock(self): # actualiza diariamente (suma 10)
        date = self.get_today()
        dd = date[0]
        mm = date[1]
        yy = date[2]

        with open(bD.stockGranelco, "r+") as sG:

            buffer = sG.readline()
            buffer = buffer.split(" ")
            diaAntes = buffer.pop(0)
            dD,mM,yY = diaAntes.split("/")

            yY = int(yY)
            mM = int(mM)
            dD = int(dD)

            if yY < yy or mM < mm or dD < dd:

                if dt.datetime.now().hour >= 10:
                    gR.resetStock()

class movimiento:
    tarjeta = ""
    fecha = ""
    monto = ""
    descripcion = ""

    def __init__(self, tarjerta, fecha, monto, descripcion):
        self.tarjeta = tarjerta
        self.fecha = fecha
        self.monto = monto
        print(descripcion)
        self.descripcion = " ".join(descripcion)

class cuenta:
    movimientos = []

    def __init__(self,user,tarjeta):
        self.dineroPesos = bD.get_line(user,"plataPesos")
        self.dineroDolares = bD.get_line(user, "plataDolares")
        with open(bD.movimientos, "r") as m:
            movimientosTotales = m.read().splitlines()
            for i in range(len(movimientosTotales)):
                movimientosTotales[i] = movimientosTotales[i].split(" ")
                if movimientosTotales[i][0] == tarjeta:
                    self.movimientos.append(movimiento(movimientosTotales[i][0], movimientosTotales[i][1], movimientosTotales[i][2], movimientosTotales[i][3: ]))                  

class Usuario:
    tajeta = 0
    pin = 0
    posicion = 0

    def __init__(self, user):
        self.tarjeta = bD.get_line(user, "tarjeta")
        self.cuenta = cuenta(user,self.tarjeta)

class PersonaFisica(Usuario):
    dni = 0

    def __init__(self, user):
        self.posicion = user
        self.dni = bD.get_line(user,"dnicuit")
        
        self.pin = bD.get_line(user, "pin")
        super().__init__(user)

class PersonaJuridica(Usuario):
    cuit = 0

    def __init__(self, user):
        self.posicion = user
        self.cuit = bD.get_line(user,"dnicuil")
        self.tarjeta = bD.get_line(user, "tarjeta")
        self.pin = bD.get_line(user, "pin")
        super().__init__(user)

class BaseDatos():

    direccionAdmin = r"C:\Users\fjara\Desktop\Ejercicios Lupi\Trabajo\Admin.txt"
    direccionBaseDatos = r"C:\Users\fjara\Desktop\Ejercicios Lupi\Trabajo\BaseDatos.txt"
    stockGranelco = r"C:\Users\fjara\Desktop\Ejercicios Lupi\Trabajo\stockgranelco.txt"
    movimientos = r"C:\Users\fjara\Desktop\Ejercicios Lupi\Trabajo\movimientos.txt"

    indexDatos = {"dnicuit":0, "tarjeta":1 , "pin":2, "plataPesos":3, "plataDolares":4, "estado":5 }
    usuariosBloqueados = []
    
    def __init__(self):
        self.set_usuariosBloqueados()
    
    def add_user(self, id, tarjeta, pin, pP, pD, e):
        with open(self.direccionBaseDatos, "a") as bd:
            bd.write(f"\n{id} {tarjeta} {pin} {pP} {pD} {e}")


    def set_usuariosBloqueados(self):
        with open(self.direccionBaseDatos, "r+") as bd:
            lineas = bd.read().splitlines()
            for i in range(len(lineas)):
                lineas[i] = lineas[i].split(" ")
                if lineas[i][5] == "b":
                    self.usuariosBloqueados.append(i)
    
    def modifyUser(self, posicionUsuario, field, nuevoDato):
        with open(self.direccionBaseDatos, "r+") as bd:
            lineas = bd.read().splitlines()
            usuario = lineas[posicionUsuario]
            datosUsuario = usuario.split(" ")
            data = datosUsuario[self.indexDatos[field]]
            data = nuevoDato
            datosUsuario[self.indexDatos[field]] = data
            usuario = ' '.join(datosUsuario)
            lineas[posicionUsuario] = usuario
            bd.seek(0)
            bd.write("\n".join(lineas))
            
    def search_line(self, userPosition, tipoDato, dato):
        with open(self.direccionBaseDatos, "r+") as bd:
            lineas = bd.read().splitlines()
            linea = lineas[userPosition].split(" ")

            if linea[self.indexDatos[tipoDato]] == dato:
                return True
            else:
                return False
    
    def get_line(self, userPosition, tipoDato):
        with open(self.direccionBaseDatos, "r") as bd:
            lineas = bd.read().splitlines()
            linea = lineas[userPosition].split(" ")
            return linea[self.indexDatos[tipoDato]]

    def search(self, tipoDato, dato):
        with open(self.direccionBaseDatos, "r+") as bd:
            lineas = bd.read().splitlines()
            for i in range(len(lineas)):
                lineas[i] = lineas[i].split(" ")
                if lineas[i][self.indexDatos[tipoDato]] == dato:
                    return i
            return None


pI = pantallaInicio()           # State Inicio
pIng = pantallaIngeso()         # State Ingreso
pP = pantallaPrincipal()        # State Principal
pE = pantallaExtra()            # State Extra
pD = pantallaDep()              # State
pS = pantallaSaldo()            # State
pM = pantallaMovimientos()      # State
pPi = pantallaPin()             # State Pin
pB = pantallaBloqueo()          # State Bloqueado
pA = pantallaAdmin()            # State Admin
pN = pantallaNewUser()          # State
pDes = desblUser()              # State
pR = resetStock()               # State

mE = maquinaEstados()           # State

bD = BaseDatos()

gR = Granelco()
pI.print_pantalla()


while True:
    gR.updStock() # chekea si se puede cargar plata en el dia
    if mE.state == "Ingreso" or (mE.state == "desbloquear" and pDes.end == False)or (mE.state == "NUser" and pN.estado == "Fisica" ) or (mE.state == "NUser" and pN.estado == "Juridica" ) or (mE.state == "Extraccion" and pE.end == False)or (mE.state == "Pin" and pPi.estados == "inicio") or (mE.state == "Pin" and pPi.estados == "confirmacion") or (mE.state == "Deposito" and pD.end == False):
        mE.entrada = input()
        mE.udpMachine()
        
    else:
        mE.checkInput()
        
        if mE.entrada != "":  
            mE.udpMachine()