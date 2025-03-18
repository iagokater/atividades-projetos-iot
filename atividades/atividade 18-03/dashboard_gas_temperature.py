import serial
import csv
import time

# Configuração da porta serial (ajuste o baudrate se necessário)
PORTA_SERIAL = "COM13"
BAUDRATE = 9600

# Nome do arquivo CSV
CSV_FILE = "dados_sensores.csv"

# Inicia a comunicação serial
ser = serial.Serial(PORTA_SERIAL, BAUDRATE, timeout=2)

# Cria o arquivo CSV e escreve o cabeçalho se não existir
with open(CSV_FILE, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Temperatura (°C)", "Umidade (%)", "Gás"])

print("Coletando dados dos sensores... (Pressione Ctrl+C para parar)")

try:
    while True:
        linha = ser.readline().decode("utf-8").strip()
        if linha:
            print(linha)  # Exibe os dados recebidos
            
            if "Erro ao ler do sensor DHT" in linha:
                continue  # Ignora leituras inválidas
            
            partes = linha.split(" / ")
            if len(partes) == 3:
                umidade = partes[0].split(": ")[1].replace(" %", "")
                temperatura = partes[1].split(": ")[1].replace(" °C", "")
                gas = partes[2].split(": ")[1]
                
                # Salva no CSV
                with open(CSV_FILE, mode="a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), temperatura, umidade, gas])

        time.sleep(2)  # Intervalo de 2 segundos entre leituras

except KeyboardInterrupt:
    print("\nColeta de dados encerrada.")
    ser.close()
