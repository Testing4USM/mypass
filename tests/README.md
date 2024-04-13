# Pruebas

## Estrategia

- Realizamos las pruebas con ayuda de la librería `pytest`. 
- Se ejecutarán las pruebas en conjunto utilizando `TDD`, es decir que se realizan pruebas unitarias antes de escribir código para detectar errores tempranamente.
- Para las pruebas relacionadas con el usuario (cuenta) se hicieron uso de `fixtures`.

## Ejecución de los `tests`
- Para ejecutar los `tests` basta con hacer uso del comando en consola:
```
pytest
```

### - Pruebas de usuarios

#### PRUEBA DE INSTANCIA DE USUARIO NULA
- ID_test: `test_empty_user`
- Input: `empty_user` (fixture de usuario sin estado de sesión)
- Resultado esperado: Se espera que los campos dentro de la clase de usuario obtenidos sean `None`.
- Resultado obtenido: Los campos obtenidos son `None`.
- Fallo o éxito:
    - **Falla**: Alguno de los campos no es `None`.
    - **Éxito**: Todos los camposo son `None`.

#### PRUEBA DE INSTANCIA DE REGISTRO DE USUARIO
- ID_test: `test_user_register`
- Input: `user` (fixture de usuario con posibilidad de registro)
- Resultado esperado: Se espera que los campos dentro de la clase de usuario obtenidos no sean `None`, es decir, que se haya podido registrar.
- Resultado obtenido: Los campos obtenidos son distintos de `None`.
- Fallo o éxito:
    - **Falla**: Alguno de los campos es `None`.
    - **Éxito**: Todos los camposo no son `None`.

#### PRUEBA DE INSTANCIA DE INICIO DE SESIÓN
- ID_test: `test_user_login`
- Input: `user` (fixture de usuario con posibilidad de iniciar sesión)
- Resultado esperado: Se espera que el usuario pueda iniciar sesión, es decir, que sea `True`.
- Resultado obtenido: El inicio de sesión es exitoso es decir, que sea `True`.
- Fallo o éxito:
    - **Falla**: Cuando el inicio de sesión es `False`.
    - **Éxito**: Cuando el inicio de sesión es `True`.

#### PRUEBA DE INSTANCIA DE INICIO DE SESIÓN CON CREDENCIALES INCORRECTAS
- ID_test: `test_user_incorrect_login`
- Input: `user` (fixture de usuario con posibilidad de iniciar sesión)
- Resultado esperado: Se espera que el usuario no pueda iniciar sesión, es decir, que sea `False`.
- Resultado obtenido: El inicio de sesión no es exitoso es decir, que sea `False`.
- Fallo o éxito:
    - **Falla**: Cuando el inicio de sesión es `True`.
    - **Éxito**: Cuando el inicio de sesión es `False`.

#### PRUEBA DE INSTANCIA DE LLAVERO DE UN USUARIO
- ID_test: `test_keychain_user`
- Input: `user` (fixture de usuario con sesión)
- Resultado esperado: Se espera que el usuario cuente con una `KeyChain`, por lo tanto debe ser distinto de `None`.
- Resultado obtenido: El usuario cuenta con una `KeyChain`.
- Fallo o éxito:
    - **Falla**: Cuando el usuario no tiene una `KeyChain` con sesión.
    - **Éxito**: Cuando el usuario tiene una `KeyChain` con sesión.

#### PRUEBA DE AÑADIR UNA CONTRASEÑA AL LLAVERO
- ID_test: `test_add_password`
- Input: `user` (fixture de usuario con sesión)
- Resultado esperado: Se espera que se pueda añadir una nueva contraseña y esta se guarde.
- Resultado obtenido: La contraseña se almacena correctamente.
- Fallo o éxito:
    - **Falla**: Cuando la contraseña no se almacena.
    - **Éxito**: Cuando la contraseña se queda guardada y persiste.

#### PRUEBA DE AÑADIR UNA CONTRASEÑA CON KEY DUPLICADA AL LLAVERO
- ID_test: `test_add_password_duplicate`
- Input: `user` (fixture de usuario con sesión)
- Resultado esperado: Se espera que no se pueda añadir otra contraseña con la misma `key`, por lo que el valor debe mantenerse con el primer insertado.
- Resultado obtenido: La contraseña no cambia al tratar de añadirla nuevamente con la `key`.
- Fallo o éxito:
    - **Falla**: Cuando la contraseña actual cambia por la duplicada.
    - **Éxito**: Cuando la contraseña actual se mantiene.

