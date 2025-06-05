from datetime import datetime
from app.extensions import db, ma
from marshmallow_sqlalchemy import auto_field


# Definição da classe/tabela dos itens
class Itens(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(60), nullable=False)
    create_on = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, id, name):
        self.id = id
        self.name = name

# Schema que funciona com SQLAlchemy
class ItensSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Itens
        load_instance = True

    id = auto_field()
    name = auto_field()
    create_on = auto_field()

# Instâncias separadas para uso individual ou múltiplo
item_schema = ItensSchema()
itens_schema = ItensSchema(many=True)
