import sys
import random
import math
from PIL import Image

ERR = -1
SUCCESS = 0
ITERATIONS = 20

def main():

	if len(sys.argv) != 3 and len(sys.argv) != 5:
		print 'Usage: python k_means.py <input_image_file> <number_of_means>'
		sys.exit( ERR )

	im = Image.open( sys.argv[1] )
	width, height = im.size
	M = list( im.getdata() )
	k = int( sys.argv[2] )

	Theta, h = KMeansAlgorithm( M, k )

	temp = [Theta[h[ XYtorow(rowtoXY(row,width,height),width,height) ]] for row in range(len(M))]
	im.putdata( temp )
	im.save( 'out_' + sys.argv[1].replace('.png','') + '_k_' + str(k) + '.png' )
	sys.exit( SUCCESS )

def KMeansAlgorithm( M, k ):

	h = [ random.randint(0, k-1) for i in range( len(M) ) ]
	Theta = [ (0.0,0.0,0.0) for row in range( k ) ]

	for t in range( ITERATIONS ):
		for l in range( k ):
			mean = findMean( M, h, l )
			if mean != -1:
				Theta[l] = mean
		for m in range( len(M) ):
			h[m] = closestK( M[m], Theta )

	Theta = [ ( int(ThetaRow[0]),int(ThetaRow[1]),int(ThetaRow[2]) ) for ThetaRow in Theta ]

	return Theta, h

def findMean( M, h, l ):

	avg = [0.0,0.0,0.0]
	count = 0

	for i in range( len(h) ):
		if h[i] == l:
			avg[0] += float(M[i][0])
			avg[1] += float(M[i][1])
			avg[2] += float(M[i][2])
			count += 1

	if count == 0:
		return -1

	avg[0] = avg[0]/float(count)
	avg[1] = avg[1]/float(count)
	avg[2] = avg[2]/float(count)

	return (avg[0],avg[1],avg[2])

def closestK( v, Theta ):

	candidates = [distance( v, ThetaRow ) for ThetaRow in Theta]
	return candidates.index( min( candidates ) )

def distance( a, b ):

	return math.sqrt( math.pow( float(a[0]) - float(b[0]), 2.0 ) + 
					  math.pow( float(a[1]) - float(b[1]), 2.0 ) + 
					  math.pow( float(a[2]) - float(b[2]), 2.0 ) )

def rowtoXY( row, width, height ):

	if row >= width * height:
		print 'rowtoXY called with an out-of-bound row'
		sys.exit( ERR )

	x = row % width
	y = (row - x)/width

	return [x, y]

def XYtorow( coord, width, height ):

	if coord[1] >= height:
		print 'XYtorow called with an out-of-bound y'
		sys.exit( ERR )

	if coord[0] >= width:
		print 'XYtorow called with an out-of-bound x'
		sys.exit( ERR )

	row = coord[1] * width + coord[0]

	return row

main()
