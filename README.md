# Ejercicios Primeros y Siguentes

Integrantes:

- Eduardo Hincapie 
- Josh Lopez 
- Miguel Suarez 
- Alejandra Vargas

# 🧷 Requerimientos necesarios

Se realiza un código para ejecutar según una gramática dada, el conjunto de primeros, siguientes y producción con el propósito de aprender, tener claridad y poner a prueba los conocimientos sobre el análisis sintáctico descendente.

## 💥 Uso:

Como caso base utilizamos una gramática sencilla la cual se encuentra directamente en el código, por lo que no necesita ningún parámetro de entrada al ejecutarlo.

Como ejemplo base tenemos la siguiente gramática:

    S -> A uno B C
    S -> S dos
    A -> B C D
    A -> A tres
    A -> ε
    B -> D cuatro C tres
    B -> ε
    C -> cinco D B
    C -> ε
    D -> seis
    D -> ε

En el código:
```
grammar = {
    'S':  [['A', 'uno','B','C'], ['S','dos']],
    'A': [['B','C','D'], ['A','tres'], ['ε']],
    'B': [['D','cuatro','C','tres'],['ε']],
    'C': [['cinco','D','B'],['ε']],
    'D': [['seis'],['ε']],
}
```

Como resultado obtenemos el conjunto de primeros, siguientes y producción:
```
gra
```

Como segundo ejemplo tenemos la siguiente gramática:

    S -> A B uno
    A -> dos B
    A -> ε
    B -> C D
    B -> tres
    B -> ε
    C -> cuatro A B
    C -> cinco
    D -> seis
    D -> ε

En el código:
```
grammar = {
    'S':  [['A', 'B', 'uno'],
    'A': [['dos', 'B'], ['ε']],
    'B': [['C', 'D'], ['tres'], ['ε']],
    'C': [['cuatro','A','B'],['cinco']],
    'D': [['seis'],['ε']],
}
```

Como resultado obtenemos el conjunto de primeros, siguientes y producción:
```
gra
```
