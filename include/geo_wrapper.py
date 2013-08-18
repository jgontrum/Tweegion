import regions #< German regions defined as polygons

# This class stores all custom functions for geo-calculation in the tweegion project
class GeoFunctions():
    region_dict = regions.regions #< Key: Int 0-6 (see documentation for the region-index!); Value: List of float-tupels (coordinates)

    # Takes a point as a tupel of x and y coordinates and a polygon object and returns true, if it is inside the polygon
    def point_in_poly(self, point, poly):
        # Source: http://geospatialpython.com/2011/08/point-in-polygon-2-on-line.html
        # Edited to return a boolean
        x = point[0]
        y = point[1]
        # check if point is a vertex
        if (x,y) in poly: return True
        # check if point is on a boundary
        for i in range(len(poly)):
            p1 = None
            p2 = None
            if i==0:
                p1 = poly[0]
                p2 = poly[1]
            else:
                p1 = poly[i-1]
                p2 = poly[i]
            if p1[1] == p2[1] and p1[1] == y and x > min(p1[0], p2[0]) and x < max(p1[0], p2[0]):
                return True
        n = len(poly)
        inside = False
        p1x,p1y = poly[0]
        for i in range(n+1):
            p2x,p2y = poly[i % n]
            if y > min(p1y,p2y):
                if y <= max(p1y,p2y):
                    if x <= max(p1x,p2x):
                        if p1y != p2y:
                            xints = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                        if p1x == p2x or x <= xints:
                            inside = not inside
            p1x,p1y = p2x,p2y
        return inside

    # Takes coordinates as a tupel and optional a dict of polygons and returns in which polygon the point lays
    # Example:
    #    geo = geo_functions.GeoFunctions()
    #    line = "12.32424,53.1244"
    #    lat,lon = line.split(",")
    #    region_index = geo.get_region((float(lat),float(lon)))
    def get_region(self, needle, haystack = region_dict):
        # Iterate over all regions and return the index!
        for region in haystack:
            if self.point_in_poly(needle, haystack[region]):
                return region
        return -1
        
if __name__ == "__main__":
   pass