# Minecraft vanilla <img src="https://assets.stickpng.com/images/580b57fcd9996e24bc43c301.png" alt="logo" width="43"/>
<p>
  <img src="https://img.shields.io/badge/python-3.9%2B-green">
  <img src="https://img.shields.io/badge/pygame-2.1%2B-green">
  <img src="https://img.shields.io/badge/moderngl-5.6%2B-green">
</p>


This project is a 2D version of the popular game Minecraft, created using Python with the help of Pygame and ModernGL. The primary goal of this project is educational based on computer graphics academic project, aiming to explore and understand various concepts such as procedural terrain generation, managing infinite worlds with chunk systems, and experimenting with different lighting effects and scenarios in a tile-based game environment.

## Installing on Linux

Make sure you have Python 3.9 or newer installed on your system.

- First, download the src folder. You can also get it by extracting it from the downloaded repository.
- Next, you need to install the required dependencies. Open your terminal and run these commands:

```
python3 -m pip install pygame>=2.1
```
```
python3 -m pip install moderngl>=5.6
```
- To start the game, run the main script by typing:
```
python3 "/.../main.py"
```

## Game Controls
The following are the default controls for the game. Customizable input settings will be added later.

Use <kbd>A</kbd> and <kbd>D</kbd> keys to move left and right.
Press <kbd>W</kbd> or <kbd>SPACE</kbd> to jump.
Hold <kbd>SHIFT</kbd> to crouch.
Click the Left Mouse Button (<kbd>LMB</kbd>) to break blocks.
Click the Right Mouse Button (<kbd>RMB</kbd>) to place blocks.
Press <kbd>F3</kbd> to show or hide the debug screen.
Press <kbd>L</kbd> to turn the lighting effects on or off.