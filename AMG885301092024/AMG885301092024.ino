#include <SparkFun_GridEYE_Arduino_Library.h>
#include <Wire.h>

GridEYE grideye;

void setup() {

  // Start your preferred I2C object 
  Wire.begin();
  // Library assumes "Wire" for I2C but you can pass something else with begin() if you like
  grideye.begin(0x68,Wire);
  // Pour a bowl of serial 
  Serial.begin(9600);

}

void loop() {

for(unsigned char i = 0; i < 63; i++){
Serial.print(grideye.getPixelTemperature(i));
Serial.print(",");
}
Serial.print(grideye.getPixelTemperature(63));
Serial.println();
delay(1000);

  
}