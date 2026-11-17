Módulo: utilidades.py - Escrito por: Jaiver Rodríguez Córdoba
# Este módulo tiene las funciones chiquitas que ayudan a los otros módulos

DIAS_MES = 30

# Recibe: afiliados, documento, dia
# Devuelve: mensaje de si se registró o por qué no se pudo
def registrar_asistencia(afiliados, documento, dia, dias_mes=DIAS_MES):
    if documento in afiliados:
        datos = afiliados[documento]
        dias = datos[3]
        if dia < 1 or dia > dias_mes:
            return f"El día debe estar entre 1 y {dias_mes}"
        if dia in dias:
            return "Ese día ya estaba registrado"
        dias.append(dia)
        return f"Asistencia registrada para {datos[0]}"
    return "No existe un afiliado con ese documento"

# Recibe: datos del afiliado
# Devuelve: porcentaje de asistencia con 2 decimales
def porcentaje_asistencia(datos, dias_mes=DIAS_MES):
    dias = datos[3]
    return round(len(dias) / dias_mes * 100, 2)

# Recibe: documento y datos del afiliado
# Devuelve: texto listo para mostrar en pantalla
def texto_afiliado(documento, datos):
    nombre, plan, peso, dias = datos
    return f"{documento} | {nombre} | plan {plan} | peso {peso} kg | asistencias {len(dias)}"

# Recibe: un número
# Devuelve: True si es mayor que 0, False si no
def valor_positivo(numero):
    return numero > 0

# Recibe: plan que escribió el usuario y los planes que existen
# Devuelve: True si el plan existe, False si no
def plan_valido(plan, planes):
    return plan in planes

if __name__ == "__main__":
    prueba = {"100": ["Ana Perez", "basico", 60.5, [1, 2]]}
    print(registrar_asistencia(prueba, "100", 5))
    print(registrar_asistencia(prueba, "100", 5))
    print(registrar_asistencia(prueba, "100", 45))
    print(registrar_asistencia(prueba, "100", 999))
    print(porcentaje_asistencia(prueba["100"]))
    print(texto_afiliado("100", prueba["100"]))
    print(valor_positivo(3), valor_positivo(0))
    print(plan_valido("plus", {"basico": 1, "plus": 2}))