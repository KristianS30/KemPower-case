# roomlight.py
# Created by: Kristian Schmidt

from os import system

class Light:
    name: str
    is_on: bool
    brightness: int
    warmth: int
    room_number: int

    def __init__(self, p_name: str, p_room_number: int, p_light_on: bool = True) -> None:
        self.name = p_name
        self.is_on = p_light_on
        self.brightness = 5     # Max brightness: 10
        self.warmth = 5         # Max warmth: 10
        self.room_number = p_room_number

    def turn_on(self) -> None:
        self.is_on = True

    def turn_off(self) -> None:
        self.is_on = False

    #REQ_007 You can control the brightness and color of the lights  
    def edit_light(self) -> None:
        while True:
            print("(1) Change name | (2) Change brightness | (3) Change warmth | (0) Back")
            option = input("Enter choice: ")
            print("")
            
            match option:
                case "1":
                    # REQ_010 You can name the lights in the controller for ease of use
                    self.name = input("Change the name from " + self.name + " to: ")
                case "2":
                    self.brightness = int(input("Change the brightness from " + str(self.brightness) + " to (0-10): "))
                case "3":
                    self.warmth = int(input("Change the warmth from " + str(self.warmth) + " to (0-10): "))
                case "0":
                    break
                case _:
                    print("Unknown option")
        print("")
    
    def print_info(self) -> None:
        print("Name: " + self.name + " | Room: " + str(self.room_number) +
               " | Brightness: " + str(self.brightness) + " | Warmth: " + str(self.warmth) + " | ", end="")
        if self.is_on:
            print("Status: ON")
        else:
            print("Status: OFF")


# REQ_003 You can create new light presets  
class LightPreset:
    name: str
    brightness: int
    warmth: int

    def __init__(self, p_name: str, p_brightness: int, p_warmth: int):
        self.name = p_name
        self.brightness = p_brightness
        self.warmth = p_warmth
    
    def edit_preset(self, p_light_presets) -> None:
        system("clear||cls")
        print("----- ROOMLIGHT CONTROLLER -----\n")
        while True:
            print(" - Edit preset -")
            print("(1) Change name | (2) Change brightness | (3) Change warmth | (0) Back")
            feed = input("Enter choice: ")
            print("")
            
            match feed:
                case "0":
                    break
                case "1":
                    new_name = input("Change the name from " + self.name + " to: ")
                    for preset in p_light_presets:
                        if new_name == preset.name:
                            print("Preset named '" + new_name + "' already exists.")
                case "2":
                    new_brightness = int(input("Change the brightness from " + str(self.brightness) + " to (0-10): "))
                    if new_brightness > 10:
                        self.brightness = 10
                    else:
                        self.brightness = new_brightness
                case "3":
                    new_warmth = int(input("Change the warmth from " + str(self.warmth) + " to (0-10): "))
                    if new_warmth > 10:
                        self.warmth = 10
                    else:
                        self.warmth = new_warmth
                case _:
                    print("Unknown option")
        print("")
    
    # REQ_007 You can control the brightness and color of the lights
    # REQ_002 You can apply settings to multiple lights simultanously
    def apply_preset(self, p_lights: list[Light]) -> list[Light]:
        for light in p_lights:
            light.brightness = self.brightness
            light.warmth = self.warmth
        return p_lights
    
    def print_info(self) -> None:
        print("Name: " + self.name + " | Brightness: " + str(self.brightness) + " | Warmth: " + str(self.warmth))
                    

