class HtmlDocument:
    def __init__(self):
        self._content: str = ""

    def make_bold(self):
        self._content = f'<b> {self._content} </b>'

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, content):
        self._content = content
