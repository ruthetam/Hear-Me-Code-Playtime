BottlesOnTheWall = 100

# for bottle in range(100):
# 	# bottles == bottles-1
# 	print "{0} bottles of beer on the wall. {0} bottles of beer. Take one down, pass it around.".format(BottlesOnTheWall);BottlesOnTheWall = BottlesOnTheWall - 1 ; print "{0} bottles of beer on the wall.".format(BottlesOnTheWall)

while BottlesOnTheWall > 1a:
	print "{0} bottles of beer on the wall. {0} bottles of beer. Take one down pass it around. {1} bottles of beer on the wall".format (BottlesOnTheWall, BottlesOnTheWall -1)
	BottlesOnTheWall = BottlesOnTheWall - 1

	if BottlesOnTheWall == 1:
		print "{0} bottle of beer on the wall. {0} bottle of beer. Take one down pass it around. Go to the nearest liquor store!".format (BottlesOnTheWall)
