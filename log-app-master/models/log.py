from db import db


class LogModel(db.Model):
    __tablename__ = 'logs'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String())
    spreadsheet_title = db.Column(db.String())
    spreadsheet_id = db.Column(db.String())
    api_key = db.Column(db.String())
    trigger_source = db.Column(db.String())
    api_hits = db.Column(db.Integer())
    tsa_owner = db.Column(db.String())

    def __init__(self, date, spreadsheet_title, spreadsheet_id, api_key,trigger_source,api_hits,tsa_owner):
        self.date = date
        self.spreadsheet_title = spreadsheet_title
        self.spreadsheet_id = spreadsheet_id
        self.api_key = api_key
        self.trigger_source = trigger_source
        self.api_hits = api_hits
        self.tsa_owner = tsa_owner

    def json(self):
        return {'date': self.date, 'spreadsheet_title': self.spreadsheet_title,'spreadsheet_id': self.spreadsheet_id ,'api_key': self.api_key,'trigger_source': self.trigger_source,'api_hits': self.api_hits,'tsa_owner': self.tsa_owner}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
