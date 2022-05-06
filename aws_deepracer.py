# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 21:23:24 2020

@author: ray34
"""
def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''
    
   
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    
   
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  
    
    return float(reward)