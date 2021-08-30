        elif (i > northing_cutoff and j <= easting_cutoff):   
            north_west.append(stations[k])
            k=k+1
            
        elif (i < northing_cutoff and j < easting_cutoff):   
            south_west.append(stations[k])
            k=k+1
            
        else: 
            south_east.append(stations[k])
            k=k+1    