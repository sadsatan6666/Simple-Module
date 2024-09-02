from odoo import models, fields, api
from odoo.exceptions import ValidationError 

class subject(models.Model):
    _name = 'simple_contact.subject'
    _description = 'subjects'
    name=fields.Char("Subject Name")
    student_id=fields.Many2one("simple_contact.simple_contact",string="Student ",    domain=[("StudentName", "ilike", "%(search)%")])


    MarkObtained= fields.Integer('Marks Obtained')
    MarkRange=fields.Integer("Mark Range")
    Percentage=fields.Float(compute="_Percentage" )
    Grade= fields.Char(compute="_GradeFunc" )
    overall_percentage=fields.Float(compute="_overall_percentage",string="Overall Percentage")
    overall_grade=fields.Char(compute="_overall_grade",string="Overall Grade")
    
    @api.depends('MarkObtained','MarkRange')
    def _overall_percentage (self):
        """ Function doc """
        for record in self:
            total_marks_obtained=sum (subject.MarkObtained for subject in self.env['simple_contact.subject'].search([]))
            total_marks_range=sum(subject.MarkRange for subject in self.env['simple_contact.subject'].search([]))

            if total_marks_range > 0:
                record.overall_percentage=(total_marks_obtained / total_marks_range) * 100
            else:

                record.overall_percentage=0
            
    @api.depends('overall_percentage')
    def _overall_grade (self):
        """ Function doc """
        for record in self:
            if record.overall_percentage >= 90:
                record.overall_grade='A'
            elif record.overall_percentage >= 80:
                record.overall_grade='B+'
            elif record.overall_percentage >= 70:
                record.overall_grade='C'
            elif record.overall_percentage >= 60:
                record.overall_grade='D'
            elif record.overall_percentage >= 50:
                record.overall_grade='E'
            else:
                record.overall_grade='Fail'
                
                
    @api.depends('MarkObtained','MarkRange')
    def _Percentage (self):
        """ Function doc """
        for record in self:
            if record.MarkRange:
                record.Percentage= (record.MarkObtained / record.MarkRange) * 100
            else:
                record.Percentage=0

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
    
  
        
