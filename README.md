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
ε
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



