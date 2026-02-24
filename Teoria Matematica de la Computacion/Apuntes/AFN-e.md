# Autómatas Finitos No Deterministas con transiciones $\lambda$

Un autómata finito no deterministas con transiciones $\lambda$ es una tupla:

> $(\Sigma, Q, s, F, f:Qx(\Sigma U \{\lambda\})\rightarrow P(Q))$

donde la función de transición puede incluir movimientos sin consumir símbolos de entrada.  

## Clausura $\lambda$
Para un estado q, la clausura $\lambda(q)$ (cl(q)) es el conjunto de estados que pueden alcanzarse desde q utilizando únicamente transiciones $\lambda$.  

> Una cadena es aceptada si existe un camino que al consumir toda la cadena termine en un estado final.

