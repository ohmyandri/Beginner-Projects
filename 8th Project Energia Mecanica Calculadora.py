def EnergiaMecanicaEPGyEC(masa, altura, velocidad ):
    gravedad = 9.81
    print(
        "Este programa Permite calcular la Energia Mecanica en un problema donde hay masa, altura y velocidad, es decir, donde hay Energia Potencial Gravitacional y Energia Cinetica")

    EnergiaCinetica = 0.5 * masa * velocidad ** 2
    print(f'La energia Cinetica existente es de {EnergiaCinetica} Joules')

    EnergiaPG = masa * gravedad * altura
    print(f'La energia Potencial Gravitatoria es de {EnergiaPG} Joules')

    EnergiaMecanica = EnergiaCinetica + EnergiaPG
    print(f'La Energia Mecanica en este caso es de {EnergiaMecanica} Joules')

EnergiaMecanicaEPGyEC() #Parametros = masa, altura, velocidad # En dicho orden

def EnergiaMecanicaEPEyEPG(masa, altura, deformacion, rigidez):
    gravedad = 9.81
    print("Este programa Permite calcular la Energia Mecanica en un problema donde hay masa, altura, deformacion y rigidez, es decir, donde hay Energia Potencial Gravitacional y Energia Potencial Elastica. Para evitar errores, debera haber introducido las medidas en metros y metros sobre segundos")

    EPG = masa * gravedad * altura
    print(f'La energia Potencial Gravitatoria es de {EPG} Joules')

    EPE = 0.5 * rigidez * deformacion ** 2
    print(f'La energia Potencial Elastica es de {EPE} Joules')

    EnergiaMecanica = EPG + EPE
    print(f'La Energia Mecanica en este caso es de {EnergiaMecanica} Joules')

EnergiaMecanicaEPEyEPG() #Parametros = masa, altura, deformacion, rigidez
                         # En dicho orden
