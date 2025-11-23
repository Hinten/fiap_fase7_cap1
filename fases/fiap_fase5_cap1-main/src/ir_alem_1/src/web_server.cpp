
#include "web_server.h"
#include <WebServer.h>
#include <ArduinoJson.h>
#include <FS.h>
#include <SPIFFS.h>
#include "sensors.h"

extern WebServer server;

void handleRoot() {
    server.sendHeader("Location", "/dashboard.html", true);
    server.send(302, "text/plain", "");
}

void handleData() {
    float temperature = readTemperature();
    float humidity = readHumidity();
    JsonDocument doc;
    doc["temperature"] = temperature;
    doc["humidity"] = humidity;
    String output;
    serializeJson(doc, output);
    server.send(200, "application/json", output);
}

void handleHealth() {
    server.send(200, "text/plain", "OK");
}

void setupWebServer() {
    if (!SPIFFS.begin(true)) {
        Serial.println("An Error has occurred while mounting SPIFFS");
        return;
    }
    server.on("/", handleRoot);
    server.on("/dashboard.html", HTTP_GET, []() {
        File file = SPIFFS.open("/dashboard.html", "r");
        if (!file) {
            server.send(404, "text/plain", "File not found");
            return;
        }
        server.streamFile(file, "text/html");
        file.close();
    });
    server.on("/data", HTTP_GET, handleData);
    server.on("/health", HTTP_GET, handleHealth);
}
