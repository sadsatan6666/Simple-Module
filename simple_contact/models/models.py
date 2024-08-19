# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError 

class simple_contact(models.Model):
    _name = 'simple_contact.simple_contact'
    _description = 'simple_contact.simple_contact'

    description = fields.Text('Description')
    StudentName = fields.Char('Student Name')
    MarkObtained= fields.Integer('Marks Obtained')
    MarkRange=fields.Integer("Mark Range")
    Grade= fields.Char(compute="_GradeFunc" )
    Percentage= fields.Float(compute="_Percentage" )
    
    @api.depends('MarkObtained','MarkRange')
    def _Percentage (self):
        """ Function doc """
        for record in self:
            if record.MarkRange:
                record.Percentage= (record.MarkObtained / record.MarkRange) * 100
            else:
                record.Percentage=0
            

    
    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 =     float(record.value) / 100

    @api.depends('Percentage')
    def _GradeFunc (self):
        """ Function doc """
        for record in self:
            if record.Percentage >= 90:
                record.Grade='A'
            elif record.Percentage >= 80:
                record.Grade='B+'
            elif record.Percentage >= 70:
                record.Grade='C'
            elif record.Percentage >= 60:
                record.Grade='D'
            elif record.Percentage >= 50:
                record.Grade='E'
            elif record.Percentage >= 40:
                record.Grade='F'
            else:
                record.Grade="Fail"
    
