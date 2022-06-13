# CodingScientist Anbu Kumar

# Calculate the derivative of an neuron output
def transfer_derivative(output):
	return output * (1.0 - output)