#### PRUEBA DE CAMBIAR UNA CONTRASEÑA EXISTENTE EN EL LLAVERO
- ID_test: `test_change_password`
- Input: `user` (fixture de usuario con sesión)
- Resultado esperado: Se espera que al cambiar la contraseña esta se actualice a la nueva.
- Resultado obtenido: La contraseña se cambia correctamente.
- Fallo o éxito:
    - **Falla**: Cuando la contraseña antigua se mantiene y no se actualiza.
    - **Éxito**: Cuando la contraseña se cambia por la nueva.

#### PRUEBA DE CAMBIAR UNA CONTRASEÑA QUE NO EXISTENTE EN EL LLAVERO
- ID_test: `test_change_password_not_exists`
- Input: `user` (fixture de usuario con sesión)
- Resultado esperado: Se espera que no se pueda cambiar la contraseña de una `Key` que no existe, es decir, obtener `None`.
- Resultado obtenido: La contraseña no se cambia y no da error porque no existe la `Key`.
- Fallo o éxito:
    - **Falla**: Cuando da un error por no manejar esa excepción.
    - **Éxito**: Cuando no se cambia ni da un error.

#### PRUEBA DE BORRAR UNA CONTRASEÑA DE UN LLAVERO
- ID_test: `test_delete_password`
- Input: `user` (fixture de usuario con sesión)
- Resultado esperado: Se espera que la contraseña asociada al `Key` que se quiere borrar, desaparezca del sistema.
- Resultado obtenido: La contraseña asociada al `Key` desaparece.
- Fallo o éxito:
    - **Falla**: Cuando la contraseña aún se mantiene en la base de datos.
    - **Éxito**: Cuando está se elimina por completo.

### - Pruebas de generador de contraseñas
#### CONTRASEÑA DE LARGO CORRECTO
- ID_test: test_length_password
- Input: 14
- Resultado esperado: Se espera que se cree la contraseña correctamente.
- Resultado obtenido: Se creó la password
- Fallo o éxito: 
  - Falla: cuando no se crea la contraseña
  - Éxito: cuando sí se crea la contraseña
- Comentario adicional: el input está entre los límites por ende es exitosa
  

#### CONTRASEÑA MAS LARGA QUE LO PERMITIDO
- ID_test: test_greater_max_length_password
- Input: 17
- Resultado esperado: Se espera que no se cree la contraseña
- Resultado obtenido: No se crea la contraseña
- Fallo o éxito: 
  - Falla: cuando no se crea la contraseña
  - Éxito: cuando sí se crea la contraseña
- Comentario adicional: se tiene un input mayor al largo máximo permitido


#### CONTRASEÑA MAS CORTA QUE LO PERMITIDO
- ID_test: test_lower_min_length_password
- Input: 5
- Resultado esperado: Se espera que no se cree la contraseña
- Resultado obtenido: no se crea la contraseña
- Fallo o éxito: 
  - Falla: cuando sí se crea la contraseña
  - Éxito: cuando no se crea la contraseña

#### CONTRASEÑA CON CARACTERES ASCII
- ID_test: test_chars_password
- Input: "abc"
- Resultado esperado: Se espera una contraseña con los caracteres "abc"
- Resultado obtenido: Contraseña correcta con caracteres "abc"
- Fallo o éxito: 
  - Falla: cuando se crea contraseña con otros caracteres
  - Éxito: cuando la contraseña contiene solamente esos caracteres

#### CONTRASEÑA CON CARACTER UNICODE
- ID_test: test_unicode_chars_password
- Input: "🐍"
- Resultado esperado: Se espera que no se genere la contraseña con solamente el input entregado
- Resultado obtenido: El generador da la excepción de que no es posible hacer una secuencia con el emoji del input
- Fallo o éxito: 
  - Falla: Se genera una contraseña con solo el caracter entregado
  - Éxito: Si es que no se crea la contraseña