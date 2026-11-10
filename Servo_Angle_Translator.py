# You should not modify the signature (name, input, return type) of this function
def translate(angle: float) -> int:
	"""
	Converts an angle in degrees to the corresponding input
	for the duty_u16 method of the servo class

	See https://docs.micropython.org/en/latest/library/machine.PWM.html for more
	details on the duty_u16 method
	"""

	# Your code here
	#if angle is too small, corrects to 1˚
	if angle < 0:
		output = int(((500 + (2500 - 500) * (1 / 180)) / 20000) * 65535)
	#if angle is too large, corrects to 179˚
	elif angle > 180:
		output = int(((500 + (2500 - 500) * (179 / 180)) / 20000) * 65535)
	#if angle is in range, calculates the duty value
	else:
		output = int(((500 + (2500 - 500) * (angle / 180)) / 20000) * 65535)
	return output # Replace with your return value