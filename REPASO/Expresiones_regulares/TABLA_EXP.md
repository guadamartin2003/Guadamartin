
| Secuencia de escape| representación | 
|-------------	|----------	|
| \n | salto de línea | 
| \t | Tab o cambio de pestaña |
| \s | espacio |
| \' | Comillas simples |
| \" | Comillas dobles |   


| Metacaracter| Significado | 
|-------------	|----------	|
| ^	| Inicio de línea | 
| $ | Fin de linea |
| \A | Inicio de texto |
| \Z | Fin de texto |
| . | Coincide con cualquier caracter en una línea dada | 


| Metacaracter| Significado | 
|-------------	|----------	|
|  *	| Cero o más: todas las ocurrencias de un dado substring |	
|  +	| Una o más ocurrencias del patrón|	
|? | Cero o una|
|{n} | Exactamente n veces|
|{n,m} | Por lo menos n pero no más de m veces.|


| Metacaracter| Significado | 
|-------------	|----------	|
|  \w	| Caracter alfanumércio|
|  \W	| Caracter NO alfanumércio|	
|  \d	| Caracter numércio|	
|  \D	| Caracter NO numércio|	
|  \s	| Un espacio, de cualquier tipo (\t\n\r\f)|	
|  \S	| Cualquier caracter que no sea un espacio|	


- El rango [a-d] equivale al [abcd]
    - El rango [1-10] equivale al substring [12345678910]
    - El rango [Dd] equivale a buscar una D mayúscula y una d minúscula