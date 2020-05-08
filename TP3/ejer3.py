#import sys
#PETIDO A PROCESAR 
peptido = "ATVEKGGKHKTGPNEKGKKIFVQKCSQCHYKTVLHGLFGRKTGQA"
#peptido = sys.argv[1]

#peptido = "LLLPPYKTGQA"

cant = peptido.find("YK")

#PROCESAMIENTO DEL PEPTIDO

result = ""

for i in range(cant+2, len(peptido)):
    result = result + peptido[i]

print(result)



# base a adn y base arn 
# TAT        =    UAU Y 
# AAA        =    AAA K