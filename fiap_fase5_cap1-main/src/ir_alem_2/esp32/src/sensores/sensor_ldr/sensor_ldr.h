//
// Created by Lucas on 26/08/2025.
//

#ifndef SENSOR_LDR_H
#define SENSOR_LDR_H
#include <Arduino.h>


class SensorLDR
{
    const uint8_t LDR_PIN;
    const float VCC; // tensão de alimentação do divisor de tensão (3.3V ou 5V)
    const float LDR_RESISTOR; // resistor fixo (10k, por ex.)

    const float LUX_COEFFICIENT; // coeficiente para conversão em lux
    const float GAMMA_COEFFICIENT; // expoente para a fórmula de conversão

public:
    SensorLDR(const uint8_t LDR_PIN, const float VCC, const float LDR_RESISTOR, const float LUX_COEFFICIENT=500000.0, const float GAMMA_COEFFICIENT=0.7)
        : LDR_PIN(LDR_PIN), VCC(VCC), LDR_RESISTOR(LDR_RESISTOR), LUX_COEFFICIENT(LUX_COEFFICIENT), GAMMA_COEFFICIENT(GAMMA_COEFFICIENT) {}

    void setup() const
    {
        pinMode(LDR_PIN, INPUT);
    }

    float read_lux() const
    {
        const int adc = analogRead(LDR_PIN);

        
        if (isnan(adc))
        {
            return NAN;
        }

        const float vout = adc / 4095.0 * VCC;

        // Resistência do LDR
        const float Rldr = LDR_RESISTOR * (VCC / vout - 1);

        // Estimativa de Lux (aproximado)
        const float lux = pow((LUX_COEFFICIENT / Rldr), (1.0 / GAMMA_COEFFICIENT));

        return lux;
    }

};

#endif //SENSOR_LDR_H
