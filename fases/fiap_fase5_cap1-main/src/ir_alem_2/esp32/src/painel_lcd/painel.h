#ifndef PAINEL_H
#define PAINEL_H

#include <Arduino.h>
#include <LiquidCrystal_I2C.h>

class PainelLCD {
    const uint8_t I2C_ADDR;
    const uint8_t LCD_COLUMNS;
    const uint8_t LCD_ROWS;
    const uint8_t I2C_SDA;
    const uint8_t I2C_SCL;
    LiquidCrystal_I2C lcd;

public:
    PainelLCD(
        const uint8_t i2c_addr,
        const uint8_t lcd_columns,
        const uint8_t lcd_rows,
        const uint8_t i2c_sda,
        const uint8_t i2c_scl)
        : I2C_ADDR(i2c_addr), LCD_COLUMNS(lcd_columns), LCD_ROWS(lcd_rows), I2C_SDA(i2c_sda), I2C_SCL(i2c_scl), lcd(i2c_addr, lcd_columns, lcd_rows) {}

    void setup()
    {
        Wire.begin(I2C_SDA, I2C_SCL);

        lcd.begin(LCD_COLUMNS, LCD_ROWS);  // Inicializa o LCD com o número de colunas e linhas
        lcd.backlight();  // Liga a luz de fundo do LCD

        lcd.setCursor(0, 0);
        lcd.print("Iniciando...");

        lcd.clear();
    }

    void printLCDSerial(const uint8_t col, const uint8_t row, const String& msg) {
        lcd.setCursor(col, row);
        lcd.print("                "); // Limpa a linha (16 espaços)
        lcd.setCursor(col, row);
        lcd.print(msg);
        Serial.println(msg);
    }

    void printFloatLcdSerial(const uint8_t col, const uint8_t row, const String& start, const float& value, const String& end = "")
    {
        if (isnan(value))
        {
            printLCDSerial(col, row, start + " Error");
        } else
        {
            printLCDSerial(col, row, start + String(value) + end);
        }

    }

    uint8_t get_I2C_ADDR() const { return I2C_ADDR; }
    uint8_t get_LCD_COLUMNS() const { return LCD_COLUMNS; }
    uint8_t get_LCD_ROWS() const { return LCD_ROWS; }
    uint8_t get_I2C_SDA() const { return I2C_SDA; }
    uint8_t get_I2C_SCL() const { return I2C_SCL; }
    LiquidCrystal_I2C& get_lcd() { return lcd; }
};

#endif //PAINEL_H
