# Owictrl
This folder contains a number of utilities to control the arm.
It should probably be organised as a module or two, but this is how they are right now.

## armdemo-1.py, armdemo-2.py
simple demo actions

## armtest.py
single arm test program

## edgell.py
Defines a class supporting a low level level protocol to specify the current output state for the arm 

## edgehl.py
Defines an class that supports driving the arm via a high level level language to specify moves in the low level protocol 

## edgelang.py
Defines the high level language used by  edgehl

## edgemock.py
Mock class for the arm

## getch.py
Keyboard capture class

## keydriver.py
Driver program for the driving based upon keyboard input  

## langdriver.py
Driver program for the driving based upon the high level language.

## logutil.py
Logger helper

## lsusb.py
List USB attached devices using pyusb

## stoparm.py
Emergency stop for the arm - only outputs zeroes

## testarm.py
Test program for the arm 

## testarmlang.py
Test suite for the arm language

## testhl.py
Test suite for the high level driver

## testll.py
Test suite for the low level driver
