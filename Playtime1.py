bread_slice = 4
peanut_butter = 18
jelly = 1
full_sandwiches = bread_slice/2

# if bread_slice == 2 and peanut_butter == 1 and jelly == 1:
# 	print "It's peanut butter jelly time!"
# if bread_slice >= 2 and peanut_butter >=1 and jelly >=1:

# For full sandwiches (if you have all ingredients)
if bread_slice > 0 and peanut_butter > 0 and jelly > 0:
	if full_sandwiches and full_sandwiches <= peanut_butter and full_sandwiches <= jelly:
		print "You can make {0} sandwiches. Bread is your limiting factor.".format(full_sandwiches)
	if peanut_butter <= full_sandwiches and peanut_butter <= jelly:
			print "You can make {0} sandwiches. Peanut butter is your limiting factor.".format(peanut_butter)
	if jelly <= peanut_butter and jelly <= full_sandwiches:
			print "You can make {0} sandwiches. Jelly is your limiting factor.".format(jelly)

# For open-face sandwiches (if you have an odd # of bread and peanut butter)
if 0 < bread_slice and bread_slice <= peanut_butter and bread_slice <= jelly:
	print "You can make {0} open-face sandwiches. Bread is your limiting factor.".format(bread_slice)

# For peanut butter sandwiches (if you have enough bread and peanut butter)
if jelly == 0:
	if 0 < full_sandwiches and full_sandwiches <= peanut_butter:
		print "You can make {0} peanut butter sandwiches. Get more jelly in your life.".format(full_sandwiches)
	if 0 < peanut_butter and peanut_butter <= full_sandwiches:
		print "You can make {0} peanut butter sandwiches. Get more jelly in your life.".format(peanut_butter)

# For just no peanut butter
if peanut_butter == 0 and bread_slice > 0 and jelly > 0:
	print "No peanut butter? WTF is wrong with you. Add bread and jelly for a good time."

# For just no jelly
if jelly == 0 and bread_slice > 0 and peanut_butter > 0:
	print "No jelly? WTF is wrong with you. Add bread and peanut butter for a good time."

# For just no bread
if bread_slice == 0 and peanut_butter > 0 and jelly > 0:
	print "No bread? WTF is wrong with you. Add peanut butter and jelly for a good time."
