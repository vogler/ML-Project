@echo off

echo 4. capture Sudoku using webcam
call run-cv.bat

echo 5. split image into fields and postprocess
python splitImage.py

echo 6. predict class for each field using different methods and call solver
python processAndPredict.py

pause