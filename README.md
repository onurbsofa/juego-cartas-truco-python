# juego-cartas-truco-python
Este proyecto nació de la  necesidad de mejorar 
mi lógica de programación y de ayuda para profundizar en conceptos de OOP.
También me ayuda a entender sobre 
entornos virtuales y sobre como usar bash o powershell para operar en los entornos

## Configuración 
Primero cree un entorno virtual para poder manipular paquetes y modulos mas facilmente 
python -m venv Truco.py-env

Después entre en la carpeta abrí una terminal en la powershell y  ejecute el comando para que se active el entorno
c:/Users/brufa/Documents/Truco.py-env/Scripts/Activate.ps1

## Desarrollo del proyecto

### Clases
*Empecé creando todas las clases necearías para representar el juego* 
- Una para las cartas que consiste en una clase con dos arrays dentro que representan los palos y los valores 
- Otra par representar el jugador con su nombre, las partidas ganadas y un array para el mazo
- Otra para representar la mesa llamada Deck que se encarga de crear un mazo con todas las cartas, lo mezcla y reparte 
- y por ultimo una clase para el juego donde se crean todas las funcionalidades para que el juego se de 

### Métodos
*Cada objeto(clase) tienen su métodos que son como las propiedades en la vida real
Por lo tanto para recrear el truco necesito:*
- La clase carta tiene como método especial __init__ su valor y su palo( el metodo init se ejecuta cuando se crea una instancia)
- el método init del Deck crea un mazo apenas se crea la instancia de la clase 
- Deck también tiene dos métodos importantes que mezclan y reparten las cartas 
- La clase del jugador tiene un metodo init para almacenar todos los valores del jugador necesarios como el mazo de cartas, el nombre, las partidas ganadas y los puntos
- luego tres métodos básicos uno para agarrar una carta, otra para jugar una carta y otro que muestra el mazo en consola
- y por ultmo la clase truco que es donde se recrea el juego por ahora solo crea dos instancias de jugadores les reparte cartas y muestra las cartas por consola
*Hay un error en el programa que hace que las cartas repartidas sean siempre las mismas nose si po la cache o por algo del metodo que mezcla*