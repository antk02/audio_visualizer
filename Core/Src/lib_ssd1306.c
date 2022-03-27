#include "lib_ssd1306.h"
#include <string.h>
#include <stdint.h>
#include "stm32f1xx_hal.h"

void writeCmd(uint8_t byte)
{
    HAL_I2C_Mem_Write(&SSD1306_I2C_PORT, SSD1306_I2C_ADDRESS, 0x00, 1, &byte, 1, HAL_MAX_DELAY);
}

void writeData(uint8_t* buffer, size_t buffer_size)
{
	HAL_I2C_Mem_Write(&SSD1306_I2C_PORT, SSD1306_I2C_ADDRESS, 0x40, 1, buffer, buffer_size, HAL_MAX_DELAY);
}

//based on ssd1306.h library
void ssd1306_setup()
{
	HAL_Delay(10);
	writeCmd(SSD1306_DISPLAYOFF);
	writeCmd(SSD1306_MEMORYMODE);
	writeCmd(0x00);
	writeCmd(0xB0);
	writeCmd(SSD1306_COMSCANDEC);
	writeCmd(0x00);
	writeCmd(0x10);
	writeCmd(SSD1306_SETSTARTLINE);
	writeCmd(SSD1306_SETCONTRAST);
	writeCmd(0xFF);
	writeCmd(0xA1);
	writeCmd(SSD1306_NORMALDISPLAY);
	writeCmd(SSD1306_SETMULTIPLEX);
	writeCmd(0x1F);
	writeCmd(SSD1306_DISPLAYALLON_RESUME);
	writeCmd(SSD1306_SETDISPLAYOFFSET);
	writeCmd(0x00);
	writeCmd(SSD1306_SETDISPLAYCLOCKDIV);
	writeCmd(0xF0);
	writeCmd(SSD1306_SETPRECHARGE);
	writeCmd(0x22);
	writeCmd(SSD1306_SETCOMPINS);
	writeCmd(0x02);
	writeCmd(SSD1306_SETVCOMDETECT);
	writeCmd(0x20);
	writeCmd(SSD1306_CHARGEPUMP);
	writeCmd(0x14);
	writeCmd(SSD1306_DISPLAYON);
	ssd1306_clear();
	ssd1306_update();
}

void ssd1306_clear()
{
	memset(pixelBuffer, 0, 512);
}

void ssd1306_update()
{
	for(uint8_t i = 0; i < 32/8; i++) {
	    writeCmd(0xB0 + i); // Set the current RAM page address.
	    writeCmd(0x00);
	    writeCmd(0x10);
	    writeData(&pixelBuffer[128*i], 128);
	}
}

void ssd1306_pixel(uint8_t x, uint8_t y)
{
	if ((x < 0) || (x >= 128) || (y < 0) || (y >= 32)) {
		return;
	}
	pixelBuffer[x+y/8*128] |= (1 << (y & 7));
}

void ssd1306_line(uint8_t x, uint8_t h)
{
	for(uint8_t i = 32; i > h; i--) ssd1306_pixel(x, i);
}
