# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError 

class simple_contact(models.Model):
    _name = 'simple_contact.simple_contact'
    _description = 'simple_contact.simple_contact'

    description = fields.Text('Description')
    StudentName = fields.Char('Student Name')
    MarkObtained= fields.Integer('Marks Obtained')
    Grade= fields.Char(compute="_GradeFunc" )

    
    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 =     float(record.value) / 100

    @api.depends('MarkObtained')
    def _GradeFunc (self):
        """ Function doc """
        for record in self:
            if record.MarkObtained >= 90:
                record.Grade='A'
            elif record.MarkObtained >= 80:
                record.Grade='B+'
            elif record.MarkObtained >= 70:
                record.Grade='C'
            elif record.MarkObtained >= 60:
                record.Grade='D'
            elif record.MarkObtained >= 50:
                record.Grade='E'
            elif record.MarkObtained >= 40:
                record.Grade='F'
            else:
                record.Grade="Fail"
 
