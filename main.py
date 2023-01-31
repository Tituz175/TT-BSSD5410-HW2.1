from SortFunctions import quicksort, selection_sort
import random
import csv


def main():
    movies_by_genre = []
    movie_recom = []
    with open("movies.csv", newline="\n") as csvfile:
        movie_reader = csv.reader(csvfile, delimiter=",")
        for row in movie_reader:
            movies_by_genre.append((row[2].split("|")[0], row[1]))

    choice = input("Should I sort the movies? (y/n) ")

    if choice == "y":
        movies_by_genreSort = quicksort(movies_by_genre)
        print("\n===================Sorted Movies===================\n")
        for movie in movies_by_genreSort:
            print(f"{movie[0]}:  {movie[1]}");
        print("\n========================================================\n")

        movie_recommendations = int(input("How many movie recommendations you want? "))
        if movie_recommendations < 3 or movie_recommendations > 7:
            movie_recommendations = 3

        random_index = random.randint(0, len(movies_by_genreSort));

        for i in range(movie_recommendations):
            movie_recom.append(movies_by_genreSort[random_index + i])

        print("\n===================Recommended Movies===================\n")
        for movie in movie_recom:
            print(f"{movie[0]}:  {movie[1]}");
        print("\n========================================================\n")
    else:
        print(movies_by_genre)


if __name__ == "__main__":
    main()
