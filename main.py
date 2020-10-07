Resistance = 0

def on_forever():
    global Resistance
    Resistance = pins.analog_read_pin(AnalogPin.P0)
    basic.show_number(Resistance)
    basic.pause(1000)
basic.forever(on_forever)
