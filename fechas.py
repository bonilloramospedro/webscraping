from datetime import datetime, timedelta

# Obtener la fecha y hora actual
fecha_actual = datetime.now()
print("Fecha y hora actual:", fecha_actual)

# Crear una fecha específica
fecha_personalizada = datetime(2022, 1, 1)
print("Fecha personalizada:", fecha_personalizada)

# Sumar o restar días a una fecha
nueva_fecha = fecha_personalizada + timedelta(days=-2)
print("Fecha personalizada + 5 días:", nueva_fecha)

# Extraer componentes de una fecha
print("Año:", fecha_actual.year)
print("Mes:", fecha_actual.month)
print("Día:", fecha_actual.day)
print("Hora:", fecha_actual.hour)
print("Minuto:", fecha_actual.minute)
print("Segundo:", fecha_actual.second)

# Formatear una fecha como una cadena
cadena_formateada = fecha_actual.strftime("%m/%Y-%d %H:%M:%S")
print("Fecha formateada:", cadena_formateada)

fecha1 = datetime(2023, 1, 1)
fecha2 = datetime(2022, 1, 1)

if fecha1 < fecha2:
    print("fecha1 es anterior a fecha2")
elif fecha1 == fecha2:
    print("fecha1 es igual a fecha2")
else:
    print("fecha1 es posterior a fecha2")