import math
import json

def main():
    print("Hello from homework-streaming-service-analyse!")



movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

#FIRST STAGE

def average_rating(movies):
    """Вычисляет среднее значение рейтинга списка фильмов
    Args:
        movies: Список объектов фильмов
    Returns:
        среднее значение рейтинга фильмов
    """
    count_rating = 0
    final_rating = 0.0

    for movie in movies:
        final_rating += movie["rating"]
        count_rating += 1

    return round(final_rating / count_rating, 1)

def catalog_age_stats(movies, current_year=2026):
    """Определяет самый старый фильм, самый новый фильм и среднее значение года
    Args:
        movies: Список объектов фильмов,
        current_year: текущий год, дефолтное значение=2026
    Returns:
        самый старый фильм, самый новый фильм и среднее значение года
    """
    years = [movie["year"] for movie in movies]

    movie_average = 0
    count_movie = 0
    oldest_movie = min(years)
    newest_movie = max(years) 
    
    
    for movie in movies:
        movie_average += current_year - movie["year"]
        count_movie += 1

    movie_average = math.ceil(movie_average / count_movie)
    return (oldest_movie, newest_movie, movie_average)


def duration_in_hours(minutes):
    """Вычисляет количество часов и минут длительности фильма из минут
    Args:
        minutes: Количество минут фильма
    Returns:
        количество часов и минут длительности фильма
    """
    hours = minutes // 60
    minute = minutes % 60

    return (hours, minute)


#Отладочные методы 
#TODO убрать перед сдачей работы на проверку
print(average_rating(movies))
print("")
print("ДРУГОЙ МЕТОД")
print("")
print(catalog_age_stats(movies))
print("")
print("ДРУГОЙ МЕТОД")
print("")
for movie in movies:
    print(duration_in_hours(movie["duration_min"]))
print("")
print("ДРУГОЙ МЕТОД")
print("")




#SECOND STAGE

def rating_tier(rating):
    rating_value = ""
    if rating < 5:
        rating_value = "слабо"
    elif 6.9 >= rating >= 5:
        rating_value = "средне"
    elif 8.9 >= rating >= 7:
        rating_value = "хорошо"
    elif rating >= 9:
        rating_value = "шедевр"

    return rating_value
        

def decade_label(year):
    film_novelty_indicator = ""
    match year:
        case year if year > 2020:
            film_novelty_indicator = "новые"
        case year if 2015 <= year <= 2020:
            film_novelty_indicator = "недавние"
        case _:
            film_novelty_indicator = "старые"

    return film_novelty_indicator


#Отладочные методы 
#TODO убрать перед сдачей работы на проверку
for movie in movies:
    print(rating_tier(movie["rating"]))
print("")
print("ДРУГОЙ МЕТОД")
print("")
for movie in movies:
    print(decade_label(movie["year"]))





#THIRD STAGE

def not_comedy_movies(movies):
    not_comedy_movies_list = []
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        not_comedy_movies_list.append(movie["title"])
        

    return not_comedy_movies_list


def get_first_masterpiece_movie(movies):
    result = ""
    i = 0
    while i < len(movies):
        current_movie = movies[i]
        if current_movie["rating"] > 9.0:
            result = current_movie["title"]
            break
        i += 1
    else:
        result = "Шедевров не найдено"

    return result

def count_long_movies(movies, threshold=120):
    movie_long_duration_count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            movie_long_duration_count += 1

    return movie_long_duration_count
    

#Отладочные методы 
#TODO убрать перед сдачей работы на проверку
for movie_name in not_comedy_movies(movies):
    print(movie_name)

print("")
print("ДРУГОЙ МЕТОД")
print("")

for movie_name in not_comedy_movies(movies):
        print(movie_name)

print("")
print("ДРУГОЙ МЕТОД")
print("")

print(get_first_masterpiece_movie(movies=movies))

print("")
print("ДРУГОЙ МЕТОД")
print("")

print(count_long_movies(movies=movies))
print("")
print("ДРУГОЙ МЕТОД")
print("")




#FOURTH STAGE

def normalize_title(title):
    words = title.split()
    final_titles = []

    for word in words:
        first_letter = word[0].upper()
        another_part_of_title = word[1:]
        new_word = first_letter + another_part_of_title
        final_titles.append(new_word)
    return ' '.join(final_titles)


def make_slug(title):
    norm_title = normalize_title(title)
    lower_title = norm_title.lower()
    return lower_title.replace(" ", "-")


