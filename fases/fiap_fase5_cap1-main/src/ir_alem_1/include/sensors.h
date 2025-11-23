
#ifndef SENSORS_H
#define SENSORS_H

#include <DHT.h>

// DHT11 Sensor Configuration
#define DHTPIN 15
#define DHTTYPE DHT11

// Function Declarations
void initSensors();
float readTemperature();
float readHumidity();

#endif // SENSORS_H