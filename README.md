# Ejercicios Primeros y Siguentes

Integrantes:

- Eduardo Hincapie 
- Josh Lopez 
- Miguel Suarez 
- Alejandra Vargas

Se realiza un código para ejecutar según una gramática dada, el conjunto de primeros, siguientes y predicción con el propósito de aprender, tener claridad y poner a prueba los conocimientos sobre el análisis sintáctico descendente.

# 🧷 Requerimientos necesarios

Para correr el código creado en python, solo necesitamos un ambiente que sea capaz de correr el mismo, ya sea la terminal, un emulador web o visual studio code con el interprete instalado correctamente.

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
gram = {
    'S':  [['A', 'uno','B','C'], ['S','dos']],
    'A': [['B','C','D'], ['A','tres'], ['ε']],
    'B': [['D','cuatro','C','tres'],['ε']],
    'C': [['cinco','D','B'],['ε']],
    'D': [['seis'],['ε']],
}
```

Como resultado obtenemos el conjunto de primeros, siguientes y predicción:
```
Primeros(S): {'uno', 'tres', 'cuatro', 'cinco', 'seis'}
Primeros(A): {'ε', 'cuatro', 'tres', 'cinco', 'seis'}
Primeros(B): {'ε', 'seis', 'cuatro'}
Primeros(C): {'ε', 'cinco'}
Primeros(D): {'ε', 'seis'}
Siguientes(S): {'$', 'dos'}
Siguientes(A): {'uno', 'tres'}
Siguientes(B): {'$', 'uno', 'tres', 'cinco', 'seis', 'dos'}
Siguientes(C): {'$', 'uno', 'tres', 'seis', 'dos'}
Siguientes(D): {'$', 'uno', 'tres', 'cuatro', 'seis', 'dos'}
Predicción(S → A uno B C): {'cuatro', 'uno', 'tres', 'cinco', 'seis'}
Predicción(S → S dos): {'cuatro', 'uno', 'tres', 'cinco', 'seis'}
Predicción(A → B C D): {'cuatro', 'uno', 'tres', 'cinco', 'seis'}
Predicción(A → A tres): {'cuatro', 'tres', 'cinco', 'seis'}
Predicción(A → ε): {'uno', 'tres'}
Predicción(B → D cuatro C tres): {'seis', 'cuatro'}
Predicción(B → ε): {'$', 'uno', 'tres', 'cinco', 'seis', 'dos'}
Predicción(C → cinco D B): {'cinco'}
Predicción(C → ε): {'$', 'uno', 'tres', 'seis', 'dos'}
Predicción(D → seis): {'seis'}
Predicción(D → ε): {'$', 'uno', 'tres', 'cuatro', 'seis', 'dos'}
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
gram = {
    'S':  [['A', 'B', 'uno']],
    'A': [['dos', 'B'], ['ε']],
    'B': [['C', 'D'], ['tres'], ['ε']],
    'C': [['cuatro','A','B'],['cinco']],
    'D': [['seis'],['ε']],
}
```

Como resultado obtenemos el conjunto de primeros, siguientes y predicción:
```
Primeros(S): {'uno', 'tres', 'cuatro', 'dos', 'cinco'}
Primeros(A): {'dos', 'ε'}
Primeros(B): {'cuatro', 'ε', 'tres', 'cinco'}
Primeros(C): {'cinco', 'cuatro'}
Primeros(D): {'seis', 'ε'}
Siguientes(S): {'$'}
Siguientes(A): {'uno', 'tres', '$', 'seis', 'cuatro', 'cinco'}
Siguientes(B): {'uno', 'seis', 'tres', 'cuatro', '$', 'cinco'}
Siguientes(C): {'uno', 'seis', 'tres', 'cuatro', '$', 'cinco'}
Siguientes(D): {'uno', 'seis', 'tres', 'cuatro', '$', 'cinco'}
Predicción(S → A B uno): {'uno', 'tres', 'cuatro', 'dos', 'cinco'}
Predicción(A → dos B): {'dos'}
Predicción(A → ε): {'uno', 'seis', 'tres', 'cuatro', '$', 'cinco'}
Predicción(B → C D): {'cuatro', 'cinco'}
Predicción(B → tres): {'tres'}
Predicción(B → ε): {'uno', 'seis', 'tres', 'cuatro', '$', 'cinco'}
Predicción(C → cuatro A B): {'cuatro'}
Predicción(C → cinco): {'cinco'}
Predicción(D → seis): {'seis'}
Predicción(D → ε): {'uno', 'seis', 'tres', 'cuatro', '$', 'cinco'}
```
