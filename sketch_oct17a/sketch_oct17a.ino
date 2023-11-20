const int LED = 14;
const int SEN_1 = 38;
const int SEN_2 = 39;
// add these
const int S_OK  = 0xaa;
const int S_ERR = 0xff;

const int MOTOR_START = 0x02;
const int MOTOR_STOP = 0x03;

const int MOTOR_PIN1 = 1;
const int MOTOR_PIN2 = 2;

const int PWM_FREQUENCY = 500;
const int PWM_CHANNEL = 0;
const int PWM_RESOLUTION = 8; 

const int MOTOR_SET_SPEED = 0x04;


void setup() {
  // pinMode(LED, OUTPUT);
  // pinMode(MOTOR_PIN1, OUTPUT);
  // pinMode(MOTOR_PIN2, OUTPUT);
  // digitalWrite(MOTOR_PIN2, LOW);
  // // register "on_receive" as callback for RX event
  // USBSerial.onEvent(ARDUINO_HW_CDC_RX_EVENT, on_receive);
  USBSerial.begin(9600);

  // ledcSetup(PWM_CHANNEL, PWM_FREQUENCY, PWM_RESOLUTION);
  // ledcAttachPin(MOTOR_PIN1, PWM_CHANNEL);
}

void loop() {
  // int state = USBSerial.read();
  // USBSerial.println(state);
  // delay(2000);  
  // USBSerial.println("F");
  // digitalWrite(MOTOR_PIN1, LOW);
  // digitalWrite(MOTOR_PIN2, HIGH); 
  // delay(2000);

  // // Stop the DC motor
  // USBSerial.println("S");
  // digitalWrite(MOTOR_PIN1, LOW);
  // digitalWrite(MOTOR_PIN2, LOW);
  // delay(1000);

  // // Move DC motor backwards at maximum speed
  // USBSerial.println("B");
  // digitalWrite(MOTOR_PIN1, HIGH);
  // digitalWrite(MOTOR_PIN2, LOW); 
  // delay(2000);

  // // Stop the DC motor
  // USBSerial.println("S");
  // digitalWrite(MOTOR_PIN1, LOW);
  // digitalWrite(MOTOR_PIN2, LOW);
  // delay(1000);
}

void on_receive(void* event_handler_arg, esp_event_base_t event_base, int32_t event_id, void* event_data) {
    // read one byte
    // int state = USBSerial.read();

    // guard byte is valid LED state

    // if (!(state == LOW || state == HIGH || state == MOTOR_START || state == MOTOR_STOP || state == MOTOR_SET_SPEED)) {
    //   // invalid byte received
    //   // report error
    //   USBSerial.write(S_ERR);
    //   return;
    // }

    // update LED with valid state
    // USBSerial.println("Signal received: ");
    // digitalWrite(LED, state);
    // if (state == MOTOR_START){
    //   digitalWrite(MOTOR_PIN1, HIGH);
    //   digitalWrite(MOTOR_PIN2, LOW);
    //   //USBSerial.write(S_OK);
    // } else if (state == MOTOR_STOP){
    //   digitalWrite(MOTOR_PIN1, LOW);
    //   digitalWrite(MOTOR_PIN2, LOW);
    //   //USBSerial.write(S_OK);
    // } else if (state == MOTOR_SET_SPEED){
      // int speed = USBSerial.read();
      // // ledcWrite(PWM_CHANNEL, speed);
      // analogWrite(MOTOR_PIN1, speed);
      // USBSerial.write(S_OK);
    // }
}