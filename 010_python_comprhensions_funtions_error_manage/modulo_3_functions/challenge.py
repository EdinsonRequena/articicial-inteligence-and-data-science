def message_creator(text: str) -> str:

    options = {
        'computadora': "Con mi computadora puedo programar usando Python",
        'celular': 'En mi celular puedo aprender usando la app de Platzi',
        'cable': '¡Hay un cable en mi bota!'
    }

    return options[text] if text in options.keys() else 'Artículo no encontrado'


text = 'computadora'
response = message_creator(text)
print(response)
