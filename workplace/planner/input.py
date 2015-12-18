# Enter route plan in string
# for Example in AB5 => city 'A' has route to city 'B' with weight 5
route = 'AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7'

def computeRouteList():
	routeList = route.replace(' ','').split(',')
	return routeList

routeList = computeRouteList()