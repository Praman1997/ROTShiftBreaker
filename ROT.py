#!/bin/env python2

text = open('code.txt','rb').read()

i = -100
while i < 100:
	try:
		print(''.join([chr(ord(c) - i) for c in text]))
	except:
		print('Error Occured in This Line... Moving to the next one...')
	i = i + 1
	print('---------------------------------------------------------------------------------------------------')