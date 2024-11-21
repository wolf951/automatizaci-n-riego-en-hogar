#include <Arduino.h>
#include <WiFi.h>
#include <HTTPClient.h>

// Configuraciones de WiFi y ThingSpeak
const char* ssid = " ";
const char* password = " ";
const char* apiKey = "GHH9KNNIQSAKNQ52";
const char* server = "https://api.thingspeak.com/update?api_key=0XRC7WK1JGHVU5RE&field1=0";

// Pines de los sensores
const int sensorHumedadPin = 34;
const int sensorUVPin = 36;

// Función para enviar datos a ThingSpeak
void enviarDatos(float humedad, int valorUV) {
  String url = String(server) + "?api_key=" + apiKey + "&field1=" + String(humedad) + "&field2=" + String(valorUV);
  HTTPClient http;
  
  http.begin(url);
  int httpCode = http.GET();
  
  if (httpCode > 0) {
    Serial.println("Datos enviados a ThingSpeak exitosamente!");
  } else {
    Serial.println("Error al enviar datos a ThingSpeak");
  }
  
  http.end();
}

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("Conectado a WiFi");
}

void loop() {
  // Leer valores de los sensores
  int valorHumedad = analogRead(sensorHumedadPin);
  float humedad = map(valorHumedad, 0, 4090, 0, 100);

  int valorUV = analogRead(sensorUVPin);

  // Enviar datos a ThingSpeak
  enviarDatos(humedad, valorUV);

  Serial.print("Humedad: ");
  Serial.print(humedad);
  Serial.print("%  UV: ");
  Serial.println(valorUV);

  delay(30000); // Enviar datos cada 30 segundos