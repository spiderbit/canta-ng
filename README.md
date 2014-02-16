<div id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#sec-1">1. Readme</a>
<ul>
<li><a href="#sec-1-1">1.1. About</a></li>
<li><a href="#sec-1-2">1.2. Why?</a></li>
<li><a href="#sec-1-3">1.3. Dependencies</a></li>
<li><a href="#sec-1-4">1.4. Start</a></li>
</ul>
</li>
</ul>
</div>
</div>

# Readme

## About

Canta-ng is a attempt to rewrite the singstar-like game/learning software canta with the usage of blender game engine and python 3.x.

## Why?

Cantas 3d Engine is Soya3d. 
That leads to several problems, but the most important right now is, that the engine is not maintained very well.

Therefore its hard to distribute / install Canta, its nearly impossible to launch it from windows and even under linux its difficult, too.

There are much more reasons why blender with bge is the better choice as python 3d engine over Soya3d, 
like better integrated developer plattform, migration to a python3 code base and also because
I tought it should be doable and a good challenge and maybe makes 
cantas core functionality more accessible and more usefull for more people ;)

## Dependencies

-   blender

-   mutagenx  (installable with python3-pip)

-   python-configobj

-   Song: ["Bruder Jakob"](https://github.com/spiderbit/canta-media)   (place it either in media/songs in the project root or in ~/.canta/songs)

## Start

1.  run from the console and keep it open: blender game.blend

2.  then move into the field with the cube

3.  press: "p"

4.  if you want to quit before it reaches the end of the song/demo press: "ESC"
