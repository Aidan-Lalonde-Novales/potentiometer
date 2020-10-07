let Resistance = 0
basic.forever(function () {
    Resistance = pins.analogReadPin(AnalogPin.P1)
    basic.showNumber(Resistance)
    basic.pause(1000)
})
