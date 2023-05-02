# 3d-bubbles

## Progreso primer spring 
  
  Durante el primer spring el único avance realizado fue el de mostrar algunos gráficos de burbujas con los archivos de datos introducidos a mano. Solo con el fin de aprender como funcionan los babiabubbles. 
  
## Progreso segundo spring

  En el segundo spring, el progreso esperado era el de poder introducir los archivos de datos de manera manual, pero hacer la multiplicación matricial de manera automatica mediante javascript, pero no fue posible ya que intenté hacerlo con archivos .xlsx y no encontré la manera. Por tanto, solo multipliqué los archivos en xlsx manualmente y mostré el archivo resultante como "cerealsrealdata.json" para poder verlo correctamente y ya si, tener un gráfico representativo del algoritmo.
  
## Progreso tercer spring
  
  Durante este período se cambió la idea de como hacer el calculo matricial y mediante el uso de python, guardando ambos archivos inicialmente en la carpeta del proyecto, es posible multiplicarlos y generar el nuevo archivo json con los datos para el index.html con el fin de mostrarlos.
  
**Problema de visualización en _github pages_**

  por algún motivo no es posible ver el resultado de la gráfica al mostrarlo en github pages, en la consola aparecer el siguiente error : 
  ```
  Failed to load resource: the server responded with a status of 404 ()
  ```
  en referencia al archivo json que carga los datos.
  Tal vez sea porque al intentar index.html utilizar el archivo de cerealsrealdata.json, este aún no se ha creado y por ello no aparece.

## Progreso cuarto spring

  Se ha creado un nuevo repositorio, la idea de representación de los datos ha avanzado, esta vez creando una caja a la que se le ha aplicado un evento para que al pulsarla, 
  pasemos al siguiente archivo de datos, con el fin de poder visualizar todos y cada uno de los datos.

  Encuentro problemas de visualizacion de datos a la hora de poder ver una cantidad muy grande de burbujas ya que cada vez crece mas y mas el grafico, haciendose incomodo con un tamaño superior a 75, por eso mis muestras son de ese tamaño.
  