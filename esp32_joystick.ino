#define VRX 34
#define VRY 35
#define SW  32

void setup() {
  Serial.begin(115200);
  pinMode(SW, INPUT_PULLUP);
}

void loop() {
  Serial.print(analogRead(VRX));
  Serial.print(",");
  Serial.print(analogRead(VRY));
  Serial.print(",");
  Serial.println(digitalRead(SW));

  delay(10);
}
