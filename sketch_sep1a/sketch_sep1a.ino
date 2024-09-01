#include <SparkFun_GridEYE_Arduino_Library.h>
#include <Wire.h>

GridEYE grideye;

void setup() {
  // put your setup code here, to run once:
Wire.begin();
grideye.begin(0x68,Wire);
Serial.begin(9600);
delay(15000);

}

void loop() {
  // put your main code here, to run repeatedly:
  for(unsigned char i = 0; i < 63; i++){
Serial.print(grideye.getPixelTemperature(i));
Serial.print(",");
}
Serial.print(grideye.getPixelTemperature(63));
Serial.println();
delay(1000);

}                                                                                  
