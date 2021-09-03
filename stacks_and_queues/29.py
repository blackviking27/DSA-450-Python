# Find the first circular tour that visits all Petrol Pumps

class Solution:
    def tour(self,lis, n):
        start = 0 # index of the petrol pump from which we can complete a tour
        fuel_tank = 0 # extra fuel that we have
        fuel_shortage = 0 # extra fuel that we need

        # starting from the petrol
        for i in range(n):
            # taking the extra fuel
            fuel_tank += lis[i][0] - lis[i][1]

            # if we cannot make the journey with the total amount of fuel we have 
            # then the starting point will not be any of the previous petrol pump
            # thus the nex petrol pump is considered start
            if fuel_tank < 0:
                start = i + 1
                fuel_shortage += fuel_tank
                fuel_tank = 0
        
        # if we can compensate the fuel that we needed before with the extra fuel we have then we can
        # make a loop
        return start if fuel_tank + fuel_shortage >= 0 else - 1