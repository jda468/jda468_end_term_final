# (3) A function knn_predict(m, x_test) where x_test is a sequence of explanatory variables, which returns a sequence of predictions, one for each row of data.
def knn_predict(m, x_test):
    """creates an open list, predictions, where x_test predictions from the function will be stored"""
    predictions = []
    """for loop that, for each explanatory variable in x_test, looks for the best 3 matches, or neighbors,
    and appends the best matches to the predictions dictionary."""
    for i in range(len(x_test)):
        import sys
        """sys.float_info.max is a built in python module that allows for the editing of variables.
        Here it is used to create a tuple, best_match, that contains informtion about the float
        type, since the knn predict function will not give back simple integers we need to use a float.
        The .max  attribute ensures that the best_match tuple stores as many decimal points as possible in the tuple"""
        best_match = sys.float_info.max
        """the best_match indexing here ensures the resulting data is stored properly"""
        best_match_index = -1
        """for loop that takes all explanatory variables in x_test and calculates the distance
        between each data point and another data point using eucledian distance.  If a best neighbor
        is found it is then stored into best_match and indexed iteratively.  These results are 
        then appended into the predictions list which was created earlier, and returns this list of predictions"""
        for j in range(len(m[0])):
            """creates an open list called distances where the 3 nearest neighbors will later
            be stored"""
            distances = []
            d = distance_euc(m[0][j], x_test[i])
            if d = best_match:
                best_match = d
                best_match_index = j
                """the new list, distances, will store the matches and indexes for all best matches.
                the if statement was changed to not replace best matches that are also less than 
                the best match, so the function will search for multiple neighbors."""
        distances.append(d,j)([best_match_index])
    return distances
