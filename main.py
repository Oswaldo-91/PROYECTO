"""
"""
Proyecto: Bitácora de Consumo de Agua
Autor: ASHLEY ANNABELLE CARRERA RUIZ 
Fecha: [09/08/2025]
Descripción: Registro y análisis de consumo de agua usando Python.
"""

# Resto del código igual...

"""


from statistics import mean

def pedir_float(mensaje: str) -> float:
    """Pide un número con validación. Repite hasta que el usuario ingrese un positivo.
    - Estructura repetitiva: while (para validar repetidamente)
    - Estructura lógica: if para validar condiciones
    """
    while True:
        dato = input(mensaje).strip()
        try:
            valor = float(dato.replace(",", "."))
            if valor <= 0:
                print("❌ Ingresa un número mayor a cero.")
                continue
            return valor
        except ValueError:
            print("❌ Entrada no válida. Escribe solo números (ej. 12.5).")

def mostrar_menu() -> None:
    print("\n=== Bitácora de Consumo de Agua ===")
    print("1) Registrar consumo de hoy (litros)")
    print("2) Definir meta diaria (litros)")
    print("3) Ver promedio y comparar con meta")
    print("4) Listar consumos registrados")
    print("5) Salir")

def main():
    consumos = []  # lista de floats
    meta = None    # meta en litros (float)

    while True:  # Estructura repetitiva: menú hasta que el usuario decida salir
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ").strip()

        if opcion == "1":
            # Registrar un consumo
            litros = pedir_float("Ingresa el consumo del día (litros): ")
            consumos.append(litros)
            print(f"✅ Guardado: {litros} L")

        elif opcion == "2":
            # Definir una meta diaria
            meta = pedir_float("Define tu meta diaria de consumo (litros): ")
            print(f"🎯 Meta fijada: {meta} L/día")

        elif opcion == "3":
            if len(consumos) == 0:
                print("ℹ️ Aún no hay consumos registrados.")
                continue

            # Calcular promedio con for/mean
            # Aquí usamos mean por claridad, pero podríamos usar:
            # promedio = sum(consumos) / len(consumos)
            promedio = mean(consumos)
            print(f"📊 Promedio actual: {promedio:.2f} L/día (basado en {len(consumos)} registro(s))")

            # Estructura lógica: comparar con meta si existe
            if meta is not None:
                if promedio > meta:
                    print("⚠️ Alerta: estás por encima de tu meta. Considera reducir el consumo.")
                elif promedio == meta:
                    print("✅ Estás exactamente en tu meta. ¡Buen equilibrio!")
                else:
                    print("💧 Bien: estás por debajo de tu meta.")
            else:
                print("ℹ️ Aún no has definido una meta (opción 2).")

        elif opcion == "4":
            if len(consumos) == 0:
                print("ℹ️ No hay consumos para listar.")
            else:
                print("🧾 Consumos registrados (litros):")
                # Estructura repetitiva: for para recorrer y mostrar
                for i, c in enumerate(consumos, start=1):
                    print(f"  Día #{i}: {c} L")

        elif opcion == "5":
            print("👋 Fin del programa. ¡Gracias!")
            break

        else:
            print("❌ Opción inválida. Elige un número del 1 al 5.")

if __name__ == "__main__":
    main()
