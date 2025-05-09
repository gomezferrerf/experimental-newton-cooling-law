#include <OneWire.h>
#include <DallasTemperature.h>

#define ONE_WIRE_BUS 4  // Pin digital donde están conectados los sensores

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

DeviceAddress sensor1, sensor2, sensor3, sensor4;

void setup() {
  Serial.begin(9600);
  sensors.begin();

  if (sensors.getDeviceCount() < 4) {
    Serial.println("¡Error! No se detectan 4 sensores. Conecta todos correctamente.");
    while (true); // Detener ejecución
  }

  // Asignar direcciones a cada sensor
  sensors.getAddress(sensor1, 0);
  sensors.getAddress(sensor2, 1);
  sensors.getAddress(sensor3, 2);
  sensors.getAddress(sensor4, 3);
}

void loop() {
  sensors.requestTemperatures();

  Serial.print("Sensor 1: ");
  Serial.print(sensors.getTempC(sensor1));
  Serial.println(" °C");

  Serial.print("Sensor 2: ");
  Serial.print(sensors.getTempC(sensor2));
  Serial.println(" °C");

  Serial.print("Sensor 3: ");
  Serial.print(sensors.getTempC(sensor3));
  Serial.println(" °C");

  Serial.print("Sensor 4 (ambiente): ");
  Serial.print(sensors.getTempC(sensor4));
  Serial.println(" °C");

  Serial.println("----------------------");
  delay(1000);
}
