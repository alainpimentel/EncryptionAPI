from app import db

class PrivateKey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    key = db.Column(db.String(256), unique=True)

    def __repr__(self):
        return '<PrivateKey %r>' % (self.name)

    @property
    def serialize(self):
        return {
            'id'    : self.id,
            'name'  : self.name,
            'key'   : self.key
        }

class PublicKey(db.Model):
    id = db.Column(db.Integer, db.ForeignKey(PrivateKey.id), primary_key=True)
    name = db.Column(db.String(64), unique=True)
    key = db.Column(db.String(256), unique=True)

    def __repr__(self):
        return '<PublicKey %r>' % (self.name)

    @property
    def serialize(self):
        return {
            'id'    : self.id,
            'name'  : self.name,
            'key'   : self.key
        }
