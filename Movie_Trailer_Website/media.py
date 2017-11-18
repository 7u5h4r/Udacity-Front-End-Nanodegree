# following line imports webbrowser to connect and work with webbrowser
import webbrowser


# following code creates class movie and two functions namely __init__ and
# show_trailer where init works as constructor and show_trailer opens the
# webbrowser and shows the trailer of movie
class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
