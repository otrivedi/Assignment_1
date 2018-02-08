#!/usr/bin/env python3

import sys
import time
import urban_planner_helpers_v2
import timeit
#Test
from random import shuffle
import numpy as np

max_duration = 10 # 10 seconds
number_boards = 100


# filler functions
def hillclimb():

    return


def genetics(list_of_hill_climbs):
 
    elite_ratio = 0.3
    normal_ratio = 0.3

    mutation_ratio = 0.1   #Can't be greater than  (1-elite_ratio)
    
    #Plceholder score-map
    score_map = np.random.randint(100, size=100)
    
    #Placeholder Elite selction
    elite_maps = list_of_hill_climbs[:int(len(list_of_hill_climbs)*elite_ratio)]
    normal_maps = list_of_hill_climbs[int(len(list_of_hill_climbs)*elite_ratio):int((len(list_of_hill_climbs)*(elite_ratio+normal_ratio)))]
    Maps_to_mutate = normal_maps
    mutation_indices = np.random.choice([i for i in range(len(Maps_to_mutate))],int(len(list_of_hill_climbs)*mutation_ratio)).tolist()
    for i in mutation_indices:
        Maps_to_mutate[i] = urban_planner_helpers_v2.mutate(Maps_to_mutate[i])

    Selected_Mutated_maps = urban_planner_helpers_v2.selection(list_of_hill_climbs,elite_maps,normal_maps)
    
    New_mapset = elite_maps + Selected_Mutated_maps
    print(np.array(New_mapset))
    
    return


if __name__ == '__main__':
    
    timeit.timeit()
    # check to make sure a valid input path was given, exit otherwise
    if len(sys.argv) is 1:
        print("You must provide the path to the input text file")
        sys.exit(-1)

    pathToFile = sys.argv[1]
    print(sys.argv[1])
    
    (num_industrial, num_commercial, num_residential, board_map) = urban_planner_helpers_v2.read_input_file(pathToFile)
    board_size_x = len(board_map)
    board_size_y = len(board_map[0])

    Zoned_board = urban_planner_helpers_v2.Add_zones(board_map,num_residential,num_industrial,num_commercial)
    list_of_hill_climbs = urban_planner_helpers_v2.generate_starting_boards(number_boards, Zoned_board)

    start_time = time.time()
    
    ## placeholder-code for selection
    
    still_computing = True
#    flat_elite = np.array(['X' ,'R' ,'X' ,'I' ,'C' ,'1' ,'2' ,'R' ,'4', 'S', '5', 'I'])
#    flat_normal = np.array(['X', '5', 'X', '2' ,'I' ,'1', 'R', '4' ,'I' ,'S' ,'C' ,'R'])
#    urban_planner_helpers_v2.proper_selection_approach(flat_elite,flat_normal)
    genetics(list_of_hill_climbs)

#    while (time.time() - start_time) < max_duration and still_computing:
#        for board in list_of_hill_climbs:
#            hillclimb()

        # do genetic engineering
#        genetics()
        
