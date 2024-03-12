# -*- coding: utf-8 -*-

from odoo import models, fields, api


class alumnos_fcties_alumno(models.Model):
    _name = 'alumnos_fcties.alumno'
    _description = 'Alumno'

    nombre = fields.Text(string="Nombre", required=True)
    apellidos = fields.Text(string="Apellidos", required=True)
    fecha_nacimiento = fields.Date(string="Fecha de nacimiento", required=True)
    curso_academico = fields.Text(string="Curso académico")
    telefono = fields.Text(string = "Teléfono")
    ciclo_formativo = fields.Selection([('0', 'DAM'), ('1', 'DAW'), ('2', 'SMR')], string="Ciclo formativo")
    periodo_practicas = fields.Selection([('0', 'Abril'), ('1', 'Septiembre')], string="Periodo de prácticas", required=True)
    nota_media = fields.Integer(string = "Nota media", required=True)
    nota_media_texto = fields.Text(string="Nota media formato texto", compute="_value_nota_media_text", store=True)
    empresa = fields.Many2one("alumnos_fcties.empresa", string = "Empresa")


    @api.depends('nota_media')
    def _value_nota_media_text(self):
        resultado = ""
        for record in self:
            if 5 <= record.nota_media <= 6:
                resultado = "Aprobado"
            elif 7 <= record.nota_media <= 8:
                resultado = "Notable"
            elif 9 <= record.nota_media <= 10:
                resultado = "Sobresaliente"
        record.nota_media_texto = resultado

class alumnos_fcties_empresa(models.Model):
    _name = 'alumnos_fcties.empresa'
    _description = 'Empresa'

    nombre = fields.Text(string = "Nombre", required = True)
    contacto = fields.Text(string = "Persona de contacto", required=True)
    tlf = fields.Text(string = "Teléfono de contacto", required = True)
    correo = fields.Text(string = "Correo electrónico", required = True)
    direccion = fields.Text(string = "Dirección", required = True)
    alumnos = fields.One2many("alumnos_fcties.alumno", "empresa", string="Alumnos")

# manuel = self.env['alumnos_fcties.alumno'].search([('nombre', '=', 'Manuel')], limit=1)
    
# access_alumnos_fcties_alumno_coordinador,Alumno coordinador,model_alumnos_fcties_alumno_coordinador,alumno_fcties_coordinador,1,1,1,1
# access_alumnos_fcties_empresa_coordinador,Empresa coordinador,model_alumnos_fcties_empresa_coordinador,alumno_fcties_coordinador,1,1,1,1
# access_alumnos_fcties_alumno_profesor,Profesor alumno,model_alumnos_fcties_alumno_profesor,alumnos_fcties_profesor,1,1,0,0
# access_alumnos_fcties_empresa_profesor,Profesor empresa,model_alumnos_fcties_empresa_profesor,alumnos_fcties_profesor,1,0,0,0
