#include <PulseSensorPlayground.h>  // Includes the PulseSensorPlayground Library.  

// Variables
const int PulseWire = 0;          // PulseSensor PURPLE WIRE connected to ANALOG PIN 0
const int LED = LED_BUILTIN;      // The on-board Arduino LED, close to PIN 13.
int Threshold = 550;              // Determine which Signal to "count as a beat" and which to ignore.
int lastBPM = -1;                 // Variable to store last valid BPM reading, initialized to -1 to handle initial case

PulseSensorPlayground pulseSensor;  // Creates an instance of the PulseSensorPlayground object called "pulseSensor"

void setup() {
  Serial.begin(115200);          // For Serial Monitor

  // Configure the PulseSensor object, by assigning our variables to it.
  pulseSensor.analogInput(PulseWire);  
  pulseSensor.blinkOnPulse(LED);       // Auto-magically blink Arduino's LED with heartbeat.
  pulseSensor.setThreshold(Threshold);  

  if (pulseSensor.begin()) {
    Serial.println("We created a pulseSensor Object !");  // This prints one time at Arduino power-up, or on Arduino reset.
  }
}

void loop() {
  if (pulseSensor.sawStartOfBeat()) {  // Constantly test to see if "a beat happened".
    int myBPM = pulseSensor.getBeatsPerMinute();  // Calls function on our pulseSensor object that returns BPM as an "int".

    // If there's no last valid BPM recorded or the current BPM change is within 12 and BPM is within allowed range
    if ((lastBPM == -1 || (abs(myBPM - lastBPM) <= 12)) && (myBPM >= 40 && myBPM <= 120)) {
      Serial.println(myBPM);
      lastBPM = myBPM;  // Update lastBPM to current myBPM
    } else if (myBPM >= 40 && myBPM <= 120) {
      // If the initial BPM reading is valid, update lastBPM
      lastBPM = myBPM;
    }
  }

  delay(20);  // Considered best practice in a simple sketch.
}
