"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher, Mark Hays,
         Aaron Wilkin, their colleagues, and Logan Jilek.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:

    # two_circles()
    # circle_and_rectangle()
    lines()


def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # Done: 2. Implement this function, per its green doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.pdf  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # -------------------------------------------------------------------------
    window1 = rg.RoseWindow(800, 800)
    circle1 = rg.Circle(rg.Point(200, 200), 100)
    circle1.attach_to(window1)
    circle1.fill_color = rg.Color(255, 1, 1)

    circle2 = rg. Circle(rg.Point(400, 400), 150)
    circle2.attach_to(window1)

    window1.render(1 / 24)
    window1.close_on_mouse_click()


def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # -------------------------------------------------------------------------
    # Done: 3. Implement this function, per its green doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # -------------------------------------------------------------------------
    window2 = rg.RoseWindow(800, 800)

    # circle dimensions
    thickness = 5
    print(thickness)
    color = 'blue'
    print(color)
    x = 100
    y = 100
    p = rg.Point(x, y)
    print(p)
    print('Center X coord:', x)
    print('Center Y coord:', y)
    r = 44
    circle_guy = rg.Circle(p, r)
    circle_guy.attach_to(window2)
    circle_guy.fill_color = color

    # rectangle dimensions
    a = 400
    b = 400
    c = 600
    d = 500
    print(thickness)
    rect_color = None
    print(rect_color)
    print('Rectangle corner 1:', rg.Point(a, b))
    print('Rectangle Corner 2:', rg.Point(c, d))

    rectangle_guy = rg.Rectangle(rg.Point(a, b), rg.Point(c, d))
    rectangle_guy.attach_to(window2)
    rectangle_guy.fill_color = rect_color

    window2.render(1/24)
    window2.close_on_mouse_click()


def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # TODO: 4. Implement and test this function.

    line_window = rg.RoseWindow(500, 500)

    # Line 1
    line_guy1 = rg.Line(rg.Point(200, 200), rg.Point(400, 200))
    line_guy1.attach_to(line_window)
    print(line_guy1.get_midpoint())
    # HOW DO I DO THISSSSSS?

    # Line 2
    line_guy2 = rg.Line(rg.Point(300, 300), rg.Point(100, 400))
    line_guy2.attach_to(line_window)
    line_guy2.thickness = 20
    line_window.render(1/24)
    line_window.close_on_mouse_click()

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
