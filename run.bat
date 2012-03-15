@echo off

echo 1. generate random images
call run-data.bat

echo 2. train neural network in octave
call run-octave.bat

rem run-PyBrain.bat

echo 3. capture Sudoku using webcam
pushd cv
cv.exe
popd

echo 4. split image into fields and postprocess
python split-image.py

echo 5. predict class for each field using trained neural network in octave and call solver
python processAndPredict.py