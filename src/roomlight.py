# roomlight.py
# Created by: Kristian Schmidt

class Light:
    name: str
    light_on: bool
    brightness: int
    warmth: int
    room_number: int

    _light_counter = 0

    def __init__(self, p_name: str, p_room_number: int, p_light_on: bool=True) -> None:
        self.name = p_name
        self.light_on = p_light_on
        self.brightness = 0
        self.warmth = 0
        self.room_number = p_room_number

        Light._light_counter += 1

    def edit_light(self) -> None:
        while True:
            print("(1) Change name, (2) Change brightness, (3) -> Change warmth (0) -> Return")
            option = input("Your choice: ")
            
            match option:
                case "1":
                    self.name = input("Change the name from " + self.name + " to: ")
                case "2":
                    self.brightness = int(input("Change the brightness from " + str(self.brightness) + " to (0-10): "))
                case "3":
                    self.warmth = int(input("Change the warmth from " + str(self.warmth) + " to (0-10): "))
                case "0":
                    break
                case _:
                    print("Unknown option")
    
    def set_brightness(self, p_brightness: int) -> None:
        self.brightness = p_brightness

    def get_brightness(self) -> int:
        return self.brightness

    def set_warmth(self, p_warmth: int) -> None:
        self.warmth = p_warmth

    def get_warmth(self) -> int:
        return self.warmth
    
    def print_info(self) -> None:
        print("Light info:")
        print("Name: " + self.name + " | Brightness: " + str(self.brightness) + " | Warmth: " + str(self.warmth))
        if self.light_on:
            print("The light is ON")
        else:
            print("The light is OFF")


class LightPreset:
    name: str
    brightness: int
    warmth: int
    def __init__(self, p_name: str, p_brightness: int, p_warmth: int):
        self.name = p_name
        self.brightness = p_brightness
        self.warmth = p_warmth
    
    def edit_preset(self) -> None:
        while True:
            print("(1) Change name, (2) Change brightness, (3) -> Change warmth (0) -> Return")
            option = input("Your choice: ")
            
            match option:
                case "1":
                    self.name = input("Change the name from " + self.name + " to: ")
                case "2":
                    self.brightness = int(input("Change the brightness from " + str(self.brightness) + " to (0-10): "))
                case "3":
                    self.warmth = int(input("Change the warmth from " + str(self.warmth) + " to (0-10): "))
                case "0":
                    break
                case _:
                    print("Unknown option")
            option = input("\nDo you want to apply these changes to the lights that ")
    
    def apply_preset(self, p_lights: list[Light]) -> list[Light]:
        for light in p_lights:
            light.brightness = self.brightness
            light.warmth = self.warmth
        return p_lights
    
    def print_info(self) -> None:
        print("Preset info:")
        print("Name: " + self.name + " | Brightness: " + str(self.brightness) + " | Warmth: " + str(self.warmth))
                    

class Room:
    lights: list[Light]
    room_number: int

    def __init__(self, p_room_number):
        self.lights = []
        self.room_number = p_room_number

    def print_info(self) -> None:
        print("Room info:")
        print("Room number: " + self.room_number)
        print("Room type: " + self.room_type)
        print("The room has " + str(len(self.lights)) + " RoomLights")
        

    def add_lights(self, p_lights: list[Light]) -> None:
        for light in p_lights:
            light.room_number = self.room_number
            self.lights.append(light)
    

    def remove_lights(self) -> None:
        print("Remove light(s) from room:")
        while True:
            choice = int(input("Select the corresponding number of the light you want to remove (0 to return): ")) - 1
            for i in range(self.lights):
                print("(" + str(i + 1) + ") - " + self.lights[i].name)
            
            match choice:
                case "0":
                    break
                case "1":
                    print(self.lights[0].name + "removed from the room.")
                    self.lights.pop(0)
                case "2":
                    print(self.lights[1].name + "removed from the room.")
                    self.lights.pop(1)
                case "3":
                    print(self.lights[2].name + "removed from the room.")
                    self.lights.pop(2)
                case _:
                    print("Invalid number. Try again.")
            


class RoomPreset:
    name: str
    num_of_lights: int
    light_presets: list[LightPreset]

    def __init__(self, p_name, p_num_of_lights) -> None:
        self.light_presets = []
        self.name = p_name
        self.num_of_lights = p_num_of_lights

        



def main():
    LIGHTS: list[Light]

    for i in range(20):     # 20 lights configuration, per prototype description.
        light_name = f"{(i + 1):03d}"
        room_number == 100
        if i % 2 != 0:      # 2 lights per room
            room_number += i
        LIGHTS.append(Light(light_name, room_number))

    return 0