#include <SPI.h>
#include <MFRC522.h>

#define SS_PIN 10
#define RST_PIN 9

//creating an instance 
MFRC522 mfrc522(SS_PIN, RST_PIN); 


void setup() {
  Serial.begin(9600);
  SPI.begin();      // Initiate  SPI bus
  Serial.println();
}

void loop() {
  String cardUID="";
  if(mfrc522.PICC_IsNewCardPresent()){
    if(mfrc522.PICC_ReadCardSerial()){
      
      // Serial.print("UID TAG: ");
      for(byte i=0; i<mfrc522.uid.size; i++){
        Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" :" ");    //checks if the current byte is less than 10, if so adds a 0 before so 0X or else
        Serial.print(mfrc522.uid.uidByte[i],HEX);                   //adds the current byte converted to HEXadecimal
        
        //saves the current uid to a buffer string
        cardUID.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ")); 
        cardUID.concat(String(mfrc522.uid.uidByte[i],HEX));
      }
      Serial.println();
      cardUID.toUpperCase();
      
      delay(2000);
    }
  }
}
