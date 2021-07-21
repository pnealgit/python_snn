# mnb_js
Simple Markov Network Brain with Javascript

PLEASE NOTE: 

This is not a "framework". This is a HTML5/Javascript program.

Background links:
My own take on networked brains ala Chris Adami's and
his teams ideas.

See: 

 Chris Adami's site (http://adamilab.msu.edu/markov-network-brains/)

 Another good description (http://devosoft.org/a-quick-introduction-to-markov-network-brains/)

 Jefferey Cave's really neat implementation
 (https://medium.com/@jefferey.cave/fun-with-markov-network-brains-8041c35ca883)

 Arend Hintze's "Markov Brains: A Technical Introduction" is also great. (https://arxiv.org/pdf/1709.05601v1.pdf)


Evolution:

1. Generate a population of "BRAINS".
2. Evaluate the fitness of each of the original BRAINS
3. Sort the population descending based on fitness
4. For the best BRAIN (POPULATION[0] after sort)
    - Crossover with a randomly chosen BRAIN from the less fit.
    - Mutate gates depending on mutation rate
5. Evaluate the fitness of the candidata brain 
6. If candidate brain is better than the worst BRAIN, 
   replace worst Brain with candidate brain
7. Go to 4 above.

The Goal:

1. Have a 'rover' go around in a big circle.
2. If the rover "body" touches a wall or a blue square it is dead.
3. The rover accumulates fitness depending on how many times in a row
   it goes straight.
4. The rover has a "Time_to_live". 
5. The rover has a 'BRAIN'.
 

How to Run:
1. Download the repository one way or another.
2. Open a Chrome browser (maybe others will work)
3. Point it at "file:///your fully qualified directory name/index.html -- I use file:///Users/pneal/mnb_js/index.html
4. You should see a red whirling rover in a field of white with blue boxes.
5. Turn on View->Developer->Javascript Console for more info

Overview:

1. The red 'rover' has 3 sensors.
2. The sensors detect whether or not it senses a wall or the side of a cube.
3. The data returned from the sensors is sent to the think module
4. The think module contains the Markov Network Brain (MNB).
5. The think module returns the best sensor choice to use.
6. The rover turns in the direction of the best sensor.

Deep Copy Hassles:

1. I had to do deep copy on the "BRAIN" because mutation and crossover should
not be done on the original too deep object oriented "brain" in the POPULATION array.

2. So I did the JSON trick
    - BRAIN = JSON.parse(JSON.stringify(POPULATION[0]));
    - POPULATION[POP_SIZE-1] = JSON.parse(JSON.stringify(BRAIN))

3. HOWEVER !!! For some reason the JSON trick wouldn't do 
   a true "GATE" object. So I had to rewrite the "NEURONS" item as a
   2 dimensional array. Sigh.

Gates:

1. I use a simple gate structure.
    - 2 input indexes 
    - 2 output indexes
    - a 2x2 matrix of 0 or 1 randomly generated for the truth table

2. I do not use probabilistic, not,neuron,or learning gates.

3. The truth table for each gate is a 2d matrix indexed by the input values

4. The values for each input index points to the binary value at INPUT_STATE[input_index]

5. The values for each output index points to the OUT_STATE[output_index] where the result of the truth table will be written.


