#include <Arduino.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include "painel_lcd/painel.h"
#include "sensores/sensor_dht22/sensor_dht22.h"
#include <DHT.h>

#include "api/api.h"
#include "conexao_wifi/conexao_wifi.h"
#include "sensores/sensor_ldr/sensor_ldr.h"
#include "sensores/sensor_umidade_solo/sensor_umidade_solo.h"

SensorDHT22 sensor_dht22 = {5, DHT22}; // Pino 5, Tipo DHT22

PainelLCD painel_lcd = {0x27, 16, 2, 21, 22}; // Endereço I2C 0x27, 16 colunas, 2 linhas, pinos SDA 21, SCL 22

SensorLDR sensor_ldr = {32, 3.3, 10000}; // Pino 4, VCC 3.3V, Resistor 10k ohms

SensorUmidadeSolo sensor_umidade_solo = {33, 4095, 0}; // Pino 2, valor seco 4095, valor úmido 0

ConexaoWifi conexao_wifi = {NETWORK_SSID, NETWORK_PASSWORD, &painel_lcd, 10000}; // Substitua por seu SSID e senha

Api api = {API_BASE_URL, API_INIT_URL, API_LEITURA_URL, API_SAUDE_URL, conexao_wifi, &painel_lcd}; // Substitua pela URL base da sua API

String convertFloatToString(const float& value, const uint8_t decimalPlaces = 2)
{
    if (isnan(value))
    {
        return "Erro";
    } else
    {
        return String(value, static_cast<unsigned int>(decimalPlaces));
    }
}

struct SensorData
{
    float temperature;
    float humidity;
    float lux;
    float soil_humidity;
} sensor_data = {NAN, NAN, NAN, NAN};

bool enviar_init = true;
bool enviar_dados = false;
bool verificar_saude = false;

void primaryTask()
{
    const auto temperature = sensor_dht22.getTemperature();
    const auto humidity = sensor_dht22.getHumidity();
    const auto lux = sensor_ldr.read_lux();
    
    const auto solo_humidity = sensor_umidade_solo.read_humidity();

    sensor_data = {temperature, humidity, lux, solo_humidity};

    String msg_row_0 = "T:" + convertFloatToString(temperature);
    msg_row_0 += " L:" + convertFloatToString(lux, 0);

    String msg_row_1 = "U:" + convertFloatToString(humidity);
    msg_row_1 += " S:" + convertFloatToString(solo_humidity);

    painel_lcd.printLCDSerial(0, 0, msg_row_0);
    painel_lcd.printLCDSerial(0, 1, msg_row_1);
    enviar_dados = true;
    verificar_saude = true;
}

void _enviar_init()
{
    if (!conexao_wifi.estaConectado())
    {
        conexao_wifi.connect();
    } else
    {
        auto response = api.post_init();
        if (response.status_code == 200 || response.status_code == 201)
        {
            painel_lcd.printLCDSerial(0, 0, "Sensor iniciado");
            enviar_init = false;
        } else
        {
            painel_lcd.printLCDSerial(0, 0, "Erro ao iniciar");
            painel_lcd.printLCDSerial(0, 1, "sensor na API");
        }
    }
}

void _enviar_dados()
{
    painel_lcd.printLCDSerial(0, 0, "Enviando dados para api");

    JsonDocument doc;
    doc["temperature"] = sensor_data.temperature;
    doc["humidity"] = sensor_data.humidity;
    doc["lux"] = sensor_data.lux;
    doc["soil_humidity"] = sensor_data.soil_humidity;

    auto response = api.post_leitura(doc);
    if (response.status_code == 200 || response.status_code == 201)
    {
        painel_lcd.printLCDSerial(0, 0, "Dados enviados com sucesso");
        enviar_dados = false;
    } else
    {
        painel_lcd.printLCDSerial(0, 0, "Erro ao enviar dados");
        enviar_init = true; // Tenta reiniciar o sensor na próxima vez
    }
}

void _verificar_saude()
{
    
    painel_lcd.printLCDSerial(0, 0, "Verificando saude");
    painel_lcd.printLCDSerial(0, 1, "da planta");

    JsonDocument doc;
    doc["temperature"] = sensor_data.temperature;
    doc["humidity"] = sensor_data.humidity;
    doc["lux"] = sensor_data.lux;
    doc["soil_humidity"] = sensor_data.soil_humidity;

    auto response = api.post_saude(doc);
    if (response.status_code == 200 || response.status_code == 201)
    {
        auto doc = response.toJson();

        if (doc["saude"] == true){
            painel_lcd.printLCDSerial(0, 0, "Planta");
            painel_lcd.printLCDSerial(0, 1, "saudavel");
        } else
        {
            painel_lcd.printLCDSerial(0, 0, "Planta");
            painel_lcd.printLCDSerial(0, 1, "doente");
        }
        verificar_saude = false;

    } else
    {
        painel_lcd.printLCDSerial(0, 0, "Erro ao verificar saude");
        verificar_saude = true;
    }
}

void secondaryTask()
{
    if (!conexao_wifi.estaConectado())
    {
        conexao_wifi.connect();
    } else
    {

        if (enviar_init)
        {
            _enviar_init();
        }

        if (enviar_init)
        {
            return; // Não tenta enviar dados se o init falhou
        }

        if (enviar_dados)
        {
            _enviar_dados();
        }

        if (verificar_saude){
            _verificar_saude();
        }

        
    }
}

void setup() {
    Serial.begin(115200);
    painel_lcd.setup();
    sensor_dht22.setup();
    sensor_ldr.setup();
    sensor_umidade_solo.setup();
    conexao_wifi.setup();
}

unsigned long ultimoMillis = 0;
const unsigned long intervalo = 5000; // 5 segundos

void loop() {
    unsigned long agora = millis();
    if (agora - ultimoMillis >= intervalo) {
        ultimoMillis = agora;
        primaryTask();
    } else
    {
        secondaryTask();
    }
}



