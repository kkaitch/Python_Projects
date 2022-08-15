"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES

    # Add the animation loop here!
    while True:

        # The switch is controlled by the mouse when clicking.
        if graphics.is_moving:

            # No need, actually
            # Assign vx, vy to get the velocity of the ball.
            # vx = graphics.get_dx()
            # vy = graphics.get_dy()

            # Move and bounce the ball
            graphics.ball.move(graphics.dx, graphics.get_dy())

            # Change direction if hits the board
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                graphics.dx = -graphics.dx  # Use property to do getter and setter
            if graphics.ball.y <= 0 or graphics.ball.y + graphics.ball.height >= graphics.window.height:
                graphics.set_dy(-graphics.get_dy())

            # Check if outside the bottom or out of lives
            if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                lives -= 1
                graphics.reset_ball()
                if lives == 0:
                    break

            # Check if no bricks left
            if graphics.bricks_left == 0:
                graphics.reset_ball()
                break

            # Check if the ball bounces or hits a brick
            if graphics.check_collision():

                # The ball hits the paddle and bounces.
                if graphics.check_collision() is graphics.paddle:
                    if graphics.get_dy() > 0:
                        graphics.set_dy(-graphics.get_dy())

                # The ball hits a brick, removes it and bounces.
                else:
                    graphics.window.remove(graphics.check_collision())
                    graphics.bricks_left -= 1
                    graphics.set_dy(-graphics.get_dy())

        # Pause
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
