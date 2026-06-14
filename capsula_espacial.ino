#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

const int pinoTemp = A0;
const int pinoLuz = A1;

int tela = 0;
unsigned long ultimaTroca = 0;

void setup() {
  lcd.begin(16, 2);
  lcd.print("CAPSULA ESPACIAL");
  lcd.setCursor(0, 1);
  lcd.print("  Iniciando...  ");
  delay(2000);
  lcd.clear();
}

void loop() {
  int leituraTemp = analogRead(pinoTemp);
  float tensao = leituraTemp * 5.0 / 1024.0;
  float temperatura = (tensao - 0.5) * 100.0;
  temperatura = constrain(temperatura, 0, 80);

  int leituraLuz = analogRead(pinoLuz);
  int luminosidade = map(leituraLuz, 0, 1023, 0, 100);

  String status;
  if (temperatura > 60) status = "CRITICO";
  else if (temperatura > 40) status = "ALERTA ";
  else status = "OK     ";

  if (millis() - ultimaTroca > 2500) {
    tela = (tela + 1) % 2;
    ultimaTroca = millis();
    lcd.clear();
  }

  if (tela == 0) {
    lcd.setCursor(0, 0);
    lcd.print("Temp: ");
    lcd.print((int)temperatura);
    lcd.print((char)223);
    lcd.print("C      ");
    lcd.setCursor(0, 1);
    lcd.print("Status: ");
    lcd.print(status);
  } else {
    lcd.setCursor(0, 0);
    lcd.print("Luz: ");
    lcd.print(luminosidade);
    lcd.print("%       ");
    lcd.setCursor(0, 1);
    lcd.print("CAPSULA v1.0    ");
  }

  delay(300);
}
