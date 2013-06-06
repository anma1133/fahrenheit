#!/usr/bin/python
import sys

print "Enter temperature in Fahrenheit: ",

try:
	fahrenheit = float(raw_input())
except ValueError:
	print "Error: please enter an integer or float"
else:
	celsius = (fahrenheit - 32) * (5.0/9.0)
	print "Fahrenheit %.2f = %.2f Celsius" % (fahrenheit, celsius)
