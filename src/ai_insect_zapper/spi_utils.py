from dataclasses import dataclass
import spidev as sp
import sys
import time

@dataclass
class SPIObject:
    name: str
    bus: int
    device: int
    hertz: int = 2_000_000
    mode: int = 0b00

class SimpleSpi:
    def __init__(self):
        self.spis = dict()
    
    def __str__(self) -> str:
        final_str = f''
        for name, obj in self.spis.items():
            final_str += f'''{name}:
            bus - {obj.bus}
            device - {obj.device}
            hertz - {obj.hertz}
            mode - {obj.mode}
            '''
        
        return final_str

    def __del__(self):
        for name, obj in self.spis.items():
            obj.close()
    
    def add_spi(self, spi_obj: SPIObject):
        new_spi = sp.SpiDev()
        new_spi.open(spi_obj.bus, spi_obj.device)
        new_spi.max_speed_hz = spi_obj.hertz
        new_spi.mode = spi_obj.mode
        
        self.spis[spi_obj.name] = new_spi
    
    def get_spi(self, spi_name: str):
        try:
            return self.spis[spi_name]
        except KeyError as e:
            print(f'Error finding SPIObject {spi_name} -> {e}')
            return None
        
def send_dac(spi_obj, value):
    # value = value & 0x0FFF
    # command = 0x7000 | (value & 0x0FFF)
    # high_byte = (command >> 8) & 0xFF
    # low_byte = command & 0xFF
    # recieved = spi_obj.xfer2([high_byte, low_byte])
    
    if not 0 <= value <= 4095:
        print("Value range: [0, 4095].")
        return
    
    config_bits = 0x7000 | value
    recieved = spi_obj.xfer2([config_bits >> 8, config_bits & 0xFF])
    
    print(recieved)