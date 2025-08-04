from ai_insect_zapper.spi_utils import SimpleSpi, SPIObject, send_dac

x = SimpleSpi()
x.add_spi(SPIObject('Device 1', 0, 0))

s = x.get_spi('Device 1')
if s is None:
    print('Not found.')
    exit()

send_dac(s, 4095)