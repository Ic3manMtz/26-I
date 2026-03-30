# Máquinas de Turing

- Modelo matemático propuesto por Turing en 1936.
- Formaliza el concepto de algoritmo y estudiar que problemas se pueden resolver de manera automática mediante un procedimiento finito.
  
Estructura  
- Cinta (**celdas**) de memoria
- Cabezal (**lector-escritor**) que puede leer el símbolo de una celda, escribir un nuevo símbolo y desplazarse a la izquierda o derecha
- Conjunto de estados
- Estado inicial
- Estados de aceptación
- Función de transición

$$ M=(Q,\Sigma,\Gamma,f,q_0,B,F) $$
donde  
- Q es el conjunto de estados
- $\Sigma$ es el alfabeto de entrada
- $\Gamma$ es el alfabeto de la cinta $\Sigma\subseteq\Gamma$
- $f:Qx\Gamma\rightarrow Qx\Gamma x\{L,R\}$
- q_0 es el estado inicial
- $B\subseteq\Gamma$
- $F\subseteq Q$

### Ejemplo $L=\{a^nb^n | n\geq0\}$

La máquina de Turing verifica que cada ```a``` tenga su correspondiente ```b```.  
1) Buscar la primer ```a``` sin marcar y cambiarla por ```X```.
2) Avanzar a la derecha hasta encontrar una ```b``` sin marcar y cambiarlo por ```Y```.
3) Regresar al inicio de la cadena.
4) Repetir el proceso.
5) Aceptar si todos los símbolos han sido marcados

**Transacciones**

$$
(q_0,a) \rightarrow (q_1,X,R) \\
(q_1,a) \rightarrow (q_1,a,R) \\
(q_1,Y) \rightarrow (q_1,Y,R) \\
(q_1,b) \rightarrow (q_2,Y,L) \\
(q_2,a) \rightarrow (q_2,a,L) \\
(q_2,Y) \rightarrow (q_2,Y,L) \\
(q_2,X) \rightarrow (q_0,X,R) \\
(q_0,Y) \rightarrow (q_0,Y,R) \\
(q_0,B) \rightarrow (q_f,B,R) \\
$$