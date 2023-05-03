First you need to install matplotlib
In cmd type python -m pip install -U matplotlib

The basic run command (python may also be python3, depending on your computer's settings, mac and linux will generally be python3), using the sudoku in hard1 as the default sudoku

python CW3.py


Adding -explain to the command on top of the base run provides a set of additional intermediate procedures instructions for solving the puzzle
 
python CW3.py -explain


Replaces the default sudoku with the input file on top of the base run

python CW3.py -file inputFileName outputFileName

where inputFileName is the name of the sudoku file and must be in the correct format, e.g. easy3 or something like that. outputFileName is something you can define yourself

python CW3.py -file easy3 easy3.out


On top of the base run, run the output only to step N (N is a number greater than or equal to 1)

python CW3.py -hint N


additionally compare the performance of the two solvers (task1 and task3) on top of the base run, in terms of run time 
Eventually an additional png image file will be saved in the folder

python CW3.py -profile


All of the above commands can be combined, e.g.
python CW3.py -explain -profile
python CW3.py -explain -file easy3 easy3.out
python CW3.py -explain -hint 10 -file hard1 hard1.out -profile
python CW3.py -hint 3 -file med1 med1.out -profile
etc.

Finally, to choose which solve, task1 or task3 to run, comment out one of the calls in the solve function in the code and uncomment the other