from app import db 

class Book(db.Model): 
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)

#function to return dictionary
    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description
        }

    def to_string(self):
        return f"{self.id}: {self.title} Description: {self.description}"