def format_report_line(movie):
    normalize_title_value = normalize_title(movie["title"])
    duration = duration_in_hours(movie["duration_min"])
    return f"'\"{normalize_title_value}\" ({movie["year"]}) - {movie["rating"]}/10, {duration[0]}ч {duration[1]}м, жанры: {', '.join(map(str, movie["genres"]))}'"


#Отладочные методы 
#TODO убрать перед сдачей работы на проверку
print(normalize_title("test case"))
print("")
print("ДРУГОЙ МЕТОД")
print("")

print(make_slug("test case"))
print("")
print("ДРУГОЙ МЕТОД")
print("")

for movie in movies:
    print(format_report_line(movie))
print("")
print("ДРУГОЙ МЕТОД")
print("")




#FIFTH STAGE

def titles_sorted_by_rating(movies):
    sorted_movies = sorted(movies, key = lambda movie: movie["rating"], reverse=True)
    return [movie["title"] for movie in sorted_movies]


def top_n_by_rating(movies, n=3):
    sorted_movies = sorted(movies, key = lambda movie: movie["rating"], reverse=True)
    top_3_movies = sorted_movies[:n]
    movies_tuples_list = []
    for movie in top_3_movies:
        #movie_tuple = f'("{movie["title"]}", {movie["rating"]})'
        #edited_title = movie["title"].replace("'", '"')
        movie_tuple = (movie["title"], movie["rating"])
        movies_tuples_list.append(movie_tuple)

    return json.dumps(movies_tuples_list)



#Отладочные методы 
#TODO убрать перед сдачей работы на проверку
for movie in titles_sorted_by_rating(movies):
    print(movie)
print("")
print("ДРУГОЙ МЕТОД")
print("")
print(top_n_by_rating(movies))

print("")
print("ДРУГОЙ МЕТОД")
print("")



#SIXTH STAGE

def count_by_genre(movies):
    dict_movies = {}
    for movie in movies:
        for genre in movie["genres"]:
            dict_movies[genre] = dict_movies.get(genre, 0) + 1

    return dict_movies
        


#Отладочные методы 
#TODO убрать перед сдачей работы на проверку
print(count_by_genre(movies))
print("")
print("ДРУГОЙ МЕТОД")
print("")


def actor_filmography(movies):
    dict_actors = {}
    for movie in movies:
        for actor in movie["actors"]:
            if dict_actors.get(actor, 0) == 0:
                dict_actors[actor] = []
            dict_actors[actor].append(movie["title"])

    return dict_actors


#Отладочные методы 
#TODO убрать перед сдачей работы на проверку
print(actor_filmography(movies))
print("")
print("ДРУГОЙ МЕТОД")
print("")


def title_rating_pairs_upper_middle(movies):
    avg_rating = average_rating(movies)
    result = {movie_top["title"]: movie_top["rating"] for movie_top in movies if movie_top["rating"] > avg_rating}
    return result


#Отладочные методы 
#TODO убрать перед сдачей работы на проверку
print(title_rating_pairs_upper_middle(movies))
print("")
print("ДРУГОЙ МЕТОД")
print("")


# SEVENTH STAGE


def all_genres(movies):
    set_genres = set()
    for movie in movies:  
        set_genres = set_genres | movie["genres"]
    return set_genres


#Отладочные методы 
#TODO убрать перед сдачей работы на проверку
print(all_genres(movies))
print("")
print("ДРУГОЙ МЕТОД")
print("")


#TODO что делать с двойными кавычками, как в задании?
def common_actors(movie1, movie2):
    return set(movie1["actors"]) & set(movie2["actors"])

print(common_actors(movies[0], movies[3]))
print("")
print("ДРУГОЙ МЕТОД")
print("")


def genres_only_in_one(movies_a, movies_b):
    set_genres_movies_a = set()
    set_genres_movies_b = set()
    for movie_a in movies_a:
        set_genres_movies_a.update(movie_a["genres"])
    for movie_b in movies_b:
        set_genres_movies_b.update(movie_b["genres"])
    return set_genres_movies_a - set_genres_movies_b


print(genres_only_in_one(movies[5:6], movies[:5]))
print("")
print("ДРУГОЙ МЕТОД")
print("")




#EIGHTH STAGE

def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        yield movie if movie["rating"] >= min_rating else None
        print(format_report_line(movie))




if __name__ == "__main__":
    main()
