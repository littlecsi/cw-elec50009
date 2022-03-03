"""deals with game window such as start menu and score screen.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

  Typical usage example:

  foo = ClassFoo()
  bar = foo.FunctionBar()
"""

# Imports
import sys
import pygame

# Global Constants
BLACK = 0, 0, 0

# Class definition
class Window():
    def __init__(self, width: int, height: int) -> None:
        assert(isinstance(width, int))
        assert(isinstance(height, int))

        pygame.init()

        self.width = width
        self.height = height
        
        self.size = self.width, self.height
        self.screen = pygame.display.set_mode(self.size)

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

            self.screen.fill(BLACK)
            pygame.display.flip()