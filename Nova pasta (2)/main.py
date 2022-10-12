#!/usr/bin/python

import os
import cgi
import cgitb
cgitb.enable()

input_data=cgi.FieldStorage()

print ("Content-type: text/html\r\n\r\n")
print()
print ("<h1>Resultado da soma</h1><\br>")
try:
	num1=int(input_data["num1"], value)
	num2=int(input_data["num2"], value)
except:
	print("<p>Desculpa, nao e possivel calcualar o valar em números(informe valores interios.</p>")
	return 1
	sum = num1 + num2
	print (f"<p>{num1}+{num2} = {sum}")