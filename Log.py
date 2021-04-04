class Log:

    def __init__(self):
        self.comment_history = []

    def add(self, name, text, time):

        comment = Comment(name, text, time)
        self.comment_history.append(comment)

    def get_latest_comment(self):

        if len(self.comment_history) > 0:
            return self.comment_history[-1].text
        else:
            return 'なつかしい'


class Comment:
    def __init__(self, name, text, time):
        self.name = name
        self.text = text
        self.time = time
