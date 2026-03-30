# Gramáticas Recursivas por la izquierda

Una gramática recursiva por la izquierda es aquella que tiene reglas similares a:  
> $A\rightarrow A\alpha|B$  

donde $\alpha$ y $\beta$ son cadena de terminales y no terminales. Para eliminar la recursividad podemos usar:  
> $A\rightarrow BA'$  
> $A'\rightarrow \alpha A'|\lambda$

Por ejemplo:  
> $A\rightarrow AR|AT|b$  

Queda de la siguiente manera:  
> $A\rightarrow AR|AT|b$  
> $A\rightarrow A(R|T) | b$  
> 
> donde (R|T) es $\alpha$ y b es $\beta$   
> $A\rightarrow bA'$  
> $A'\rightarrow (R|T)A'|\lambda$  
> 
> al final tenemos  
> $A\rightarrow bA'$  
> $A'\rightarrow RA'|TA'|\lambda$

### Ejercicio 1

$$
E\rightarrow E+T|E-T|T \\
T\rightarrow T*F|T/F|T\%F|F \\
F\rightarrow N|id \\
N\rightarrow 0|1
$$

Tomando las reglas 
$$
E\rightarrow E+T|E-T|T \\
T\rightarrow T*F|T/F|T\%F|F
$$

podemos expresarlas de la siguiente manera
$$
E\rightarrow E(+T|-T)|T \\
T\rightarrow T(*F|/F|\%F)|F
$$

usando la regla para remover la recursión por la izquierda obtenemos
$$
E\rightarrow TE' \\
E'\rightarrow +TE'|-TE'|\lambda \\

T\rightarrow FT' \\
T'\rightarrow *FT'|/FT'|\%FT|\lambda
$$

Por lo que la gramática final nos queda

$E\rightarrow TE'$  
$E'\rightarrow +TE'|-TE'|\lambda$

$T\rightarrow FT'$  
$T'\rightarrow *FT'|/FT'|\%FT|\lambda$

$F\rightarrow N|id$  
$N\rightarrow 0|1$

### Ejercicio 2

Gramática
>$S\rightarrow Aa|Bb|b$  
>$A\rightarrow Ac|Sd|\lambda$  
>$B\rightarrow Bc|Bd|e|\lambda$

