//
// Created by Lucas on 03/09/2025.
//

#ifndef API_H
#define API_H
#include <Wire.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

#include <utility>
#include "../conexao_wifi/conexao_wifi.h"

struct Response
{
    const int status_code;
    const String body;

    JsonDocument toJson() const
    {
        JsonDocument doc;
        const DeserializationError error = deserializeJson(doc, body);
        if (error) {
            // Retorna um documento JSON vazio em caso de erro
            return JsonDocument(nullptr);
        }
        return doc;
    }

};

class Api
{
    const String baseUrl; // Exemplo: "http://api.example.com" sem barra no final
    const String initUrl; // Exemplo: "/init"
    const String leituraUrl; // Exemplo: "/leitura"
    const String saudeUrl; // Exemplo: "/saude"
    String chipIdStr;
    ConexaoWifi conexao;
    PainelLCD* lcd;

public:
    Api(String  baseUrl, String  initUrl, String leituraUrl, String saudeUrl, const ConexaoWifi& conexao, PainelLCD* lcd = nullptr, const String& chipIdStr = "")
    : baseUrl(std::move(baseUrl)), initUrl(std::move(initUrl)), leituraUrl(std::move(leituraUrl)), saudeUrl(std::move(saudeUrl)), chipIdStr(chipIdStr), conexao(conexao), lcd(lcd) {

        if (chipIdStr.isEmpty()) {
            uint64_t chipid = ESP.getEfuseMac();
            char buffer[17]; // 16 caracteres + null terminator
            sprintf(buffer, "%016llX", chipid);
            this->chipIdStr = String(buffer);
        }

    }

    Response get(const String &path) {
        if (!conexao.estaConectado()) {
            return {-1, "Not connected to WiFi"};
        }

        String url = baseUrl;
        if (!path.startsWith("/")) {
            url += "/";
        }
        url += path;

        HTTPClient http;
        http.begin(url);

        const int httpCode = http.GET();

        if (httpCode > 0) {
            const String payload = http.getString();
            http.end();
            return {httpCode, payload};
        } else {
            http.end();
            return {httpCode, "Request failed"};
        }
    }

    Response post(const String &path, const String &body, const String &contentType) {
        if (!conexao.estaConectado()) {
            return {-1, "Not connected to WiFi"};
        }

        String url = baseUrl;
        if (!path.startsWith("/")) {
            url += "/";
        }
        url += path;

        HTTPClient http;
        http.begin(url);
        http.addHeader("Content-Type", contentType);

        const int httpCode = http.POST(body);

        if (httpCode > 0) {
            const String payload = http.getString();
            http.end();
            return {httpCode, payload};
        } else {
            http.end();
            return {httpCode, "Request failed"};
        }
    }

    Response post_json(const String &path, const JsonDocument& json)
    {
        String jsonStr;
        serializeJson(json, jsonStr);

        return post(path, jsonStr, "application/json");
    }

    Response post_init()
    {
        JsonDocument doc;
        doc["serial"] = chipIdStr; // Adiciona o Chip ID ao JSON
        return post_json(initUrl, doc);
    }

    Response post_leitura(JsonDocument& json)
    {
        json["serial"] = chipIdStr; // Adiciona o Chip ID ao JSON
        return post_json(leituraUrl, json);
    }

    Response post_saude(JsonDocument& json)
    {
        json["serial"] = chipIdStr; // Adiciona o Chip ID ao JSON
        return post_json(saudeUrl, json);
    }


};

#endif //API_H
