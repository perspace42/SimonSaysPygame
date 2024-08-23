'''
Author: Scott Field
Date: 8/23/2024
Version: 1.0
Purpose:
Create a label that can be used to display on the screen and track a number to each label for
score or other computations
'''
import pygame

class Label:
    def __init__(self, fontPath=None, size=36, color=(255, 255, 255), position=(10, 10)):
        self.color = color
        self.position = position
        self.currentDigit = 0
        self.font = pygame.font.Font(fontPath, size)
        self.surface = self.update_text("")
    
    # Print the current time to the screen.
    def update_time(self, screen: pygame.Surface, time_left):
        # If a new digit has been passed to the function
        if self.currentDigit != time_left or self.currentDigit == 0:
            #Clear the old digit with a black rectangle
            self.clear(screen)
            # Set the current digit equal to the new digit
            self.currentDigit = time_left
            # Reset the color to white
            self.color = (255, 255, 255)
        
        # Set the surface with the current digit
        self.surface = self.update_text(str(self.currentDigit))
        # Draw the digit
        self.draw(screen)

    def draw(self, screen: pygame.Surface):
        screen.blit(self.surface, self.position)

    #Clear the old digit with a black rectangle
    def clear(self, screen):
        rect = self.surface.get_rect(topleft = self.position)
        pygame.draw.rect(screen,(0,0,0),rect)

    def update_text(self,text):
        self.surface = self.font.render(text, True, self.color)
        return self.surface

# Test of TimerLabel
if __name__ == "__main__":
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("TimerLabel Test")

    # Main Test Loop
    timer_label = Label()
    start_time = pygame.time.get_ticks()
    count = current_time = 3

    running = True
    while running and current_time >= 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update and draw the timer
        timer_label.update_time(screen, current_time)
        # Update the display
        pygame.display.update()

        # Calculate elapsed time (divide by 1000 to convert to seconds)
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
        current_time = round(count - elapsed_time)
        print(current_time)

    # Quit Pygame
    pygame.quit()