# Expresiones regulares

+ $r=(+|-|*|/|\%) \Rightarrow L(r)=\{ +,-,*,/,\% \}$
+ $r=(>|<|>=|<=) \Rightarrow L(r)=\{ >,<,>=,<= \}$
+ $r=(0|1|2|3|\dots|9)^+ \Rightarrow L(r)=\{ 0,00,1,10,\dots \}$

### Expresiones regulares en python

> Creación de un entorno virtual `python -m venv .venv`

Funciones en re
+ re.match $\rightarrow$ re.match(patron, cadena) $\rightarrow$ re.match(r"abc","zabc")
+ re.search
+ re.findall

Símbolos especiales en los patrones (expresiones)
+ `|` Operador Unión
+ `[...]` Clase
+ `^` Inicio de la cadena
+ `$` Fin de la cadena
+ `.` Cualquier caracter

```
r.math(r"[abc]*a[abc]*b[abc]*","xxabxx")
```
> Busca este patrón como subcadena de una cadena dada

$(a|b|c)^*a(a|b|c)^*b(a|b|c)^*$


```
r.math(r"^[abc]*a[abc]*b[abc]*$","xxabxx")
```
> Busca que la cadena pertenezca exactamente con la expresión regular


L={Todas las cadenas en $\Sigma=\{ a,b,c \}$ con al menos una a y al menos una b}
$(a|b|c)^*\space a(a|b|c)^*\space b(a|b|c)^*\space|\space(a|b|c)^*\space b(a|b|c)^*\space a(a|b|c)^*$