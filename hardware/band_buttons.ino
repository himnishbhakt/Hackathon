// Button pins
const int button1 = 2; // Green
const int button2 = 3; // Yellow

// LED pins
const int greenLED = 5;
const int blueLED = 6;
const int redLED = 7;

void setup() {
  pinMode(button1, INPUT_PULLUP);
  pinMode(button2, INPUT_PULLUP);

  pinMode(greenLED, OUTPUT);
  pinMode(blueLED, OUTPUT);
  pinMode(redLED, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // Read buttons (LOW = pressed because of INPUT_PULLUP)
  bool b1 = digitalRead(button1) == LOW;
  bool b2 = digitalRead(button2) == LOW;

  // Turn all LEDs off first
  digitalWrite(greenLED, LOW);
  digitalWrite(blueLED, LOW);
  digitalWrite(redLED, LOW);

  


  // Logic: check both first
  if (b1 && b2) {
    digitalWrite(redLED, HIGH);  // Both pressed → red
    Serial.println(3);           // Send 3
    delay(150);                  // Debounce + avoid spamming
  }
  else if (b2) {                 // Button 2 only → blue
    digitalWrite(blueLED, HIGH);
    Serial.println(1);           // Send 1
    delay(150);
  }
  else if (b1) {                 // Button 1 only → green
    digitalWrite(greenLED, HIGH);
    Serial.println(2);           // Send 2
    delay(150);
  }
}
