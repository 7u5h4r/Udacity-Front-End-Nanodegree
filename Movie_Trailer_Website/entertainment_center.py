# -*- coding: cp1252 -*-

import media
import fresh_tomatoes


JUSTICE_LEAGUE = media.Movie("Justice League",
                        "Justice League is a 2017 American superhero film,"
                        "based on the DC Comics superhero team of the same name"
                        "consisting of Batman, Superman, Wonder Woman, Flash, Aquaman and Cyborg.", 
						"https://upload.wikimedia.org/wikipedia/en/3/31/Justice_League_film_poster.jpg",
                        "https://www.youtube.com/watch?v=r9-DM9uBtVI")

Thor = media.Movie("Thor: Ragnarok",
                    "Thor: Ragnarok is a 2017 American superhero film"
                    "based on the Marvel Comics character Thor.",
                    "https://upload.wikimedia.org/wikipedia/"
                    "en/7/7d/Thor_Ragnarok_poster.jpg",
                    "https://www.youtube.com/watch?v=ue80QwXMRHg")

BLACK_PANTHER = media.Movie("Black Panther",
                     "lack Panther is an upcoming American superhero film"
                     "based on the Marvel Comics character of the same name.",
                     "https://upload.wikimedia.org/wikipedia/en/0/0c/Black_Panther_film_poster.jpg",
                     "https://www.youtube.com/watch?v=xjDjIWPwcPU")

HOTEL_TRANSYLVANIA_3 = media.Movie("Hotel Transylvania 3",
                           "Hotel Transylvania 3: Summer Vacation (known internationally"
						   "as Hotel Transylvania 3: A Monster Vacation",
                           "https://upload.wikimedia.org/wikipedia/en/"
						   "9/9e/Hotel_Transylvania_3_%282018%29_Poster.jpg",
                           "https://www.youtube.com/watch?v=LyqEhGyeF5g")

X_Men = media.Movie("X-Men: The New Mutants",
                         "The New Mutants is an upcoming American horror fil"
						 " in the superhero genre, based on the Marvel Comics"
						 "team of the same name and distributed by 20th Century Fox.",
                         "https://upload.wikimedia.org/wikipedia"
						 "/en/7/76/The_New_Mutants_poster.jpg",
                         "https://www.youtube.com/watch?v=ig8h9dBON9Q")

Aladdin = media.Movie("Aladdin - The Cave of Wonders",
                         "Aladdin - The Cave of Wonders is the latest Disney classic"
						 "to be given a live action remake.  Following in the footsteps"
						 "of Maleficent, The Jungle Book, Beauty and the Beast and The"
						 "Lion King Reborn, come join Aladdin in a brand new adventure.",
                         "https://vignette.wikia.nocookie.net/disney/images/9/96/MPW-10542.jpg",
                         "https://www.youtube.com/watch?v=SN5Y6Bqxclw")


movies = [JUSTICE_LEAGUE, Thor, BLACK_PANTHER, HOTEL_TRANSYLVANIA_3, X_Men,
          Aladdin]
		  
fresh_tomatoes.open_movies_page(movies)
