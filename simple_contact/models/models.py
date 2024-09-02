# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError 


class simple_contact(models.Model):
    _name = 'simple_contact.simple_contact'
    _description = 'simple_contact.simple_contact'

    StudentName = fields.Char('Student Name')
    subject_id=fields.One2many("simple_contact.subject","student_id",string="Subject")
    description = fields.Text('Description')
                
                
        
