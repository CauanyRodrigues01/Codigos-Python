while True:
  try:
    while True:
      TempoAteTerminal = 60
      #hora_que_devia_chegar == 8h == 480min
      horarioMarcado = 480
      
      acordou = input()
      
      #transformar em minutos:
      acordou_minutos = int(acordou[0])*60 + int(acordou[2:4])

      hora_que_chega = acordou_minutos + TempoAteTerminal

      tempoDeAtrazo = hora_que_chega - horarioMarcado

      if tempoDeAtrazo <= 0:
        print("Atraso maximo: 0")
      if tempoDeAtrazo > 0:
        print("Atraso maximo:", tempoDeAtrazo)
  except EOFError:
    break
