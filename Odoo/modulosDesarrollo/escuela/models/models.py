from odoo import models, fields


class escuela_escuelas(models.Model):
    _name = 'escuela.escuelas'
    _description = 'Escuelas'

    denominacion = fields.Text(string="Denominacion")
    logo = fields.Binary(string="Logotipo")
    contacto = fields.Text(string="Contacto")
    

class escuela_cursos(models.Model):
    _name = 'escuela.cursos'
    _description = 'Cursos'

    titulo = fields.Text(string="Título")
    duracion_dias = fields.Integer(string="Duración (días)")
    horas = fields.Float(string="Horas")
    precio = fields.Float(string="Precio")

class escuela_monitores(models.Model):
    _name = 'escuela.monitores'
    _description = 'Monitores'

    codigo = fields.Integer(string="ID")
    nombre = fields.Text(string="Nombre")
    escuela = fields.Many2many('escuela.escuelas', string="Escuelas con las que colabora")


class escuela_alumnos(models.Model):
    _name = 'escuela.alumnos'
    _description = 'Alumnos'

    numero = fields.Integer(string="Numero de matricula")
    nombre = fields.Text(string="Nombre")

