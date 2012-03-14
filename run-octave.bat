@echo off
set octave=C:\Octave\3.2.4_gcc-4.4.0\bin\octave.exe
rem for %i in (octave.exe) do @echo. %~$PATH:i
pushd nn
%octave% main.m
popd
pause