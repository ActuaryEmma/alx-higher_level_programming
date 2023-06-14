#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    weighted_score = 0
    total_weight = 0

    for score, weight in my_list:
        weighted_score += score * weight
        total_weight += weight
    return weighted_score / total_weight
