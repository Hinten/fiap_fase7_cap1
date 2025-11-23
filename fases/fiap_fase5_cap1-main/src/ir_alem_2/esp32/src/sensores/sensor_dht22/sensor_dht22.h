//
// Created by Lucas on 25/08/2025.
//

#ifndef SENSOR_DHT22_H
#define SENSOR_DHT22_H
#include <Arduino.h>
#include <DHT_U.h>

class SensorDHT22 {
    const uint8_t pin;
    const uint8_t type;
    DHT_Unified dht;

public:
    SensorDHT22(const uint8_t pin, const uint8_t type)
        : pin(pin), type(type), dht(pin, type) {}

    uint8_t getPin() const { return pin; }
    uint8_t getType() const { return type; }
    DHT_Unified& getDHT() { return dht; }

    void setup() {
        dht.begin();
        sensor_t sensor;

        dht.temperature().getSensor(&sensor);
        Serial.println(F("------------------------------------"));
        Serial.println(F("Temperature Sensor"));
        Serial.print  (F("Sensor Type: ")); Serial.println(sensor.name);
        Serial.print  (F("Driver Ver:  ")); Serial.println(sensor.version);
        Serial.print  (F("Unique ID:   ")); Serial.println(sensor.sensor_id);
        Serial.print  (F("Max Value:   ")); Serial.print(sensor.max_value); Serial.println(F("°C"));
        Serial.print  (F("Min Value:   ")); Serial.print(sensor.min_value); Serial.println(F("°C"));
        Serial.print  (F("Resolution:  ")); Serial.print(sensor.resolution); Serial.println(F("°C"));
        Serial.println(F("------------------------------------"));

        dht.humidity().getSensor(&sensor);
        Serial.println(F("Humidity Sensor"));
        Serial.print  (F("Sensor Type: ")); Serial.println(sensor.name);
        Serial.print  (F("Driver Ver:  ")); Serial.println(sensor.version);
        Serial.print  (F("Unique ID:   ")); Serial.println(sensor.sensor_id);
        Serial.print  (F("Max Value:   ")); Serial.print(sensor.max_value); Serial.println(F("%"));
        Serial.print  (F("Min Value:   ")); Serial.print(sensor.min_value); Serial.println(F("%"));
        Serial.print  (F("Resolution:  ")); Serial.print(sensor.resolution); Serial.println(F("%"));
        Serial.println(F("------------------------------------"));
    }

    float getTemperature() {
        sensors_event_t event;
        dht.temperature().getEvent(&event);
        return isnan(event.temperature) ? NAN : event.temperature;
    }

    float getHumidity() {
        sensors_event_t event;
        dht.humidity().getEvent(&event);
        return isnan(event.relative_humidity) ? NAN : event.relative_humidity;
    }
};

#endif //SENSOR_DHT22_H
