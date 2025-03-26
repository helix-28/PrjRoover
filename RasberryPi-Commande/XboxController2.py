import pygame

pygame.init()
pygame.joystick.init()

# Initialize the joystick
joystick = pygame.joystick.Joystick(0)
joystick.init()

print(f"Controller detected: {joystick.get_name()}")
print(f"Number of axes: {joystick.get_numaxes()}")
print(f"Number of buttons: {joystick.get_numbuttons()}")
print(f"Number of hats: {joystick.get_numhats()}")

# Start listening for events
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.JOYAXISMOTION:
            # Print the axis motion events (stick movement)
            print(f"Axis {event.axis} moved to {event.value}")

        elif event.type == pygame.JOYBUTTONDOWN:
            # Print button press events (button down)
            print(f"Button {event.button} pressed")

        elif event.type == pygame.JOYBUTTONUP:
            # Print button release events (button up)
            print(f"Button {event.button} released")

        elif event.type == pygame.JOYHATMOTION:
            # Print D-Pad motion events (hat)
            print(f"D-Pad moved to {event.value}")
