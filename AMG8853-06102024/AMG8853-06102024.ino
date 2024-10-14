#include <SparkFun_GridEYE_Arduino_Library.h>

#include <Wire.h>


GridEYE grideye;

const int dirPin1= 33;
const int stepPin1=32;

const int dirPin2= 17;
const int stepPin2=16;

const int STEPS_PER_REV=10;

void setup() {

  // Start your preferred I2C object 
  Wire.begin();
  // Library assumes "Wire" for I2C but you can pass something else with begin() if you like
  grideye.begin(0x68,Wire);
  // Pour a bowl of serial 
  Serial.begin(9600);
  pinMode(dirPin1, OUTPUT);
  pinMode(dirPin2, OUTPUT);
  pinMode(stepPin1, OUTPUT);
  pinMode(stepPin2, OUTPUT);
}

void loop() {
 /* 
 digitalWrite(dirPin1,HIGH);
  for(int x = 0; x < STEPS_PER_REV; x++) {
    digitalWrite(stepPin1,HIGH); 
    delayMicroseconds(2000); 
    digitalWrite(stepPin1,LOW); 
    delayMicroseconds(2000); 
  }*/



    digitalWrite(dirPin2,HIGH);
  for(int x = 0; x < STEPS_PER_REV; x++) {
    digitalWrite(stepPin2,HIGH); 
    delayMicroseconds(2000); 
    digitalWrite(stepPin2,LOW); 
    delayMicroseconds(2000); 
  }


for(unsigned char i = 0; i < 63; i++){
Serial.print(grideye.getPixelTemperature(i));
Serial.print(",");
}
Serial.print(grideye.getPixelTemperature(63));
Serial.println();
delay(1000);

  
}