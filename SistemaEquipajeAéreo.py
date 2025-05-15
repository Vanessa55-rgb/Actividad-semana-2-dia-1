# Precios base
precio_nacional = 230000
precio_internacional = 4200000

# Costos de equipaje
# (Si pesa hasta 20kg cuesta 50000, hasta 30kg cuesta 70000, hasta 50kg cuesta 110000)
# Si pasa de 50kg, no se admite
reservas = []
contador_id = 1  # Para los IDs de reservas

while True:
    print("\n Sistema de reservas ")
    print("1. Registrar nueva reserva")
    print("2. Ver reporte")
    print("3. Salir")

    opcion = input("Seleccione una opcion (1-7): ")

    # Opcion 1: registrar nueva reserva
    if opcion == "1":
        nombre = input("Nombre del pasajero: ")
        tipo_viaje = input("Tipo de viaje (nacional/internacional): ").lower()
        if tipo_viaje == "Nacional":
            destino = "Bogota - Medellin"
            precio_base = precio_nacional
        elif tipo_viaje == "Internacional":
            destino = "Bogota - España"
            precio_base = precio_internacional
        else:
            print("Tipo de viaje no valido")
            continue  # Vuelve al menu
        fecha = input("Fecha del viaje (YYYY-MM-DD): ")

        # Equipaje principal
        peso_principal = float(input("Peso del equipaje principal (kg): "))
        if peso_principal <= 20:
            costo_equipaje = 50000
            estado_equipaje = "Admitido"
        elif peso_principal <= 30:
            costo_equipaje = 70000
            estado_equipaje = "Admitido"
        elif peso_principal <= 50:
            costo_equipaje = 110000
            estado_equipaje = "Admitido"
        else:
            costo_equipaje = 0
            estado_equipaje = "No admitido"

        # Equipaje de mano
        lleva_mano = input("¿Lleva equipaje de mano? (sí/no): ").lower()
        if lleva_mano == "Si":
            peso_mano = float(input("Peso del equipaje de mano (kg): "))
            if peso_mano <= 13:
                estado_mano = "Admitido"
            else:
                estado_mano = "Rechazado"
        else:
            estado_mano = "No lleva"

        # Costo total
        costo_total = precio_base + costo_equipaje

        # Crear reserva y guardarla
        id_reserva = "COMP" + str(contador_id)
        contador_id += 1

        reserva = {
            "ID": id_reserva,
            "Nombre": nombre,
            "Destino": destino,
            "Fecha": fecha,
            "Equipaje Principal": estado_equipaje,
            "Equipaje de Mano": estado_mano,
            "Total": costo_total
        }
        reservas.append(reserva)
        print("\n Reserva registrada con exito")
        print("ID de la reserva: ", id_reserva)

    # Opcion 2: ver reporte
    elif opcion == "2":
        total_recaudado = 0
        total_pasajeros = len(reservas)
        print("\n Reporte de reservas ")
        for r in reservas:
            print(r)
            total_recaudado += r["Total"]
        print("\n Total de pasajeros :", total_pasajeros)
        print("Total recaudado :", total_recaudado)

    # Opcion 3: salir
    elif opcion == "3":
        print("Gracias por usar el sistema")
        break
    # Cualquier otra opcion
    else:
        print("Opcion no valida. Intenta de nuevo")