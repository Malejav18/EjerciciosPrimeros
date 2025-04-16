# Calcular el conjunto de Primeros de un símbolo 'simb'
def primeros(simb, gram, primeros_sets):
    # Inicializamos el conjunto Primeros vacío para 'simb'
    primeros_sets[simb] = set()
    
    # Si 'simb' es un terminal 
    if simb.islower():
        primeros_sets[simb].add(simb)
        return primeros_sets[simb]
    
    # Si 'simb' es no terminal
    for production in gram.get(simb, []):  # Para cada producción de 'simb'
        for prod_simb in production:  # Para cada símbolo en la producción
            primeros_prod = primeros(prod_simb, gram, primeros_sets)
            primeros_sets[simb].update(primeros_prod - {'ε'})  # Añadimos todos excepto ε
            if 'ε' not in primeros_prod:
                break  # Si no hay ε, seguimos
        else:
            # Se añade ε al conjunto
            primeros_sets[simb].add('ε')
    return primeros_sets[simb]

# Calcular el conjunto de Siguientes de un símbolo 'simb'
def siguientes(simb, gram, primeros_sets, siguientes_sets, inicio):
    # Si el conjunto ya fue calculado, lo devolvemos
    if simb in siguientes_sets:
        return siguientes_sets[simb]
    
    siguientes_sets[simb] = set()
    
    # Si es el símbolo inicial, se agrega el símbolo de fin de cadena $
    if simb == inicio:
        siguientes_sets[simb].add('$')
    
    for left, productions in gram.items():
        for production in productions:
            if simb in production:
                index = production.index(simb)  # Posición del simbolo en la producción
                # Si hay un símbolo a la derecha 
                if index + 1 < len(production):
                    siguientes_sets[simb].update(
                        primeros(production[index + 1], gram, primeros_sets) - {'ε'}
                    )
                # Si 'simb' es el último o lo que sigue es ε
                if index + 1 == len(production) or 'ε' in primeros(production[index + 1], gram, primeros_sets):
                    siguientes_sets[simb].update(siguientes(left, gram, primeros_sets, siguientes_sets, inicio))
    return siguientes_sets[simb]

# Calcular el conjunto Predicción para cada producción de la gramática
def prediccionesC(gram, primeros_sets, siguientes_sets):
    predicciones = {}
    for nt, producciones in gram.items():
        for produccion in producciones:
            key = (nt, tuple(produccion))  # Clave compuesta: (no_terminal, producción)
            pred = set()
            i = 0
            while i < len(produccion):
                simb = produccion[i]
                primeros_simb = primeros(simb, gram, primeros_sets)
                pred.update(primeros_simb - {'ε'})  # Añadimos todos excepto ε
                if 'ε' not in primeros_simb:
                    break
                i += 1
            else:
                # Si todos los símbolos pueden producir ε, añadimos el conjunto Siguientes del no terminal
                pred.update(siguientes_sets[nt])
            predicciones[key] = pred
    return predicciones

# Gramática ejemplo
gram = {
    'S':  [['A', 'B', 'uno']],
    'A': [['dos', 'B'], ['ε']],
    'B': [['C', 'D'], ['tres'], ['ε']],
    'C': [['cuatro','A','B'],['cinco']],
    'D': [['seis'],['ε']],
}

primeros_sets = {}
siguientes_sets = {}
inicio = 'S'

for no_terminal in gram:
    primeros(no_terminal, gram, primeros_sets)
    print(f'Primeros({no_terminal}): {primeros_sets[no_terminal]}')

for no_terminal in gram:
    siguientes(no_terminal, gram, primeros_sets, siguientes_sets, inicio)
    print(f'Siguientes({no_terminal}): {siguientes_sets[no_terminal]}')

predicciones = prediccionesC(gram, primeros_sets, siguientes_sets)

for (nt, prod), pred in predicciones.items():
    prod_str = ' '.join(prod)  # Convertimos la producción a string para mejor visualizacion
    print(f'Predicción({nt} → {prod_str}): {pred}')