class Room:
    lights: list[Light]
    room_number: int
    main_light: Light
    bed_light: Light
    secondary_light: Light

    def __init__(self, 
                 p_room_number: int, 
                 p_main_light: Light, 
                 p_bed_light: Light, 
                 p_secondary_light: Light = None):
        self.room_number = p_room_number
        self.lights = []
        self.main_light = p_main_light
        self.bed_light = p_bed_light
        self.lights.extend([self.main_light, self.bed_light])
        if p_secondary_light is not None:
            self.secondary_light = p_secondary_light
            self.lights.append(self.secondary_light)
        else:
            self.secondary_light = None

    def print_info(self) -> None:
        print("Room number: " + str(self.room_number) + " | The room has " + str(len(self.lights)) + " RoomLights:")
        print("    Main light:       ", end="")
        self.main_light.print_info()
        print("    Bed light:        ", end="")
        self.bed_light.print_info()
        if self.secondary_light is not None:
            print("    Secondary light:  ", end="")
            self.secondary_light.print_info()
        print("")
        
    def add_light(self, p_light: Light) -> None:
        self.lights.append(p_light)

    def turn_lights_on(self) -> None:
        for light in self.lights:
            light.turn_on()
    
    def turn_lights_off(self) -> None:
        for light in self.lights:
            light.turn_off()
            

# REQ_006 You can create preset categories for different room configurations
class RoomPreset:
    name: str
    num_of_lights: int
    light_presets: list[LightPreset]
    main_light_preset: LightPreset
    bed_light_preset: LightPreset
    secondary_light_preset: LightPreset


    def __init__(self, p_name: str, 
                 p_main_light_preset: LightPreset, 
                 p_bed_light_preset: LightPreset, 
                 p_secondary_light_preset: LightPreset = None) -> None:
        self.name = p_name
        self.light_presets = []
        self.main_light_preset = p_main_light_preset
        self.bed_light_preset = p_bed_light_preset
        self.light_presets.append(p_main_light_preset)
        self.light_presets.append(p_bed_light_preset)
        if p_secondary_light_preset is not None:
            self.secondary_light_preset = p_secondary_light_preset
            self.light_presets.append(p_secondary_light_preset)
        else:
            self.secondary_light_preset = None
        self.num_of_lights = len(self.light_presets)
    
    def print_info(self) -> None:
        print("Name: " + self.name + " | The room preset includes these light presets:\n")
        print("     Main light:          ", end="")
        self.main_light_preset.print_info()
        if self.secondary_light_preset is not None:
            print("\n     Secondary light:     ", end="")
            self.secondary_light_preset.print_info()
        print("\n     Bed light:           ", end="")
        self.bed_light_preset.print_info()
        print("")

    def edit_preset(self, p_light_presets: list[LightPreset]) -> None:
        system("clear||cls")
        print("----- ROOMLIGHT CONTROLLER -----\n")
        while True:
            print(" - Edit preset -")
            if self.secondary_light_preset is None:
                print("(1) Change name | (2) Add secondary light | (3) Change light presets | (0) Back")
            else:
                print("(1) Change name | (2) Remove secondary light | (3) Change light presets | (0) Back")
            feed = input("Enter choice: ")
            print("")
            
            match feed:
                case "0":
                    break
                case "1":
                    self.name = input("Change the name from " + self.name + " to: ")
                case "2":
                    if self.secondary_light_preset is None:
                        print("Add secondary light preset")
                        name = input("Enter name: ")
                        brightness = int(input("Enter brightness (1-10): "))
                        warmth = int(input("Enter color warmth (1-10): "))
                        self.secondary_light_preset = LightPreset(name, brightness, warmth)
                        self.light_presets.append(self.secondary_light_preset)
                    else:
                        self.light_presets.remove(self.secondary_light_preset)
                        self.secondary_light_preset = None
                        print("Secondary light removed")
                case "3":
                    system("clear||cls")
                    print("----- ROOMLIGHT CONTROLLER -----\n")
                    print(" - Change presets -\n")
                    print(self.name + "\n")
                    print("Current light presets: ")
                    print("Main light preset")
                    self.main_light_preset.print_info()
                    print("\nBed light preset\n")
                    self.bed_light_preset.print_info()
                    if self.secondary_light_preset is not None:
                        print("Secondary light preset\n")
                        self.secondary_light_preset.print_info()
                        feed = input("Which light preset do you want to change (main, bed or secondary): ")
                    else:
                        feed = input("Which light preset do you want to change (main or bed ): ")
                    for l_preset in p_light_presets:
                        l_preset.print_info()
                    print("")
                    feed2 = input("Type the name of the new preset you want to use (list above): ")
                    for l_preset in p_light_presets:
                        if feed2 == l_preset.name:
                            if feed.lower() == "main":
                                self.main_light_preset = l_preset
                            elif feed.lower() == "bed":
                                self.bed_light_preset = l_preset
                            elif feed.lower() == "secondary" and self.secondary_light_preset is not None:
                                self.secondary_light_preset = l_preset
                            else:
                                print("Invalid input")
                case _:
                    print("Invalid input")

    # REQ_002 You can apply settings to multiple lights simultanously
    def apply_preset(self, p_rooms: list[Room]) -> None:
        for room in p_rooms:
            self.main_light_preset.apply_preset([room.main_light])
            self.bed_light_preset.apply_preset([room.bed_light])
            if self.secondary_light_preset is not None and room.secondary_light is not None:
                self.secondary_light_preset.apply_preset([room.secondary_light])


