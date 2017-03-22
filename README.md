# Repositorio de bots usados como ejemplo en la conferencia
Repositorio de bots usados en la conferencia https://goo.gl/0xXbk6

# Bots echo
### [Ejemplo 1](https://github.com/i32ropie/conferencia-bots-telegram/blob/master/Ejemplos/echo1.py)

Simplemente es un ejemplo muy básico que responde a todos los mensajes con el mismo texto que se le envie.

### [Ejemplo 2](https://github.com/i32ropie/conferencia-bots-telegram/blob/master/Ejemplos/echo2.py)

Mismo código pero ahora también imprimos por pantalla información de los mensajes recibidos.

# Bots control de usuario
### [Ejemplo 1](https://github.com/i32ropie/conferencia-bots-telegram/blob/master/Ejemplos/control_usuario1.py)

En este ejemplo en el listener solo imprimimos información del mensaje recibido y comenzamos a manejar comandos. Empezamos por el más básico de todos, el comando `/start` que es el que recibe nuestro bot siempre que alguien lo usa por primera vez. El ejemplo usado lo único que hace es saludar al usuario.

### [Ejemplo 2](https://github.com/i32ropie/conferencia-bots-telegram/blob/master/Ejemplos/control_usuario2.py)

Aquí introducimos un control de usuarios básico. Consistirá en almacenar en un fichero de texto plano el ID de cada conversación que usa `/start` y considerar los IDs almacenados como usuarios. Para facilitar la compresión, haremos uso de una función que dado un ID compruebe si es usuario o no y de otra función que se encargará de añadir los nuevos usuarios a nuestro archivo y a nuestra lista de usuarios conocidos. Como curiosidad, a la hora de leer el fichero utilizaremos list comprehension.

### [Ejemplo 3](https://github.com/i32ropie/conferencia-bots-telegram/blob/master/Ejemplos/control_usuario3.py)

Por desgracia nuestro bot no agradará a todo el mundo siempre, por lo que puede ser útil el contar con un comando para dar de baja a los usuarios del bot. Para ello manejaremos el comando `/stop` y actualizaremos nuestra función de añadir usuarios para que dependiendo de un parámetro más podamos usarla tanto para añadir como para borrar usuarios.
