#include <DHT.h> // Biblioteca correta

#define DHTTYPE DHT11
#define DHTPIN 7

const int ledGreen = 4; // LED verde (seguro)
const int ledYellow = 3; // LED amarelo (atenção)
const int ledRed = 2; // LED vermelho (perigo)
const int ledBlue = 8; // LED azul (alerta crítico)
const int pinGas = A0; // Sensor MQ2

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  pinMode(pinGas, INPUT);
  pinMode(ledGreen, OUTPUT);
  pinMode(ledYellow, OUTPUT);
  pinMode(ledRed, OUTPUT);
  pinMode(ledBlue, OUTPUT);

  Serial.begin(9600);
  dht.begin();
  delay(2000); // Tempo de estabilização do sensor
}

void loop() {
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  int gasLevel = analogRead(pinGas); // Leitura do sensor de gás

  // Verifica se a leitura é válida
  if (isnan(h) || isnan(t)) {
    Serial.println("Erro ao ler do sensor DHT!");
    return;
  }

  Serial.print("Umidade: ");
  Serial.print(h);
  Serial.print(" % / Temperatura: ");
  Serial.print(t);
  Serial.print(" °C / Gás: ");
  Serial.println(gasLevel);

  if (t > 29 || gasLevel > 790) { 
      digitalWrite(ledGreen, LOW);
      digitalWrite(ledYellow, LOW);
      digitalWrite(ledRed, LOW);
      Serial.println("ALERTA CRÍTICO: EVACUAR ÁREA!");
      piscarLed(ledBlue); // Pisca o LED vermelho para alertar perigo crítico
  } else if (t > 28 || gasLevel > 750) {
      digitalWrite(ledGreen, LOW);
      digitalWrite(ledYellow, LOW);
      digitalWrite(ledRed, HIGH);
      digitalWrite(ledBlue, LOW);
      Serial.println("ALERTA: RISCO ALTO!");
  } else if (t > 26 || gasLevel > 740) { //Led AMARELO
      digitalWrite(ledGreen, LOW);
      digitalWrite(ledYellow, HIGH);
      digitalWrite(ledRed, LOW);
      digitalWrite(ledBlue, LOW);
      Serial.println("ATENÇÃO: RISCO MODERADO!");
  } else { //LED VERDE
      digitalWrite(ledGreen, HIGH);
      digitalWrite(ledYellow, LOW);
      digitalWrite(ledRed, LOW);
      digitalWrite(ledBlue, LOW);
      Serial.println("Nível seguro.");
  }


  delay(2000);
}

void piscarLed(int pino) {
  for (int i = 0; i < 5; i++) { 
    digitalWrite(pino, HIGH); // Liga o LED
    delay(500); // Aguarda 500ms
    digitalWrite(pino, LOW); // Desliga o LED
    delay(500); // Aguarda 500ms
  }
}
