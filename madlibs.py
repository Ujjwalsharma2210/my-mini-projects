# Author UjjwalSharma 19/11/2020
# Version 1.0
# This program is a simple madlibs game

import imdb
import random

def getMovie():
    # creating instance of IMDb
    ia = imdb.IMDb()

    # getting top 250 movies
    search = ia.get_top250_movies()

    chosenMovie = search[random.randint(1, 100)]['title']

    listOfElementsFromChosenMovie = chosenMovie.split()

    lengthOfMovie = int(len(listOfElementsFromChosenMovie))

    while lengthOfMovie <= 1 or lengthOfMovie >= 5:

	    chosenMovie = search[random.randint(1, 100)]['title']

	    listOfElementsFromChosenMovie = chosenMovie.split()

    return listOfElementsFromChosenMovie

# for element in getMovie():
#     print(element + " ", end="")
# print()

if __name__ == "__main__":

	movieWordsAsListList = getMovie()

	print(movieWordsAsListList)

