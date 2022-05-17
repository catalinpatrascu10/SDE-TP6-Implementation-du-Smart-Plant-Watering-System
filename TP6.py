rand = 0 
def checkTemperature():
    if input.button_is_pressed(Button.A):
        basic.show_number(input.temperature()) #display the temperature

def checkLuminosity():
    def on_button_pressed_b():
        if input.light_level() < 120: #check the light level
            print("Plants needs more light")
        elif input.light_level() < 10:
            print("Place the plant in a warmer environment")
    input.on_button_pressed(Button.B, on_button_pressed_b)
       
def checkHumidity():
    rand = randint(0, 100); # procentaj umiditate 
    if rand < 60:
        def on_logo_event_pressed():
            print("Watering the plant")
        input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_event_pressed)

def main():
    checkTemperature()
    checkLuminosity()
    checkHumidity()