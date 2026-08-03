
CONFIGURACION = ("Casa Matriz - Santiago Centro", "Sector Norte RM", "2026")

DISTANCIAS_KM = {
    "santiago": 0,
    "conchali": 11.17,
    "independencia": 5.71,
    "huechuraba": 12.00,
    "quilicura": 17.32,
    "recoleta": 7.26,
    "renca": 12.25
} 

COMUNAS_VALIDAS = set(DISTANCIAS_KM.keys())

vendedores = {
    "Vendedor 1": [],
    "Vendedor 2": [],
    "Vendedor 3": []
}

def calcular_total_recursivo(lista_visitas, indice=0):
    """Función recursiva obligatoria para la evaluación."""
    if indice == len(lista_visitas):
        return 0.0
    return lista_visitas[indice]["kilometraje"] + calcular_total_recursivo(lista_visitas, indice + 1)


def registrar_visita():
    """Captura y valida los datos de entrada del usuario."""
    print("\n--- REGISTRO DE NUEVA VISITA ---")
    
    print("Seleccione el vendedor:")
    opciones_vendedores = list(vendedores.keys())
    for i, v in enumerate(opciones_vendedores, 1):  
        print(f"{i}. {v}")
    
    try:
        v_opcion = int(input("Ingrese el número del vendedor: ")) - 1
        if v_opcion not in range(len(opciones_vendedores)):
            print("Opción de vendedor no válida.")
            return
        vendedor_seleccionado = opciones_vendedores[v_opcion]
    except ValueError:
        print("Debe ingresar un número válido.")
        return

    cliente = input("Ingrese el nombre del cliente/empresa: ").strip()
    if not cliente:
        print(" El nombre del cliente no puede estar vacío.")
        return

    comuna = input("Ingrese la comuna zona norte de destino en la RM: ").strip().lower()    
    
    if comuna in COMUNAS_VALIDAS:
        km_base = DISTANCIAS_KM[comuna]
        km_recorridos = km_base * 2 
        print(f"Comuna encontrada. Kilometraje base (Ida): {km_base} km")
        print(f"Ajustado automáticamente a Ida y Vuelta (x2): {km_recorridos:.2f} km")
    else:
        print("Comuna no encontrada en la base de datos de la zona norte.")
        try:
           
            km_base_manual = float(input("Por favor, ingrese el kilometraje manualmente (SOLO IDA): "))
            if km_base_manual < 0:
                print("El kilometraje no puede ser negativo.")
                return
            km_recorridos = km_base_manual * 2  
            print(f"Ajustado automáticamente a Ida y Vuelta (x2): {km_recorridos:.2f} km")
        except ValueError:
    
            print("Kilometraje inválido.")
            return

    registro = {
        "cliente": cliente,
        "comuna": comuna.capitalize(),
        "kilometraje": round(km_recorridos, 2)
    }
    vendedores[vendedor_seleccionado].append(registro)
    print(f"¡Visita registrada con éxito para {vendedor_seleccionado}!")


def mostrar_reporte():
    """Despliega los datos formateados con f-strings."""
    print("\n================ REPORTES DE VISITAS Y KILOMETRAJE ================")
    print(f"Origen Operación: {CONFIGURACION[0]} | Región: {CONFIGURACION[1]}")
    
    for vendedor, visitas in vendedores.items():
        print(f"\n Vendedor: {vendedor}")
        print("-" * 60)
        if not visitas:
            print("   No registra visitas aún.")
            print(f"   Total Kilómetros: 0 km")
            continue
            
        for i, v in enumerate(visitas, 1): 
            print(f"   {i}. Cliente: {v['cliente']:<15} | Comuna: {v['comuna']:<12} | Km: {v['kilometraje']:.2f} km")
        
        total_km = calcular_total_recursivo(visitas)
        print(f"   Total Kilómetros Acumulados: {total_km:.2f} km")
    print("==================================================================")


def menu_principal():
    """Bucle principal de ejecución del programa."""
    while True:
        print("\n SISTEMA DE CONTROL DE KILOMETRAJE - CASA MATRIZ")
        print("1. Registrar nueva visita de cliente")
        print("2. Ver reporte de vendedores y kilometrajes")
        print("3. Salir")
        
        opcion = input("Seleccione una opción (1-3): ").strip()
        
        if opcion == "1":
            registrar_visita()
        elif opcion == "2":
            mostrar_reporte()
        elif opcion == "3":
            print("Saliendo del sistema. ¡Buen viaje!")
            break 
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    menu_principal()


