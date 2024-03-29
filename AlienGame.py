from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self): ## This means entering the room, not something else
        print("This scene is not yet configured")
        print("Subclass it and implement enter()")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter

class Death(Scene):

    quips = [
        "You died. You kinda suck at this.",
        "Your Mom would be proud...if she were smarter.",
        "Such a luser."
        "I have a small puppy that's better at this."
        "You're worse than your Dad's jokes."
        "Imagine dying to your own creation"
        "Come on! You literally know exactly what you need to do!"
    ]

    def enter(self):
        
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass

class Map (object):
    
    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map('central corridor')
a_game = Engine(a_map)
a_game.play()