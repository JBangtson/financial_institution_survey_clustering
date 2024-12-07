# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 07:30:30 2015

@author: John

This file includes functions needed to do k-means or PAM clustering. 
See comments in functions to understand how they work. 

Joel Grus's code from an early version, ported over to Python 3
before Joel did it. 

"""

# Code to perform k-means clustering, from _Data Science from Scratch_
import random
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


# First, some linear algebra functions. K-means likes these, but PAM 
# doesn't need them. 
def scalar_multiply(c, v):
    return( [c * v_i for v_i in v])

def vector_mean(vectors):
    """compute the vector whose i-th element is the mean of the
    i-th elements of the input vectors"""
    n = len(vectors)
    return(scalar_multiply(1/n, vector_sum(vectors)))

def vector_add(v, w):
    """adds two vectors componentwise"""
    return( [v_i + w_i for v_i, w_i in zip(v,w)])

def vector_subtract(v, w):
    """subtracts two vectors componentwise"""
    return([v_i - w_i for v_i, w_i in zip(v,w)])

def vector_sum(vectors):
    total = []
    for vec in vectors :
        if total :
            total = vector_add(total, vec)
        else :
            total = vec
    return(total)

def squared_distance(v, w):
    return( sum_of_squares(vector_subtract(v, w)))

def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return (sum(v_i * w_i for v_i, w_i in zip(v, w)))

def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n"""
    return( dot(v, v))


# K-means functions
def classify(input, means, k) :
    """return the index of the cluster closest to the input"""
    return (min(range(k),
               key=lambda i: squared_distance(input, means[i])))


def train(inputs, k) :
    """ fit a k-means model. Input """
    means = random.sample(inputs, k)
    assignments = None

    while True:
        # Find new assignments
        new_assignments = [classify(input, means, k) for input in inputs]

        # If no assignments have changed, we're done.
        if assignments == new_assignments:
            return(assignments, means)

        # Otherwise keep the new assignments,
        assignments = new_assignments

        for i in range(k):
            i_points = [p for p, a in zip(inputs, assignments) if a == i]
            # avoid divide-by-zero if i_points is empty
            if i_points:
                means[i] = vector_mean(i_points)

def train_dict(input_dict, k, dd = None) :
    """ fit a k-means model to a dictionary
        of lists. First it builds a list of lists
        and calls train. Then it returns a dictionary
        for assignments a list for means.

        Takes an optional argument dd that is a dictionary
        of distances of the form dd[a][b] = distance_between_a_and_b

        """
    inputs = []
    key_list = []
    for kk,v in input_dict.items() :
        key_list.append(kk)
        inputs.append(v)

    assignments, means = train(inputs,k)
    assignments_dict = dict()

    for idx, kk in enumerate(key_list) :
        assignments_dict[kk] = assignments[idx]

    return(assignments_dict,means)


# PAM functions. 
def get_dist(o1,o2,dists) :
    """ 
        helper function to get distances out of 2d dict of dists
    """
    if o1 in dists and o2 in dists[o1] :
        return(dists[o1][o2])
    else :
        return(dists[o2][o1])


def pam_classify (owners, meds, dists) :
    ''' puts owners into clusters. 
        Input: owners (a set of all owners)
               meds (the current medoids)
               dists (distance dictionary with dists[o1][o2] = dist)
        Output: a dictionary with key of owner and value of cluster
    '''
    
    ret_dict = dict()
    k = len(meds)
    
    for own in owners :
        ret_dict[own] = min(range(k),
               key=lambda i: get_dist(own, meds[i], dists))
    
    return(ret_dict)

def get_pam_medoids(assgn, dists) :
    """
        Returns a set of owners that are the medoid of their
        cluster. The list order is arranged along 0, ..., k-1.
        Input: assgn: dictionary of owner -> cluster
               dists: distance dictionary
               
        Output: a list of owners who are the medoids for the clusters.
    """

    def _get_total_distance(m1, owns) :
        # Gets the distance for a medoid candidate.
        d = 0
        for o1 in owns :
            d += get_dist(m1,o1,dists)
        return(d)                
        
    k = max(assgn.values()) + 1        
            
    ret_meds = []    
    for i in range(k) :
        owners = [own for own, clust in assgn.items() if clust==i]
        tot_dists = [_get_total_distance(own,owners) for own in owners]        

        lowest_index = min(range(len(owners)),
                           key=lambda idx: tot_dists[idx])        
        
        ret_meds.append(owners[lowest_index])        
    
    return(ret_meds)    

def PAM(dd, k) :
    """
        takes in distance data and desired k. returns clustering output.
        
        Input
            dd: a dictionary with two keys, k1 and k2. k1 is an owner, 
                k2 is an owner, and the value is the distance between them.
            k: desired number of clusters.
        Output
            assignments: a dictionary of owner to cluster
            medoids: a dictionary of the cluster centers
    """
    
    # Generate our list of owners
    owner_set = set(dd.keys())
    for owner in dd :
        for o2 in dd[owner] :
            owner_set.add(o2)
    
    medoids = random.sample(owner_set,k)
    assignments = None
    
    counter = 0
    while True :
        counter += 1
        if counter > 10 :
            break

        # assign owners to medoids        
        new_assignments = pam_classify(owner_set, medoids, dd)

        # Nothing changed? let's boogie...
        if assignments == new_assignments:
            return(assignments, medoids)
        else :
            assignments = new_assignments

        # calculate new medoids. 
        medoids = get_pam_medoids(new_assignments, dd)


print("Clustering Code Loaded")