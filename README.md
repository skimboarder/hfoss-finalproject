# hfoss-finalproject

## Project idea
> Tux is exploring space. Tell him what kind of angle he needs to use to get to the next planet!

Tux is exploring space. Planets will be generated at a random angle of 0<angle<180 on a 15deg increment for clarity. The angle will be drawn in the background to help build the concept in (the other part of the angle will be from the right because of the Unit Circle), Tux will be at the center, and the planet/asteroid that Tux is going to will be on the end of the angle.

For example:

```
     P
    /
   T--
```

## _Planned_ assets
* [Planets](https://opengameart.org/content/17-planet-sprites)
* [Tux](https://opengameart.org/content/tux-the-linux-mascot)

## How to run the POC

* access a device running Sugar
* using the terminal, clone this repo ``` git clone https://github.com/skimboarder/hfoss-finalproject.git ~/Activities/TuxExplorer.activity ```
* Open a new instance of the Develop app (can be found on the Sugar activities website) and select TuxExplorer to edit
* if the TuxExplorer does not appear as a valid Activity, restart your machine and log back in
* you may also find it helpful to go to the list view of the installed activities and star Develop, Terminal, and TuxExplorer
* `git` is pre-installed on the Debian LiveCD of Sugar. You can use `git` like normal

Restarting can be hard... you have to swipe your mouse to the bottom right of the screen and it opens up a navigator style window. In the top right is your user icon. click that and you can restart. 

## Useful Documentation
pygame - https://www.pygame.org/docs/
