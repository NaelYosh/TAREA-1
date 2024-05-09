meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "Una respuesta a una broma",
            "SHEESH" : "ligera desaprobación",
            "CREEPY" : "aterrador",
            "AGGRO"  : "Ponerse agresivo",
            "TROLL" : "Persona que engaña a las personas",
            "BRO" : "Manera de decirle a un amigo",
            "BUG" : "Error de programación" ,
            "CRACK" : "Persona que destaca extraordinariamente en algo",
            }
            
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    print (meme_dict[word])
else:
    print ("Esta palabra no está en el diccionario")
