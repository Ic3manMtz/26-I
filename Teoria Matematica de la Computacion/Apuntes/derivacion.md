# Derivación

Una derivación consiste en aplicar reglas de producción de la gramática hasta obtener una cadena formada únicamente por símbolos terminales. 

Ejemplo:s
> $S\rightarrow aSb|ab$

Derivación
> $S\rightarrow aSb \rightarrow aaSbb \rightarrow aaabbb$

## Derivación por la izquierda
El no terminal que se deriva es aquel más a la izquierda  
Ejemplo:
> $E \rightarrow E+E | id$

Derivación por la izquierda
> $E\rightarrow E+E \rightarrow E+E+E\rightarrow id+E+E\rightarrow id+id+E\rightarrow id+id+id$

## Derivación por la derecha
El no terminal que se deriva es aquel más a la derecha  
Ejemplo:
> $E\rightarrow E+E\rightarrow E+E+E\rightarrow E+E+id\rightarrow E+id+id\rightarrow id+id+id$

## Árbol de derivación
Un árbol de derivación representa de forma jerárquica la aplicación de las reglas de producción donde:
- La raíz del árbol corresponde al símbolo inicial
- Los nodos internos corresponden a símbolos no terminales
- Las hojas corresponden a símbolos terminales

> $S\rightarrow aSb | ab$  
> $S\rightarrow aSb\rightarrow aaSbb\rightarrow aaabbb$  
>
> Si tomamos las hojas del siguiente árbol podemos generar la cadena buscada


```mermaid
flowchart 
    S --> a
    S --> S1[S]
    S --> b

    S1 --> a1[a]
    S1 --> S2[S]
    S1 --> b1[b]

    S2 --> a2[a]
    S2 -->b2[b]
```

> $E\rightarrow E+E\rightarrow id+E\rightarrow id+E+E\rightarrow id+id+E\rightarrow id+id+id$

```mermaid
flowchart 

    E --> E1[E]
    E --> +(+)
    E --> E2[E]

    E1 --> id(id)
    
    E2 --> E3[E]
    E2 --> +1(+)
    E2 --> E4[E]

    E3 --> id1(id)
    E4 --> id2(id)
``` 

> Si obtenemos árboles distintes al hacer derivaciones por la izquierda y por la derecha podemos decir que hay ``` ambiguedad ```

Ejemplo:
> $S\rightarrow if\space E\space then\space S|if\space E\space then\space S\space else\space S|a$  
>
> Cadena a generar ```if E then if E then a else a```
>
> $S\rightarrow ifEthenS\rightarrow if\space E\space then\space if\space E\space then\space S\space else\space S\rightarrow if\space E\space then\space if\space E\space then\space a\space else\space S\rightarrow if\space E\space then\space if\space E\space then\space a\space else\space a$

Ejercicio:
> Gramática  
> $S\rightarrow SS | (S) | \lambda$  
>
> Cadena a generar ```()()```

### Derivación por la izquierda
> $S\rightarrow SS\rightarrow (S)S\rightarrow (\lambda)S\rightarrow ()(S)\rightarrow ()(\lambda)$

```mermaid
flowchart
    S --> S1[S]
    S --> S2[S]

    S1 --> p1("(")
    S1 --> S3[S]
    S1 --> p2(")")

    S3 --> l1("λ")

    S2 --> p3("(")
    S2 --> S4[S]
    S2 --> p4(")")

    S4 --> l2("λ")
```

### Derivación por la derecha
> $S\rightarrow SS\rightarrow S(S)\rightarrow S(\lambda)\rightarrow (S)()\rightarrow (\lambda)()$