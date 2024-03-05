print('Bienvenidos a la a aerolinea "DELTA ROSA" ')
print('Por favor ingrese los sientes datos')
nombreStr = input("Ingrese su nombre por favor: ")
contactoStr = input("Ingrese su número de contacto por favor: ")
montoFlt = float(input('Monto ->'))
var_opcionStr = int(input('<<< MENU DE OPCIONES >>>\n\n1. Tiquete VIP\n2. Tiquete Turista\n3. Tiquete Economica\n4. SALIR\n ->'))


if var_opcionStr == 1:
    descuentoFlt = montoFlt * 0.05
    var_compradoInt = montoFlt - descuentoFlt
     
if var_opcionStr == 2:
    descuentoFlt  = montoFlt * 0.10
    var_compradoInt = montoFlt - descuentoFlt    
        
if var_opcionStr == 3:
    descuentoFlt = montoFlt * 0.15
    var_compradoInt = montoFlt - descuentoFlt    

print('Nombre del usuario', nombreStr)
print('Contacto del usuario', contactoStr)
print('valor total a pagar es de $', var_compradoInt)

    
        