# Create default rooms and example presets
def initialize(p_room_list: list[Room], 
               p_light_presets: list[LightPreset], 
               p_room_presets: list[RoomPreset]) -> None:
    
    # 8 Rooms total. 4 rooms with three lights and 4 with 2
    # This totals 20 lights, as stated in the prototype scope "03_Prototype_Scope.md"
    number_of_rooms = 8
    start_room_number = 100

    j = 1
    for i in range(number_of_rooms):
        current_room = start_room_number + i
        main_light = Light("RoomLight_" + f"{j:03d}", current_room)
        j += 1
        bed_light = Light("RoomLight_" + f"{j:03d}", current_room)
        j += 1
        
        if i >= 4:
            secondary_light = Light("RoomLight_" + f"{j:03d}", current_room)
            j += 1
            room = Room(current_room, main_light, bed_light, secondary_light)
        else:
            room = Room(current_room, main_light, bed_light)
        p_room_list.append(room)
    
    example_light_preset_1 = LightPreset("LightPreset1", 7, 6)
    example_light_preset_2 = LightPreset("LightPreset2", 3, 2)
    example_light_preset_3 = LightPreset("LightPreset3", 5, 8)
    p_light_presets.extend([example_light_preset_1, example_light_preset_2, example_light_preset_3])

    example_room_preset_1 = RoomPreset("RoomPreset1", example_light_preset_1, example_light_preset_2)
    example_room_preset_2 = RoomPreset("RoomPreset2", example_light_preset_1, example_light_preset_2, example_light_preset_3)
    p_room_presets.extend([example_room_preset_1, example_room_preset_2])


def use_existing_light_preset(p_light_presets: list[LightPreset], 
                              p_room_presets: list[RoomPreset], 
                              p_light_type: str) -> LightPreset | None:
    for l_preset in p_light_presets:
        l_preset.print_info()
    feed = input("Type the name of the light preset you want to use for " + p_light_type + " light (list above): ")
    preset_found = False
    for l_preset in p_light_presets:
        if feed == l_preset.name:
            return l_preset
    print("Preset not found.")
    return None



def print_main_menu() -> str:
    print("----- ROOMLIGHT CONTROLLER -----\n")
    print(" - Home - \n")
    print("(1) - Show rooms and lights")
    print("(2) - Light presets")
    print("(3) - Room presets")
    print("(0) - Exit program\n")
    choice = input("Enter choice: ")
    print("")
    return choice


