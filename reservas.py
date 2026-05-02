# ================================
# CLASES PRINCIPALES
# ================================

class Cliente:
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento


class Servicio:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


class Reserva:
    def __init__(self, cliente, servicio):
        self.cliente = cliente
        self.servicio = servicio

    def mostrar_reserva(self):
        return f"Cliente: {self.cliente.nombre} - Servicio: {self.servicio.nombre} - Precio: {self.servicio.precio}"


# ================================
# EXCEPCIÓN PERSONALIZADA
# ================================

class ErrorReserva(Exception):
    pass


# ================================
# FUNCIÓN PARA GUARDAR ERRORES
# ================================

def guardar_error(mensaje):
    with open("errores.log", "a") as archivo:
        archivo.write(mensaje + "\n")


# ================================
# FUNCIÓN PRINCIPAL
# ================================

def crear_reserva():
    try:
        nombre = input("Ingrese el nombre del cliente: ")
        documento = input("Ingrese el documento: ")

        if nombre == "" or documento == "":
            raise ErrorReserva("Datos del cliente incompletos")

        cliente = Cliente(nombre, documento)

        servicio_nombre = input("Ingrese el servicio: ")
        
        try:
            precio = float(input("Ingrese el precio del servicio: "))
        except ValueError:
            raise ErrorReserva("El precio debe ser un número válido")

        servicio = Servicio(servicio_nombre, precio)

        reserva = Reserva(cliente, servicio)

    except ErrorReserva as e:
        print("Error:", e)
        guardar_error(str(e))

    except Exception as e:
        print("Error inesperado:", e)
        guardar_error("Error inesperado: " + str(e))

    else:
        print("\nReserva creada con éxito:")
        print(reserva.mostrar_reserva())

    finally:
        print("\nProceso finalizado.")


# ================================
# EJECUCIÓN
# ================================

if __name__ == "__main__":
    crear_reserva()