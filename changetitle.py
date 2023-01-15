# updates browser document title on input changes
# credit @Lendemor

import pynecone as pc

class MyState(pc.State):
    """The app state."""

    title: str

    def update_title(self, v):
        self.title = v


def index():
  return pc.box(pc.input(on_change=MyState.update_title))

app = pc.App(state=MyState)
app.add_page(index, path="", title=MyState.title)
app.compile()
