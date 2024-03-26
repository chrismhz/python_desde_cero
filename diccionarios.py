paciente1 = {"nombre":"Christian","edad":42, "peso":50.2,"fuma":True, "Clin":"Completamente sano"}
paciente2 = {"nombre":"Juan","edad":23, "peso":60.5,"fuma":False, "Clin":"Resfriado"}
paciente3 = {"nombre":"Julia","edad":13, "peso":50.5,"fuma":False, "Clin":"Resfriado"}

pacientes = [paciente1,paciente2,paciente3]

demo = ['uno', 'dos', 'tres','cuatro','cinco']

for x in range(len(pacientes)):
        print("------------------------------------------")
        print("- DICCIONARIO N°" ,x+1, "-")
        print("------------------------------------------")
        print("CLAVE\t\tVALOR\t\t<33\t\t\n")
        for clave, valor in pacientes[x].items():
            menor=""
            if (clave == "edad" and valor < 33):
                    menor = "✔"
            print(clave,"\t\t",valor,"\t\t",menor)
            
                #print("Encontramos un paciente con menos de 33")

# for clave, valor in paciente1.items():
#     print("Clave -> ", clave," | Valor -> ",valor)
#     print("***********************************\n")
#     if (clave == "edad" and valor < 33):
#         print("Encontramos un paciente con menos de 33")


#paciente["edad"]=18
#print("peso" in paciente)
#paciente.update({"edad":18})
#print(paciente.get("edad"))
#print(paciente['nombre'])
#print(paciente['fuma'])