def preset_menu(p_preset_type: str, 
                p_light_presets: list[LightPreset], 
                p_room_presets: list[RoomPreset], 
                p_rooms: list[Room], 
                recall: bool = False) -> None:
    feed = ""
    if recall:
        feed = "1"
    while True:
        system("clear||cls")
        print("----- ROOMLIGHT CONTROLLER -----\n")
        print(" - " + p_preset_type.capitalize() + " presets -\n")
        if p_preset_type == "light":
            if len(p_light_presets) != 0:
                print(str(len(p_light_presets)) + " light presets found: \n")
                for preset in p_light_presets:
                    preset.print_info()
                    print("")
            else:
                print("No light presets found.\n")
        if p_preset_type == "room":
            if len(p_room_presets) != 0:
                print(str(len(p_room_presets)) + " light presets found: \n")
                for preset in p_room_presets:
                    preset.print_info()
                    print("")
            else:
                print("No room presets found.\n")
        print("(1) Create new preset | (0) Back")
        print("To modify or apply a preset to " + p_preset_type + "(s), type the name of the preset\n")
        if feed == "":
            feed = input("Enter choice / preset name: ")
        print("")
        match feed:
            case "0":
                break
            case "1":
                # REQ_003 You can create new light presets  
                # REQ_006 You can create preset categories for different room configurations  
                system("clear||cls")
                print(" - New " + p_preset_type +" preset -")
                name = input("Enter preset name: ")
                if p_preset_type == "room":
                    num_of_lights = int(input("Enter number of lights (2 or 3): "))
                    types = ["main", "bed", "secondary"]

                    selected_presets = []

                    for i in range(num_of_lights):
                        light_type = types[i]

                        while True:
                            s_feed = input("Create new preset for " + light_type + " light? (y/n): ")

                            if s_feed.lower() == "y":
                                lp_name = input("Enter preset name: ")
                                brightness = min(int(input("Brightness (0-10): ")), 10)
                                warmth = min(int(input("Warmth (0-10): ")), 10)

                                preset = LightPreset(lp_name, brightness, warmth)
                                p_light_presets.append(preset)
                                selected_presets.append(preset)
                                break

                            elif s_feed.lower() == "n":
                                preset = use_existing_light_preset(p_light_presets, p_room_presets, light_type)
                                selected_presets.append(preset)
                                break

                            else:
                                print("Invalid input")
                    if num_of_lights == 2:
                        new_room_preset = RoomPreset(name, selected_presets[0], selected_presets[1])
                    elif num_of_lights == 3:
                        new_room_preset = RoomPreset(name, selected_presets[0], selected_presets[1], selected_presets[2])
                    p_room_presets.append(new_room_preset)
                elif p_preset_type == "light":
                    name = input("Enter name: ")
                    brightness = int(input("Enter brightness (1-10): "))
                    warmth = int(input("Enter color warmth (1-10): "))
                    if brightness > 10:
                        brightness = 10
                    if warmth > 10:
                        warmth = 10
                    else:
                        new_light_preset = LightPreset(name, brightness, warmth)
                        p_light_presets.append(new_light_preset)
                break
            case _:
                if p_preset_type == "light":
                    for l_preset in p_light_presets:
                        if feed == l_preset.name:
                            system("clear||cls")
                            print("----- ROOMLIGHT CONTROLLER -----\n")
                            print(" - Light presets -\n")
                            l_preset.print_info()
                            print("\n(1) Edit preset | (2) Apply preset to lights | (0) Back\n")
                            feed = input("Enter choice: ")
                            print("")
                            match feed:
                                case "0":
                                    pass
                                case "1":
                                    l_preset.edit_preset(p_light_presets)
                                case "2":
                                    # REQ_002 You can apply settings to multiple lights simultanously
                                    for room in p_rooms:
                                        room.print_info()
                                    print("")
                                    print("Type the name(s) of the light(s) you want to apply the preset to (empty stops):")
                                    lights_to_modify: list[Light] = []
                                    while True:
                                        feed = input("Light name: ")
                                        if feed == "":
                                            break
                                        light_found = False

                                        for room in p_rooms:
                                            for light in room.lights:
                                                if feed == light.name:
                                                    lights_to_modify.append(light)
                                                    light_found = True
                                                    break
                                        if not light_found:
                                            print("Light '" + feed + "' not found.")
                                    l_preset.apply_preset(lights_to_modify)
                                case _:
                                    "Invalid input"
                        else:
                            system("clear||cls")
                            print("Preset '" + feed + "' not found.")
                if p_preset_type == "room":
                    for r_preset in p_room_presets:
                        if feed == r_preset.name:
                            system("clear||cls")
                            print("----- ROOMLIGHT CONTROLLER -----\n")
                            print(" - Room presets -\n")
                            r_preset.print_info()
                            print("(1) Edit preset | (2) Apply preset to rooms | (0) Back\n")
                            feed = input("Enter choice: ")
                            print("")
                            match feed:
                                case "0":
                                    pass
                                case "1":
                                    r_preset.edit_preset(p_room_presets)
                                case "2":
                                    # REQ_002 You can apply settings to multiple lights simultanously
                                    for room in p_rooms:
                                        room.print_info()
                                    print("")
                                    print("Type the number of the room you want to apply the preset to (empty stops)")
                                    rooms_to_modify: list[Room] = []
                                    while True:
                                        feed = input("Room number: ")
                                        if feed == "":
                                            break

                                        room_found = False
                                        
                                        for room in p_rooms:
                                            try:
                                                if int(feed) == room.room_number:
                                                    if len(room.lights) == r_preset.num_of_lights:
                                                        rooms_to_modify.append(room)
                                                        room_found = True
                                                    elif len(room.lights) != r_preset.num_of_lights:
                                                        print("The amount of lights in the room and preset dont match.")
                                                        room_found = True
                                            except ValueError:
                                                print("Invalid room number")
                                                continue
                                        
                                        if not room_found:
                                            print("Room " + feed + " not found.")
                                    if len(rooms_to_modify) >= 1:
                                        print("\nAre you sure you want to apply " + r_preset.name + " to the following rooms:")
                                        for room in rooms_to_modify:
                                            room.print_info()
                                        confirm = input("y/n: ")
                                        if confirm.lower() == "y":
                                            r_preset.apply_preset(rooms_to_modify)
                                            rooms_to_modify.clear()
                                            break
                                        else:
                                            rooms_to_modify.clear()
                                            print("Preset applying cancelled.")
                                            break
                                case _:
                                    "Invalid input"
                        else:
                            system("clear||cls")
                            print("Preset '" + feed + "' not found.")
    system("clear||cls")

