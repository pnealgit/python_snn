# python_snn

Implementation by Phillip R. Neal
philn1984@gmail.com

Developed and tested on a clapped out
MacAir running macOS Catalina Verison 10.15.7

For this project, the goal is for the
rover to learn to keep away from the walls ,
the square in the middle and some little squares.

Some of the ideas are from :

Evolution of Spiking Neural Circuits in Autonomous Mobile Robots
Dario Floreano, Yann Epars, Jean-Christophe Zufferey, Claudio Mattiussi
INTERNATIONAL JOURNAL OF INTELLIGENT SYSTEMS, VOL. XX, 2005
(The SNN paper)

Spiking Nerural Networks with a ga are a lot cooler than
the usual Rumelhart-McClelland feed-forward neural networks.
It is a specific case of an extreme learning machine


TO RUN:

Open up a terminal session.

Get to the command line

cd to your python_snn directory

Fire up the node server:

    node server.js &

Then

Open up your Chrome browser and set the url to :

file:///where_you_put_the_repository/python_snn/index.html

You should see a square canvas with some blue squares inside it.

Turn on your javascript console and see if all is ok

Then:

Open up another terminal session.

cd to your python_snn directory again

type: python red_snn.py

Things should start happening.



