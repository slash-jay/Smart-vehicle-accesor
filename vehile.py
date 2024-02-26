#include <LiquidCrystal.h> //Load Liquid Crystal Library
LiquidCrystal lcd(12,11,5,4,3,2);  //Create Liquid Crystal Object called LCD

#define trigPin 8 //Sensor Echo pin connected to Arduino pin 13
#define echoPin 7 //Sensor Trip pin connected to Arduino pin 12


void setup() 
{  
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(13, OUTPUT);
  pinMode(11, OUTPUT);
 
  
  lcd.begin(16,2); //Tell Arduino to start your 16 column 2 row LCD
  lcd.setCursor(0,0);  //Set LCD cursor to upper left corner, column 0, row 0
  lcd.print("Height:");  //Print Message on First Row
}
void loop() {
  long duration, distance;
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance = (duration/2) / 29.1;

  lcd.setCursor(0,1);  //Set cursor to first column of second row
  lcd.print("                "); //Print blanks to clear the row
  lcd.setCursor(0,1); 
  distance=30-distance;
  if(distance>0){//Set Cursor again to first column of second row
  lcd.print(distance);
  }
  else{
    lcd.print("0");
} //Print measured distance
  lcd.print(" cm");
  if(distance>30||distance<0){
  lcd.print("       NO");
  //Serial.print("     NO");
  digitalWrite(10,LOW);
  digitalWrite(9, HIGH);
  delay(1000);
  }
  else{
  lcd.print("       YES");
  //Serial.print("     YES");
  digitalWrite(10,HIGH);
  digitalWrite(9, LOW);
  delay(1000);
  }
  delay(250); /
}