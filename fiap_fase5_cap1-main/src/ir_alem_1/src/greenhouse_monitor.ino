
#include <WiFi.h>
#include <WebServer.h>
#include <FS.h>
#include <SPIFFS.h>
#include "sensors.h"
#include "web_server.h"
#include "config/wifi_credentials.h"

WebServer server(80);

void setup() {
    Serial.begin(115200);
    delay(1000);
    
    // Inicializa sensores
    initSensors();

    // Inicializa SPIFFS para servir arquivos HTML
    if (!SPIFFS.begin(true)) {
        Serial.println("Erro ao montar SPIFFS");
        return;
    }

    // Conecta ao Wi-Fi
    WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
    Serial.print("Connecting to WiFi");
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    Serial.println(" Connected!");
    Serial.print("IP: ");
    Serial.println(WiFi.localIP());

    // Inicializa web server
    setupWebServer();
    server.begin();
}

void loop() {
    server.handleClient();
    // Log apenas DHT11
    float temperature = readTemperature();
    float humidity = readHumidity();
    Serial.printf("Temperature: %.2f °C, Humidity: %.2f %%\n", temperature, humidity);
    delay(2000);
}