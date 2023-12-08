from engine import Engine
import scenes


if __name__ == "__main__":
    engine = Engine()

    engine.add_scene(scenes.game.Scene(engine), "Game")

    engine.run()