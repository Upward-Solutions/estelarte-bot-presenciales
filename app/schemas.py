from marshmallow import Schema, fields

class CursoSchema(Schema):
    id = fields.Int(dump_only=True)
    titulo = fields.Str(required=True)
    descripcion = fields.Str()
    capacidad = fields.Int(required=True)
    precio = fields.Float(required=True)

class ActividadSchema(Schema):
    id = fields.Int(dump_only=True)
    fecha = fields.Date(required=False)
    horario = fields.Str(required=False)
    id_curso = fields.Int(required=False)
