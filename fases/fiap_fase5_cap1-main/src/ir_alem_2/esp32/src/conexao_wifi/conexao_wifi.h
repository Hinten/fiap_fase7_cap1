//
// Created by Lucas on 03/09/2025.
//

#ifndef CONEXAO_WIFI_H
#define CONEXAO_WIFI_H
#include <WiFi.h>
#include "../painel_lcd/painel.h"

class ConexaoWifi
{
    const char* ssid;
    const char* password;
    PainelLCD* lcd;
    unsigned long tempoMaximoConexao;
    bool conectado;

    void print_serial_or_lcd(const String& msg) const {
        if (lcd != nullptr) {
            lcd->printLCDSerial(0, 0, msg);
        } else {
            Serial.println(msg);
        }
    }

public:
    ConexaoWifi(const char* ssid, const char* password, PainelLCD* lcd = nullptr, unsigned long tempoMaximoConexao = 10000)
        : ssid(ssid), password(password), lcd(lcd), tempoMaximoConexao(tempoMaximoConexao), conectado(false) {}

    void connect() {
        WiFi.begin(ssid, password);
        print_serial_or_lcd("Conectando ao WiFi");
        const unsigned long inicio = millis();
        conectado = false;
        while (WiFi.status() != WL_CONNECTED && (millis() - inicio) < tempoMaximoConexao) {
            delay(500);
            print_serial_or_lcd("Conectando ao WiFi...");
        }
        if (WiFi.status() == WL_CONNECTED) {
            print_serial_or_lcd("\nWiFi conectado!");
            conectado = true;
        } else {
            print_serial_or_lcd("\nFalha ao conectar ao WiFi!");
            conectado = false;
        }
    }

    void setup() {
        connect();
    }

    bool estaConectado() {
        conectado = WiFiClass::status();
        return conectado;
    }
};

#endif //CONEXAO_WIFI_H
