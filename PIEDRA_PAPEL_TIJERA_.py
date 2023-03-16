#PIEDRA_PAPEL_TIJERA
from random import randint
print("------------------------------")
print(" piedra , papel o tijera")
print("-------------------------------")

#input
print("-----PREPARADO--------")
print("----1--------2-----------3------")
print("---------Piedra-----------")
print("---------Papel------------")
print("---------Tijera-----------")

#procesing
print("dime cual opcion deseas secar: \n")
print("1.piedra")
print("2.papel")
print("3.Tijera")
num_maq= randint(1,3)

opcion=int(input("\n Dame la opcion:"))
if (opcion==1):
    if num_maq==1:
        print("Sacó piedra y tu sacaste piedra; asi que : empataste")
    elif num_maq==2:
          print("Sacó papel  y tu sacaste piedra;asi que: perdiste") 
    elif num_maq==3:
      print("Sacó tijera y tu sacaste piedra; asi que:  ganaste")
elif(opcion==2):
     if num_maq==1:
            print("Sacó piedra y tu sacaste pepel; asi que: ganaste")
     elif num_maq==2:
      print("Sacó papel y tu sacaste papel; asi que empataste")  
     elif num_maq==3:
       print("Sacó tijera y tu sacaste papel; asi que: perdiste")
elif (opcion==3):
    if num_maq==1:
      print("Sacó piedra y tu tijera; asi que: perdiste")
    elif num_maq==2:
      print("Sacó papel y tu tijera; asi que: ganaste")
    elif num_maq==3:
      print("Sacó tijera y tu tijera;  asi que: empataste")
else:
      print("No se puede realizar el proceso esa opcion no hace parte de la propuestas")