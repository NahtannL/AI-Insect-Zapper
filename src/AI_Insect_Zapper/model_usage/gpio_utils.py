"""SimpleGPIO: Simplified GPIO and PWM control for Jetson platforms.

Classes:
    SimpleGPIO -- Wrapper class that handles GPIO and PWM initialization,
        output value changes, and cleanup.

Example:
    gpio = SimpleGPIO()
    gpio.setup_gpio([12])
    gpio.setup_pwm([33: 1000.00])
    gpio.clean()

Requirements:
    * Jetson.GPIO package
"""

import Jetson.GPIO as GPIO

GPIO_CLASS_TYPE = GPIO.gpio.PWM

class SimpleGPIO:
    """Simplified interface for GPIO and PWM control.

    This class simplifies the abstraction of the Jetson.GPIO library,
    supporting simple initialization, value changes, frequency updates, and
    cleanup.
    """
    def __init__(self, board_mode=GPIO.BOARD):
        GPIO.setmode(board_mode)
        self.pin_dict = {}

    def __str__(self):
        return str(self.pin_dict)
    
    def setup_gpio(self, pin_list: list):
        """Setup GPIO pins for output.

        Configures each pin passed into the function with an initial value of
        GPIO.LOW.

        Keyword arguments:
            pin_list -- list of pins to configure
        
        """
        if not isinstance(pin_list, list):
            print('ERROR: pin_list should be a list of pin(s)')
            return

        for pin in pin_list:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
            self.pin_dict[f'pin{pin}'] = pin
    
    def setup_pwm(self, pin_list: dict):
        """Setup PWM pins for output.

        Configures each pin passed into the function with an initial value of
        GPIO.LOW.

        Keyword arguments:
            pin_list (dictionary) -- pin values to configure 
                (e.g. {pin (int): frequency (float)})
        """
        if not isinstance(pin_list, dict):
            print('ERROR: pin_list should be a dictionary of pin(s)')
            return

        for pin, freq in pin_list.items():
            if not isinstance(pin, int) or not isinstance(freq, float):
                print('ERROR: Invalid type(s). Pin should be of type int and' \
                'frequency should be of type float.')
                return

            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
            pwm = GPIO.PWM(pin, freq)
            pwm.start(0)
            self.pin_dict[f'pin{pin}'] = pwm
    
    def change_value(self, pin, value):
        """Change pin value.

        Changes the pin's value based on its type (GPIO pin or PWM pin). The
        possible values for each type of pin is as listed:
        
        GPIO:
            [0, 1]
        PWM:
            [1 Hz, 408 MHz]

        Keyword arguments:
            pin (string) -- select pin (e.g. 'pin33')
            value (int) -- new value
        """
        queried_pin = self.pin_dict.get(pin)
        
        # Error handling
        if queried_pin is None:
            print('ERROR: Invalid pin.')
            return
        if not isinstance(value, int):
            print('ERROR: Invalid value. value should be of type int')
            return

        # Change value depending on type of pin
        if isinstance(queried_pin, GPIO_CLASS_TYPE): 
            if 0 <= value <= 100:
                queried_pin.ChangeDutyCycle(value)
            else:
                print('ERROR: Duty cycle should be between 0 and 100.')
        elif isinstance(queried_pin, int):
            if 0 <= value <= 1:
                GPIO.output(queried_pin, value)
            else:
                print('ERROR: GPIO value must be either 0 or 1.')
        else:
            print('ERROR: Unable to change pin value.')
    
    def change_freq(self, pin, frequency):
        """Change PWM pin frequency.

        Frequency should be within an acceptable range (0 - 408 MHz).

        Keyword arguments:
            pin (string) -- select pin (e.g. 'pin33)
            frequency (float) -- new frequency
        """
        queried_pin = self.pin_dict.get(pin)

        # Error handling
        if queried_pin is None or not isinstance(queried_pin, GPIO_CLASS_TYPE):
            print('ERROR: Invalid pin.')
            return
        if not isinstance(frequency, float):
            print('ERROR: Invalid frequency. Frequency should be ' \
            'of type float')
        if 1 <= frequency and frequency < 408_000_000:
            print('ERROR: Frequency is out of range (1 - 408 MHz).')
        
        # Change frequency
        queried_pin.ChangeFrequency(frequency)
        
    def clean(self):
        """Cleanup GPIO pins.

        Stops all PWM output pins and cleanup remaining GPIO pins.
        """
        for pin in self.pin_dict.values():
            if isinstance(pin, GPIO_CLASS_TYPE):
                pin.stop()
        
        GPIO.cleanup()