meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "DELULU": " Viene del inglés delusional (delirante). Se usa para describir a alguien que vive en una fantasía o que tiene expectativas irreales sobre algo.",
            "RIZZ": "Viene de carisma en inglés. Define la habilidad natural que tiene una persona para coquetear, encantar o atraer a otros.",
            "SLAY":"Significa hacer algo de manera excelente, destacar o lucir increíblemente bien."
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    print (meme_dict[word])
else:
    print ("esa palabra no esta en nuestro diccionario")
