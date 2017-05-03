# Contains a class Movie with all the required attributes.

import webbrowser


class Movie():

    def __init__(self, title, m_description, m_trailer):
        self.title = title
        self.summary = m_description
        self.trailer = m_trailer

    def show_trailer(self, m_title):
        webbrowser.open(m_title)
