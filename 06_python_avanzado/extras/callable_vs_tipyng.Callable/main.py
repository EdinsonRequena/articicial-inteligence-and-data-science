"""
En Python, typing.Callable y la función incorporada callable tienen propósitos diferentes, aunque sus nombres puedan parecer similares.

typing.Callable:
*) typing.Callable es parte del módulo typing, que se utiliza para la anotación de tipos.
*) Su propósito principal es proporcionar una manera de especificar el tipo de una función o un objeto invocable (que se comporta como una función) en las anotaciones de tipo.
*) Se usa principalmente para la verificación estática de tipos, ayudando a herramientas como IDEs y linters a comprender qué tipo de función o invocable se espera en un determinado contexto.
*) Ejemplo de uso: Si tienes una función que acepta otra función como argumento, puedes anotar este argumento usando typing.Callable para especificar los tipos de los argumentos de entrada y salida de esa función.

built in callable:
*) callable es una función incorporada en Python.
*) Se utiliza para comprobar si un objeto es invocable, es decir, si se puede llamar como una función.
*) Devuelve True si el objeto parece invocable (si tiene un método __call__), de lo contrario, devuelve False.
*) Es una herramienta en tiempo de ejecución y se utiliza para hacer comprobaciones dinámicas.
*) Ejemplo de uso: Si tienes un objeto y quieres comprobar si se puede llamar como una función, puedes usar callable para hacer la comprobación.

¿Cuál usar? Depende de lo que necesites hacer:

Si necesitas verificar si un objeto puede ser llamado como una función en tu código (en tiempo de ejecución), usa la función callable.
Si estás anotando tipos en tu código para claridad, seguridad de tipos o para trabajar con herramientas de análisis estático de código, utiliza typing.Callable.
Ambos son útiles en diferentes contextos y no son directamente intercambiables. Su elección depende de si estás haciendo una verificación de tipo en tiempo de ejecución o especificando tipos para análisis estático.

En los ejemplos de este modulo se muestran cómo typing.Callable se utiliza para anotaciones de tipo y ayudar con el análisis estático del código,
mientras que callable se utiliza para comprobaciones en tiempo de ejecución para ver si un objeto se comporta como una función.
"""
