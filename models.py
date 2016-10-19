# -*- coding: utf-8 -*-
import datetime
from openerp import models, fields, api

class mutabaah(models.Model):
     _name = 'mutabaah.mutabaah'

     tanggal = fields.Date()


     zuhur = fields.Boolean (default= False, required=True)
     ashar = fields.Boolean (default= False,required=True)
     maghrib = fields.Boolean (default= False,required=True)
     isya = fields.Boolean (default= False,required=True)
     tahajjud = fields.Boolean (default= False,required=True)
     dhuha = fields.Boolean (default= False,required=True)
     tilawah = fields.Char()
     itikaf = fields.Boolean (default= False,required=True)
     shubuh = fields.Boolean(default=False, required=True)




