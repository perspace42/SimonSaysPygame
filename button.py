import pygame
pygame.init()

'''
Class for buttons
'''
class Button(pygame.sprite.Sprite):
    def __init__(self,onColor,offColor,sound,xCor,yCor): # Add given properties as parameters
        pygame.sprite.Sprite.__init__(self)
        # Initialize properties here
        self.onColor = onColor
        self.offColor = offColor
        self.sound = sound
        self.xCor = xCor
        self.yCor = yCor

        self.image = pygame.Surface((200, 200))
        self.image.fill(self.offColor)
        self.rect = self.image.get_rect()
        # Assign x, y coordinates to the top left of the sprite
        self.rect.topleft = (self.xCor,self.yCor)
        self.clicked = False
    '''
    Draws button sprite onto pygame window when called
    '''
    def draw(self, screen):
        # blit image here
        screen.blit(self.image,(self.rect.x, self.rect.y))

    '''
    Used to check if given button is clicked/selected by player
    '''
    def selected(self, mouse_pos):
        # Check if button was selected. Pass in mouse_pos.
        if self.rect.collidepoint(mouse_pos):
            self.clicked = True
            return True
        return False

    '''
    Illuminates button selected and plays corresponding sound.
    Sets button color back to default color after being illuminated.
    '''
    def update(self, screen):
        # Illuminate button to indicate it has been pressed
        self.image.fill(self.onColor)
        # Draw the Change
        self.draw(screen)
        # Play sound
        pygame.mixer.Sound.play(self.sound)
        # Update Display
        pygame.display.update()
        # Illuminate buttone to indicate button press is over
        self.image.fill(self.offColor)
        # Draw The Change
        self.draw(screen)
        # Wait 1/2 A Second Before Updating
        pygame.time.wait(1000)
        # Update Display
        pygame.display.update()

'''Indicate which file is to be run'''
if __name__ == "__main__":
    print("Please run the main.py file instead")
