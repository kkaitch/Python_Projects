"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

This program makes a game called "break out".
It sets bricks, the ball, the velocity of ball,
the paddle, and all the items and conditions
which will be used in the game.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 120      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'cadetblue'
        self.paddle.color = 'cadetblue'
        self.window.add(self.paddle, x=(window_width-paddle_width)/2, y=(window_height-paddle_offset-paddle_height))

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.x = window_width/2 - ball_radius
        self.ball.y = window_height/2 - ball_radius
        self.ball.filled = True
        self.ball.fill_color = 'lightblue'
        self.ball.color = 'lightblue'
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmousemoved(self.move_paddle)
        onmouseclicked(self.start)

        # Initialize variables
        self.is_moving = False
        self.bricks_left = brick_rows * brick_cols

        # Draw bricks
        for i in range(0, brick_rows):

            # Assign the color for  the bricks
            color = ''
            if i // 2 == 0:
                color = 'darkolivegreen'
            elif i // 2 == 1:
                color = 'olive'
            elif i // 2 == 2:
                color = 'darksage'
            elif i // 2 == 3:
                color = 'sage'
            elif i // 2 == 4:
                color = 'darkseagreen'

            for j in range(0, brick_cols):
                brick = GRect(brick_width, brick_height)
                brick.filled = True
                brick.fill_color = color
                brick.color = color
                brick.x = j * (brick_width + brick_spacing)
                brick.y = i * (brick_height + brick_spacing) + brick_offset
                self.window.add(brick)

    def move_paddle(self, event):
        """
        This function moves the paddle with the mouse at its center.
        :param event: mouse event, having the position information where the mouse moves
        """
        if self.paddle.width/2 < event.x < self.window.width - self.paddle.width/2:
            self.paddle.x = event.x - self.paddle.width/2

        # To prevent the paddle from moving outside of the left side
        elif event.x < self.paddle.width/2:
            self.paddle.x = 0

        # To prevent the paddle from moving outside of the right side
        else:
            self.paddle.x = self.window.width-self.paddle.width

    def start(self, event):
        """
        This function let the ball start.
        :param event: mouse event, having the position information where the mouse moves
        """
        if not self.is_moving:
            self.is_moving = True
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__dx = -self.__dx

    def reset_ball(self):
        """
        This function reset the position of the ball.
        """
        self.is_moving = False
        self.ball.x = (self.window.width - self.ball.width) / 2
        self.ball.y = (self.window.height - self.ball.height) / 2

    # Getter: get velocity x
    @property
    def dx(self):
        return self.__dx

    # Setter: set velocity x
    @dx.setter
    def dx(self, velocity):
        self.__dx = velocity

    # Getter: get velocity y
    def get_dy(self):
        return self.__dy

    # Setter: set velocity y
    def set_dy(self, velocity):
        self.__dy = velocity

    def check_collision(self):
        """
        Check what the ball hits to further define its action in the front.
        """
        for i in range(0, 2):
            for j in range(0, 2):

                # Get the vertices of the ball
                ball_x = self.ball.x + i*self.ball.width
                ball_y = self.ball.y + j*self.ball.height

                # Detect if there is an object.
                maybe_object = self.window.get_object_at(ball_x, ball_y)

                # Check the ball hits an object.
                if maybe_object:
                    return maybe_object
