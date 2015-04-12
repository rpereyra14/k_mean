Part 5 - Problem 1 HW 3

The number of bits needed to store the images for different K is the number of bits needed to store the h vector plus the bits needed to store the different K:

	//Width * Hight entries in the h vector, each entry needing floor(log_2(K)) bits to encode for K number of pixel means
	h_vector_bits = Width * Height * floor(log_2(K))

	//24 bits per pixel, K number of pixel means
	K_bits = 24 * K

	bits_needed = h_vector_bits + K_bits