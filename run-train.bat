@echo off

echo 1. generate random images
rem call run-data.bat

echo 2. train neural network (Octave)
call run-octave.bat

echo 3. train neural network (PyBrain)
call run-PyBrain.bat

pause