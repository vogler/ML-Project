copy sudoku.png ..\cv
pushd ..
python splitImage.py
python processAndPredict.py > models\result.txt
popd
pause