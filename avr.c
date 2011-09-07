/*--------------------------------------------------
Filename: avr.c
Author: Akhil K, Jithu Sunny, Rahul CP, Salim Ali
Date: March 1, 2011
Blog: http://jithusunnyk.blogspot.com/
--------------------------------------------------*/

#include <avr/io.h>
#include <util/delay.h>
#include <inttypes.h>

void USARTInit(uint16_t ubrr_value) {

	//Set Baud rate

	UBRRL = ubrr_value;
	UBRRH = (ubrr_value>>8);

	/*Set Frame Format
	>> Asynchronous mode
	>> No Parity
	>> 1 StopBit
	>> char size 8
	*/

	UCSRC=(1<<URSEL)|(3<<UCSZ0);
	//Enable The receiver and transmitter
	UCSRB=(1<<RXEN)|(1<<TXEN);
	
	return;
}
	
char USARTReadChar() {

	//Wait untill a data is available

	while(!(UCSRA & (1<<RXC))) {
		//Do nothing
	}

	//Now USART has got data from host
	//and is available is buffer

	return UDR;
}
	
void USARTWriteChar(char data) {

	//Wait untill the transmitter is ready
	
	while(!(UCSRA & (1<<UDRE))) {
		//Do nothing
	}
	
	//Now write the data to USART buffer
	UDR=data;
 
	return;
}
	
void main() {

	char data;
	DDRC = 0x0f;

	USARTInit(51); //51 is the value calculated for a 4MHz clock. Here is a detailed explanation about this - http://extremeelectronics.co.in/avr-tutorials/using-the-usart-of-avr-microcontrollers/

	while(1) {

		data = USARTReadChar();

		if(data == ’.’) {
			data = USARTReadChar();
	
			switch (data) {
				case ’f’:
					PORTC = 0b00000110;
					break;
				case ’b’:
					PORTC = 0b00001001;
					break;
				case ’l’:
					PORTC = 0b00000010;
					break;
				case ’L’:
					PORTC = 0b00001010;
					break;
				case ’r’:
					PORTC = 0b00000100;
					break;
				case ’R’:
					PORTC = 0b00000101;
					break;
				case ’h’:
					PORTC = 0b00001111;
					break;
				default:
					break;
			}
		}
	}
	return;
}
