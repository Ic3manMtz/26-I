# Introducción

+ **Computadora** .- Una máquina electrónica que recibe datos de entrada y los procesa para convertirlos en información útil.
+ **Computación** .- Conjunto de conocimientos científicos y técnicos que se encargan del estudio del procesamiento de la información por medio de computadoras.
+ **Teoría de la computación** .- Conjunto de conocimientos que se centran en el estudio de la abstracción de los procesos que ocurren en la realidad con el fin de reproducirlos con ayuda de sistemas formales, es decir, mediante símbolos e instrucciones lógicas, reconocidos por el ser humano, con capacidad de ser modeladas en las limitaciones de los dispositivos.
+ **Conjunto** .- Colección de símbolos sin repetición. Existen varias formas de representarlos:
  + Listando sus elementos.
  + Describiendo sus elementos.

## Operaciones con conjuntos
+ Unión 
+ Intersección 
+ Diferencia
+ Complemento
+ Potencia P(A): El conjunto de todos los *subconjuntos* de A.
+ Concatenación: ${ wx | w\in A y x \in B}$
+ Producto cruz AxB: Conjunto de todos los pared ordenados (a,b) tales que a pertenece a A y b pertenece a B.

> Un **alfabeto** es una colección finita y no vacía de símbolos y se representa por $\Sigma$ 

> Una **cadena** es una secuencia finita de simbolos sobre un alfabeto $\Sigma$. Sea $\omega$ una cadena sobre $\Sigma$: 
> + Cadena vacía: $\lambda$ (cadena que no tiene símbolos)
> + Concatenación: si $\omega$ y $z$ son cadenas la concatenación de $z$ en $\omega$ se denota $\omega$*z*.
> + Potencia de una cadena: $\omega^n$. Si n=0 $\lambda$. En caso contrario, $\omega\omega^{n-1}$
> + Longitud de una cadena: Número de símbolos que contiene una cadena. Se representa por $|\omega|$
> + Prefijo y sufijo de una cadena: Sea $\omega$ y $x$ cadenas, se dice que $x$ es un prefijo de $\omega$ si existe una cadena $y$ tal que $\omega=xy$. De manera análoga, $x$ es un sufijo de $\omega$ si existe una cadena $y$ tal que $\omega=yx$

> Un **lenguaje** es un conjunto de cadenas formadas a partir de un mismo alfabeto.
> + $\emptyset$: Lenguaje vacío, no contiene ninguna cadena.
> + $\Sigma^*$: Lenguaje de todas las cadenas que pueden formarse sobre el alfabeto $\Sigma$. Contiene la cadena vacía $\lambda$.
> + $\Sigma^+$: Lenguaje de todas las cadenas que pueden formarse sobre el alfabeto $\Sigma$. No contiene la cadena vacía.

### Problema
Consiste en determinar si una cadena pertenece o no a un lenguaje. ESte tipo de problema de denomina **problema de decisión**

## Tipos de lenguajes
+ Lenguajes regulares
+ Lenguajes libres de contexto
+ Lenguajes dependientes del contexto
+ Lenguajes recursivamente numerables
  
## Lenguajes regulares
Sea $\Sigma$ un alfabeto. El conjunto de los lenguajes regulares su $\Sigma$ se define recursivamente de la siguiente manera:
+ El lenguaje vacío $\emptyset$ es un lenguaje regular.
+ El lenguaje que contiene únicamente la cadena vacía $\lambda$, es un lenguaje regular.
+ Para todo símbolo $a\in\Sigma$ es lenguaje regular.
+ Si A y B son lenguajes regulares, entonces $AUB, AB y A^+$ son lenguajes regulares.
+ Ningún otro lenguajes es regular.

Un lenguaje regular puede ser represenado mediante una **expresión regular**

## Expresión regular
Sea $\Sigma$ un alfaneto. Una expresión regular sobre $\Sigma$ se define recursivamente:
+ $\emptyset,\lambda son expresiones regulares$
+ Para todo símbolo $a\in\Sigma$, a es una expresión regular.
+ Si r y s son expresiones regulares $rUs, rs, r^*, r|s$ son expresiones regulares.
+ Ninguna otra secuencia de símbolos es una expresión regular

> + $r=\emptyset \Rightarrow L(r)=\emptyset$ 
> + $r=\lambda \Rightarrow L(r)=\{\lambda\}$
> + $r=a \Rightarrow L(r)=\{a\}$
> + $r=b \Rightarrow L(r)=\{b\}$
> + $r=a|b \Rightarrow L(r)=\{a,b\}$
> + $r=ab \Rightarrow L(r)=\{ab\}$
> + $r=(a|b)a \Rightarrow L(r)=\{aa,ba\}$
> + $r=a^* \Rightarrow L(r)=\{\lambda,a,aa,aaa,\dots\}$
> + $r=(ab)^* \Rightarrow L(r)=\{\lambda,ab,abab,ababab,\dots\}$ 
> + $r=(a|b)ab \Rightarrow L(r)=\{w\in\Sigma^* | w\space termina\space ab\}$
