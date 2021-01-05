import pygame, sys
import math

class Pad:
    def __init__(self):
        self.pad_width = 50
        self.pad_height = 10
        self.direction = None
        self.pad_x = WIDTH//2
        self.pad_y = HEIGHT - self.pad_height
    
    def draw(self, screen):
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(self.pad_x,self.pad_y, self.pad_width,self.pad_height))
        pygame.display.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # checking if key is up
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.direction = 'left'
                if event.key == pygame.K_RIGHT:
                    self.direction = 'right'

            # checking if key is down
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.direction = None
                if event.key == pygame.K_RIGHT:
                    self.direction = None

    def move_direction(self):
        if self.direction == 'left':
            self.pad_x -= 10
        elif self.direction == 'right':
            self.pad_x += 10

class Ball:
    def __init__(self):
        self.ball_radius = 8
        # x and y velocity
        self.velocity = [4,4]
        self.ball_x = WIDTH//2
        self.ball_y = HEIGHT//2

    def ball_physics(self):
        self.ball_x += self.velocity[0]
        self.ball_y += self.velocity[1]

        # reverse its velocityif ball_x collides with left or right side 
        if self.ball_x + self.ball_radius > WIDTH or self.ball_x < 0:
            self.velocity[0] = -self.velocity[0]

        # reverse its velocityif ball_y collides with up or down side 
        if self.ball_y < 0:
            self.velocity[1] = -self.velocity[1]

        # reset if you miss the ball
        if self.ball_y + self.ball_radius > HEIGHT:
            self.ball_x = WIDTH//2
            self.ball_y = HEIGHT//2

    def clear_screen(self,screen):
        screen.fill((0,0,0))

    def draw(self, screen):
        self.ball_physics()
        pygame.draw.circle(screen, (255,255,255), (self.ball_x, self.ball_y), self.ball_radius)
        pygame.display.update()
        self.clear_screen(screen)

    def check_collision(self, pad_x, pad_y):
        #ball_pos
        bx1, by1 = self.ball_x, self.ball_y
        #pad_left_vertex pos
        px1, py1 = pad_x, pad_y
        #pad_right_vertex pos
        px2, py2 = (pad_x + 50), pad_y

        #ac = distance between left-vertex-pos and ball-pos
        ac = math.sqrt( ((bx1-px1)**2) + ((by1-py1)**2) )
        #cb = distance between right-vertex-pos and ball-pos
        cb = math.sqrt( ((px2-bx1)**2) + ((py2-by1)**2) )

        # check if equal pad_width
        if round(ac+cb) <= 50:
            self.velocity[1] = -self.velocity[1]

WIDTH = 600
HEIGHT = 400

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()

    pad = Pad()
    ball = Ball()

    # Game loop
    while True:
        pad.draw(screen)
        ball.draw(screen)
        ball.check_collision(pad.pad_x, pad.pad_y)
        pad.move_direction()
        pad.handle_events()
        clock.tick(50)

main()