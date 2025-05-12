const int IR_LEFT = A0;
const int IR_CENTER = A2;
const int IR_RIGHT = A1;

int lastLeft = -1;
int lastCenter = -1;
int lastRight = -1;

void setup() {
  Serial.begin(9600);

  pinMode(IR_LEFT, INPUT);
  pinMode(IR_CENTER, INPUT);
  pinMode(IR_RIGHT, INPUT);
}

void loop() {
  int left = digitalRead(IR_LEFT);
  int center = digitalRead(IR_CENTER);
  int right = digitalRead(IR_RIGHT);

  // Only print when there's a change
  if (left != lastLeft || center != lastCenter || right != lastRight) {
    Serial.print("Left: ");
    Serial.print(left);
    Serial.print(" | Center: ");
    Serial.print(center);
    Serial.print(" | Right: ");
    Serial.println(right);

    lastLeft = left;
    lastCenter = center;
    lastRight = right;
  }

  delay(100); // Reduce flickering in serial output
}
