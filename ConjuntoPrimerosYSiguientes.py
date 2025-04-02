# Función para calcular el conjunto First
def first(symbol, grammar, first_sets):
    if symbol in first_sets:
        return first_sets[symbol]
    
    first_sets[symbol] = set()
    
    if symbol.islower():  # Si es terminal
        first_sets[symbol].add(symbol)
        return first_sets[symbol]
    
    for production in grammar.get(symbol, []):
        for prod_symbol in production:
            first_prod = first(prod_symbol, grammar, first_sets)
            first_sets[symbol].update(first_prod - {'ε'})
            if 'ε' not in first_prod:
                break
        else:
            first_sets[symbol].add('ε')
    
    return first_sets[symbol]

# Función para calcular el conjunto Follow
def follow(symbol, grammar, first_sets, follow_sets, start_symbol):
    if symbol in follow_sets:
        return follow_sets[symbol]
    
    follow_sets[symbol] = set()
    
    if symbol == start_symbol:
        follow_sets[symbol].add('$')  # Símbolo de fin de cadena
    
    for left, productions in grammar.items():
        for production in productions:
            if symbol in production:
                idx = production.index(symbol)
                if idx + 1 < len(production):
                    follow_sets[symbol].update(first(production[idx + 1], grammar, first_sets) - {'ε'})
                if idx + 1 == len(production) or 'ε' in first(production[idx + 1], grammar, first_sets):
                    follow_sets[symbol].update(follow(left, grammar, first_sets, follow_sets, start_symbol))
    
    return follow_sets[symbol]

# Ejemplo de uso
grammar = {
    'S':  [['A', 'uno','B','C'], ['S','dos']],
    'A': [['B','C','D'], ['A','tres'], ['ε']],
    'B': [['D','cuatro','C','tres'],['ε']],
    'C': [['cinco','D','B'],['ε']],
    'D': [['seis'],['ε']],
}

first_sets = {}
follow_sets = {}
start_symbol = 'S'

# Calculamos First y Follow
for non_terminal in grammar:
    first(non_terminal, grammar, first_sets)

for non_terminal in grammar:
    follow(non_terminal, grammar, first_sets, follow_sets, start_symbol)

# Comparar conjuntos First y Follow
for non_terminal in grammar:
    print(f'First({non_terminal}): {first_sets[non_terminal]}')
    print(f'Follow({non_terminal}): {follow_sets[non_terminal]}')
    print(f'First({non_terminal}) == Follow({non_terminal}): {first_sets[non_terminal] == follow_sets[non_terminal]}')