def light_menu(p_rooms: list[Room]) -> None:
    while True:
        system("clear||cls")
        print("----- ROOMLIGHT CONTROLLER -----\n")
        print(" - Rooms and lights -\n")
        for room in p_rooms:
            room.print_info()
        print("")
        print("(1) Edit light | (2) Turn light on/off | (0) Back\n")
        feed = input("Enter choice: ")
        print("")
        match feed:
            case "0":
                system("clear||cls")
                break
            case "1":
                # REQ_007 You can control the brightness and color of the lights  
                # REQ_010 You can name the lights in the controller for ease of use
                feed = input("Enter the name of the light you want to edit: ")
                print("")
                light_found = False
                for room in p_rooms:
                    for light in room.lights:
                        if light.name == feed:
                            light.edit_light()
                            print("")
                            light_found = True
                if not light_found:
                    print("Light '" + feed + "' not found.")
            case "2":
                feed = input("Enter the name of the light you want to toggle: ")
                print("")
                light_found = False
                for room in p_rooms:
                    for light in room.lights:
                        if light.name == feed:
                            if light.is_on:
                                light.turn_off()
                            else:
                                light.turn_on()
                            print("")
                            light_found = True
                if not light_found:
                    print("Light '" + feed + "' not found.")
            case _:
                print("Invalid input.")

        
def main():
    ROOMS: list[Room] = []
    LIGHT_PRESETS: list[LightPreset] = []
    ROOM_PRESETS: list[RoomPreset] = []

    initialize(ROOMS, LIGHT_PRESETS, ROOM_PRESETS)
    system("clear||cls")

    while True:
        choice = print_main_menu()
        match choice:
            case "0":
                break
            case "1":
                light_menu(ROOMS)
            case "2":
                system("clear||cls")
                preset_menu("light", LIGHT_PRESETS, ROOM_PRESETS, ROOMS)
            case "3":
                system("clear||cls")
                preset_menu("room", LIGHT_PRESETS, ROOM_PRESETS, ROOMS)
            case _:
                system("clear||cls")
                print("Invalid input, try again!")
        print("")
    

    return 0

main()