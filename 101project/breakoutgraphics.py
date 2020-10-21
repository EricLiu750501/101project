"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10      # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height,x=(window_width-paddle_width)/2,
                            y=window_height-paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)
        # Center a filled ball in the graphical window.
        self.ball = GOval(ball_radius*2, ball_radius*2, x=window_width/2-ball_radius,
                           y=window_height/2-ball_radius)
        self.window.add(self.ball)
        self.ball.filled = True
        # Default initial velocity for the ball.
        random_x = random.randint(1, MAX_X_SPEED)
        self.__vx = random_x
        if random.random() > 0.5:
            self.__vx = -self.__vx
        self.__vy = INITIAL_Y_SPEED
        # Initialize our mouse listeners.
        self.moved = onmousemoved(self.move_paddle)
        self.__is_gaming = False
        # Draw bricks.
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.bricks = GRect(brick_width, brick_height, x=+j*(brick_width+brick_spacing),
                                      y=brick_offset+i*(brick_height+brick_spacing))
                self.bricks.filled = True
                self.set_brick_color(self.bricks, i, j)
                self.window.add(self.bricks)

    def get_vx(self):
        return self.__vx

    def get_vy(self):
        return self.__vy

    def move_paddle(self, mouse):
        """
        control the paddle with the mouse
        """
        self.paddle.x = mouse.x - self.paddle.width/2
        if self.paddle.x < 0:
            self.paddle.x = 0
        if self.paddle.x + self.paddle.width > self.window.width:
            self.paddle.x = self.window.width - self.paddle.width

    @staticmethod
    def set_brick_color(brick, i, j):
        """
        draw color on the bricks
        """
        if i % 5 == 1:
            brick.fill_color = 'red'
        elif i % 5 == 2:
            brick.fill_color = 'orange'
        elif i % 5 == 3:
            brick.fill_color = 'yellow'
        elif i % 5 == 4:
            brick.fill_color = 'green'
        else:
            brick.fill_color = 'blue'
