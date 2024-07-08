def string_operaciones(text):


  resultado = []

  
  resultado.append(text.lower())
  
  return resultado


texto = "Lewis Hamilton gana el Gran Premio de Gran Bretaña"
resultados = string_operaciones(texto)
print(f"Resultados para '{texto}':")
for resultado in resultados:
  print(resultado)