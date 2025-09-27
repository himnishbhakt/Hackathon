const int greenPin = 2;
const int yellowPin = 3;
const int redPin = 4;

void setup() {
  pinMode(greenPin, INPUT_PULLUP);
  pinMode(yellowPin, INPUT_PULLUP);
  pinMode(redPin, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  if(digitalRead(greenPin) == LOW){
    Serial.println("green");
    delay(500);
  }
  if(digitalRead(yellowPin) == LOW){
    Serial.println("yellow");
    delay(500);
  }
  if(digitalRead(redPin) == LOW){
    Serial.println("red");
    delay(500);
  }
}
