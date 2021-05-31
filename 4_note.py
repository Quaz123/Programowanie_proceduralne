import datetime


class Note:
    ID = 0

    def __init__(self, text, tag):
        self.text = text
        self.tag = tag
        self.date = str(datetime.date.today())
        type(self).ID += 1
        self.ID = type(self).ID

    def match(self, phrase):
        return phrase in self.text or phrase in self.tag


class Notebook:
    def __init__(self):
        self.notes = []

    def new_note(self, text, tag=""):
        self.notes.append(Note(text, tag))

    def modify_text(self, Id, new_text):
        for note in self.notes:
            if note.ID == Id:
                note.text = new_text
                break

    def modify_tag(self, Id, new_text):
        for note in self.notes:
            if note.ID == Id:
                note.tag = new_text
                break

    def search(self, phrase):
        return [note for note in self.notes if note.match(phrase)]
