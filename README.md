## Integrantes grupo 4:

- Rafael Aros (201973034-7)  
- Felipe Fuentes (201973102-5)

## Requisitos
- Para instalar las librerías utilizadas en el proyecto se recomienda hacer uso del archivo `requirements.txt`, si no, posiblemente este no funcione.
```sh
pip install -r requirements.txt
```
- Es **obligatorio** configurar el ambiente para que el programa funcione correctamente, es decir, asignar las variables en un `.env`, para esto se da como ejemplo el `.env.example`.

```js
// El valor del token debe ser basado en base64
// e.g: 1F4c2GYEF44MLkwRvCLUdAEu6-F4alEkOekjbVW26JY=
TOKEN=
LOG_FILE=logs.log
```

## Uso
- Para hacer uso del programa basta con solo ejecutar el programa en el archivo principal:
```sh
python main.py
```

## Validación 

Como el requerimiento de la tarea no está completo del todo, se establecen requerimientos extra para un mejor desarrollo del programa.

### Requerimientos extra

1. El largo mínimo de la contraseña creada con el generador será de 8 caracteres.
2. El largo máximo de la contraseña creada con el generador será de 16 caracteres.
3. El almacenamiento seguro será en una base de datos (SQLite).
4. Se require de una cuenta para acceder al programa de manera segura, donde la contraseña se encuentra cifrada con MD5.
5. Cada cuenta tiene su propio llavero de contraseñas.
6. Los llaveros con contraseñas se encuentra encriptadas, es decir, son bidireccionales, permitiendo al dueño de la cuenta obtener el valor real.

Los límites de las contraseñas fueron considerados por la información del siguiente link: [Longitud de contraseñas](https://www.linkedin.com/pulse/2020-8-character-password-good-enough-colin-yeung/)

## Verificación
¿Cómo asegurarías que el programa cumpla el requerimiento?

#### Respuesta:
A través de las respectivas pruebas para los distintos requerimientos que se solicitan, además de los agregados por nosotros. 

## Organización del proyecto
Escogimos python para trabajar ya que era lo más simple de desarrollar y luego realizar pruebas.

Trabajamos en conjunto comunicandonos por Discord, utilizando Git y Slack para el almacenamiento y registro de archivos.

La separación de tareas fue la siguiente:
- Felipe: Creación del main, generador de contraseñas, README.
- Rafael: Base de datos, logs, tests.

## Evidencia flujo de trabajo
Como se solicitó, el proyecto se realizó con la integración de Git en Slack.

![Evidencia1](/images/SCR-20240412-svzm.jpeg)

![Evidencia2](/images/SCR-20240412-swve.png)

## Problemas encontrados
Como tenemos dominio de Python y de bases de datos, en particular no tuvimos problemas.
Destacar que las pruebas se definieron en conjunto porque en esa parte no teníamos tanta experiencia.





