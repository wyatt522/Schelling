This program creates a schnelling model.

In order to run:
Ensure that you are using python 3 and have these packages installed:
    - matplotlib
    - numpy
    - collections

Run either test.py or schelling_dual_thresholds.py
Close plots in order to see the next one.
Access saved files to revisit closed plots.

Adjust parameters in test files as described below to your satisfaction



How the test files run:
Instansiate a model, and the simulate it using model.run_sim().
Run_sim takes in the population fraction, and satisfaction threshold, or 
if using schelling_dual_thresholds the user can add a secondary threshold, as 
well as a fraction that represents what portion of agents will use the first threshold.

Change the iteration variable, or the input parameter to run_sim in order to change the amount 
of iterations the model will run for. It will always generate 5 graphs, and save them to the project 
folder.

