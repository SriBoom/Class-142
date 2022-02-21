#we have a data without movie poster and a data with movie poster. We are merging them
from asyncore import read
import csv

with open("movies.csv", "r") as f:
    reader=csv.reader(f)
    data=list(reader)
    all_movies=data[1:]
    headers=data[0]
    
headers.append("poster_link")

with open("final.csv", "a+") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)

with open("movies_link.csv", "r") as f:
    reader=csv.reader(f)
    data=list(reader)
    all_movies_links=data[1:]

#some movies doesn't have posters. We are going to add them. 
for movie_item in all_movies:
    #any is a function which goes through the entier data.
    #we are checking in the movie_links to see if the links have a movie name
    poster_found=any(movie_item[8] in movie_link_items for movie_link_items in all_movies_links)
    if poster_found:
        #if we have a movie name which is the same in both the files, we are taking them and merging them in movies.csv
        for movie_link_item in all_movies_links:
            if movie_item[8] == movie_link_item[0]:
                movie_item.append(movie_link_item[1])
                if len(movie_item) == 28:
                    with open("final.csv", "a+") as f:
                        csvwriter=csv.writer(f)
                        csvwriter.writerow(movie_item)