import arcade

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.BLACK
GAME_TITLE = "Introduction"
GAME_SPEED = 1/60

TIMER_MAXIMUM = 100

# Map phases to their next phase
NEXT_PHASE = {
    'spinning forward': 'waiting',
    'waiting': 'spinning backward',
    'spinning backward': 'waiting again',
    'waiting again': 'spinning forward'
    }

IMAGE_ADA = arcade.load_texture("images/ada.png")
IMAGE_BANNER = arcade.load_texture("images/cisc108_banner.png")

class Cisc108Logo(arcade.Sprite):
    phase: str
    timer: int

    def __init__(self):
        super().__init__()
        self.phase = 'waiting'
        self.timer = 0
        self.center_x = WINDOW_WIDTH/2
        self.center_y = WINDOW_HEIGHT/2
        self.texture = IMAGE_BANNER

    def update_timer(self):
        if self.timer < TIMER_MAXIMUM:
            self.timer += 1
        else:
            self.timer = 0
            self.phase = NEXT_PHASE[self.phase]

    def update_angle(self):
        progress = self.timer / TIMER_MAXIMUM
        if self.phase == 'spinning forward':
            self.angle = 360 * progress
        elif self.phase == 'spinning backward':
            self.angle = 360 * (1 - progress)
        else:
            self.angle = 0

    def update(self):
        self.update_timer()
        self.update_angle()


class Cisc108Game(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)
        self.logo_list = None

    def setup(self):
        arcade.set_background_color(BACKGROUND_COLOR)
        self.logo_list = arcade.SpriteList()
        self.logo_list.append(Cisc108Logo())

    def on_draw(self):
        """ Called when it is time to draw the world """
        arcade.start_render()
        self.logo_list.draw()

    def on_update(self, delta_time):
        self.logo_list.update()

def main():
    window = Cisc108Game()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
