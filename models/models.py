# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime

class ProductProduct(models.Model):
    _inherit = 'product.product'


    rotacion = fields.Integer(string='Rotación Semanal')
    
    @api.model
    def calcular_rotacion(self):
        semanas_a_restar = 4 # Cambia el número de semanas que deseas restar        
        fecha_actual = datetime.datetime.now()
        fecha_nueva = fecha_actual - datetime.timedelta(weeks=semanas_a_restar)        
        domain=[
            ('create_date','>=',fecha_nueva)
        ]
        product_ids=self.search([('active','=',True)])

        for p in product_ids:
            domain=[
                ('create_date','>=',fecha_nueva),
                ('product_id','=',p.id)
            ]

            stock=p.qty_available
            ventas_semanal=self.env['pos.order.line'].search(domain)
            if ventas_semanal:
                sum_cantidad=0
                for v in ventas_semanal:
                    sum_cantidad+=v.qty
                avg_cantidad=sum_cantidad/semanas_a_restar
                if avg_cantidad!=0:
                    rotacion=stock/avg_cantidad
                else:
                    rotacion=0
            else:
                rotacion=0
            
            p.rotacion=rotacion
