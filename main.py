import wmi

# Carrega Informações #

c = wmi.WMI()
my_system = c.Win32_ComputerSystem()[0]

# Mostra Resultados #

print(f"Marca: {my_system.Manufacturer}")
print(f"Modelo: {my_system.Model}")
print(f"Nome: {my_system.Name}")
print(f"Qunatidade CPUs: {my_system.numberofProcessors}")
print(f"Arquitetura: {my_system.SystemType}")
print(f"Familia: {my_system.SystemFamily}")