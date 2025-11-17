//
// Created by Lucas on 26/08/2025.
//

#ifndef SENSOR_UMIDADE_SOLO_H
#define SENSOR_UMIDADE_SOLO_H
#include <Arduino.h>


class SensorUmidadeSolo
{
    const uint8_t SENSOR_PIN;
    const uint16_t dry_value; // valor do sensor quando o solo está seco
    const uint16_t wet_value; // valor do sensor quando o solo está úmido

public:

    SensorUmidadeSolo(const uint8_t SENSOR_PIN, const uint16_t dry_value, const uint16_t wet_value)
        : SENSOR_PIN(SENSOR_PIN), dry_value(dry_value), wet_value(wet_value) {}

    void setup() const
    {
        pinMode(SENSOR_PIN, INPUT);
    }

    float read() const
    {
        return analogRead(SENSOR_PIN);
    }

    float read_humidity() const {

        const int sensor_value = analogRead(SENSOR_PIN);

        if (isnan(sensor_value))
        {
            return NAN;
        }

        // Mapeia o valor do sensor para uma porcentagem de umidade
        float humidity = 100.0f * static_cast<float>(sensor_value - static_cast<int>(dry_value)) / static_cast<float>(static_cast<int>(wet_value) - static_cast<int>(dry_value));

        // Limita o valor entre 0 e 100
        humidity = constrain(humidity, 0, 100);

        return humidity;

    }

};

#endif //SENSOR_UMIDADE_SOLO_H
