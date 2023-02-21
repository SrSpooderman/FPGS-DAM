dicci = {"Isaac": 19, "Raul": 15, "Toni": 20}
persona = ""
while persona.lower()!="fin":
    persona = input("Dime un nombre: ")
    
    try:
        print("Edad de ",persona, dicci[persona])
    except KeyError as err:
        print("Esta persona ",persona," no sabemos que edad tiene")
    except:
        print("Otro tipo de error") 