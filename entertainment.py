# Demonstration of movie website

import media
import fresh_tomatoes

avatar = media.Movie("Avatar",
                     "AVATAR takes us to a spectacular world beyond imagination, where a reluctant hero embarks on an "
                     "epic adventure, ultimately fighting to save the alien world he has learned to call home.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

a_few_good_men = media.Movie("A Few Good Men",
                             "One man is dead. Two men are accused of his murder. The entire Marines Corps is on "
                             "trial. And 'A Few Good Men' are about to ignite the most explosive episode in US "
                             "military history.",
                             "https://upload.wikimedia.org/wikipedia/en/4/45/A_Few_Good_Men_poster.jpg",
                             "https://www.youtube.com/watch?v=ePo91pMcu94")

inception = media.Movie("Inception",
                        "A skilled extractor is offered a chance to regain his old life as payment for a task "
                        "considered to be impossible.",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")

hangover = media.Movie("Hangover",
                       "Three buddies wake up from a bachelor party in Las Vegas, with no memory of the previous "
                       "night and the bachelor missing. They make their way around the city in order to find their "
                       "friend before his wedding.",
                       "https://upload.wikimedia.org/wikipedia/en/b/b9/Hangoverposter09.jpg",
                       "https://www.youtube.com/watch?v=tcdUhdOlz9M")

school_of_rock = media.Movie("School of Rock",
                             "Jack Black stars as a hell-raising guitarist with delusions of grandeur. Kicked out of "
                             "his band and desperate for work, he impersonates a substitute teacher and turns a class "
                             "of fifth grade high-achievers into high-voltage rock and rollers.",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

frozen = media.Movie("Frozen",
                     "Fearless optimist Anna teams up with Kristoff in an epic journey, encountering Everest-like conditions, and a hilarious snowman named Olaf in a race to find Anna's sister Elsa, whose icy powers have trapped the kingdom in eternal winter.",
                     "https://upload.wikimedia.org/wikipedia/en/0/05/Frozen_%282013_film%29_poster.jpg",
                     "https://www.youtube.com/watch?v=FLzfXQSPBOg")


movie_list = [a_few_good_men, avatar, frozen, hangover, inception, school_of_rock]
fresh_tomatoes.open_movies_page(movie_list)
