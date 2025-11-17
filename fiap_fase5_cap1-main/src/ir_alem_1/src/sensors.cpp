
#include "sensors.h"
#include <DHT.h>
DHT dht(DHTPIN, DHTTYPE);

void initSensors() {
    dht.begin();
}

float readTemperature() {
    return dht.readTemperature();
}

float readHumidity() {
    return dht.readHumidity();
}
