pysync 
==========

Requerimientos:

+ pip install lib_sysblack.
+ para windows robocopy en las variables de entorno.
+ para linux rsyn en las variables de entorno.




Compilacion en windows.
pyinstaller.exe --onefile --name pysync --icon=recursos/icon.ico main.py


Ejemplo de ejecucion.

+ pysync -v
+ pysync -d
+ pysync -t 
+ pysync -v -d -c fileconfig.cfg

+ /XF *.pst /MIR /R:3 /W:10
+ /XF *.pst /XO /E /R:3 /W:10



programar tareaen windows. 

Crear una tarea programada para ejecutar el bloc de notas todos los días a las 11:00 a.m.

+ C:\> schtasks /create /TN “Ejecutar espejo” /TR notepad.exe /SC DAILY /ST 11:00:00
