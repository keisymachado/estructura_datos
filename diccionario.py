persona = dict ()
continuar : bool = True

def agregar_valor (clave :str,valor:str)->None:
    persona.update({clave:valor})

def eliminar_valor ()->None:
   persona.remove()
   
continuar=True
while continuar:
    clavee = input ("que dato quieres inroducir ?")
    valor = input( clavee + ":")
    persona[clavee] = valor
    continuar = input("¿Quieres agregar algun otro dato (si /no )? ") == "Si"
    continuar == "no"
    break
    print ("quieres eliminar algun valor?")

opcion = int(input())

if opcion == 9:
      continuar = False

