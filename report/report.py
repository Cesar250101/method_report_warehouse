# Copyright 2020 Iván Todorovich <ivan.todorovich@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import datetime
from odoo import api, models, fields, tools

class Lote(models.Model):
    _inherit = 'stock.production.lot'

    lote_vencido = fields.Boolean(string='Vencido')

    @api.model
    def calcula_lote_vencido(self):
        lotes=self.search([(True,'=',True)])
        for l in lotes:
            if l.life_date<=datetime.datetime.now():
                l.lote_vencido=True
    


class VencimientoLotes(models.Model):
    _name = 'method_report_warehouse.vcto_lotes'
    _description = "Informe de vencimiento de lotes"
    _auto = False
    # _order = 'product_id desc'

    categ_id = fields.Many2one(comodel_name='product.category', string='Categoria Producto')
    descripcion = fields.Char('Descripción Producto')
    lote_id = fields.Many2one(comodel_name='stock.production.lot', string='Lote')
    fecha_vcto = fields.Datetime('Fecha Vcto Lote')
    stock = fields.Integer('Stock')
    ubicacion_id=fields.Many2one(comodel_name='stock.location', string='Ubicación')        
    lote_vencido = fields.Boolean(string='Vencido')
    
    # @api.model_cr
    # def init(self):
    #     self._cr.execute("""
    #         CREATE OR REPLACE VIEW %s AS (SELECT 
    #             ROW_NUMBER() OVER() AS id,
    #             pc.id categ_id,concat(pp.default_code,' ',pp.barcode,' ' ,pt.name) descripcion,
    #             spl.id lote_id,spl.life_date fecha_vcto,sq.quantity stock,sl.id  ubicacion_id,
    #             now() fecha_actual,spl.lote_vencido lote_vencido 
    #             from stock_production_lot spl,product_product pp,
    #             product_template pt,product_category pc,stock_quant sq,stock_location sl  
    #             where spl.product_id=pp.id  
    #             and pp.product_tmpl_id=pt.id  
    #             and pt.categ_id =pc.id 
    #             and spl.product_id=sq.product_id and spl.id=sq.lot_id  
    #             and sq.location_id =sl.id 
    #             and sl.usage='internal'    
    #         )
    #     """ % (
    #         self._table
    #         #self._select(), self._from(),user, self._group_by(), self._having(),

    #     ))


class ReglasAbastecimiento(models.Model):
    _name = 'method_report_warehouse.reglas_abastecimiento'
    _description = "Informe stock - reglas de abastecimiento"
    _auto = False
    # _order = 'product_id desc'

    categ_id = fields.Many2one(comodel_name='product.category', string='Categoria Producto')
    product_id = fields.Many2one(comodel_name='product.product', string='Producto')
    location_id=fields.Many2one(comodel_name='stock.location', string='Ubicación')            
    stock = fields.Integer('Stock')
    cantidad_minima = fields.Integer('Cantidad Mínima')
    cantidad_maxima = fields.Integer('Cantidad Máxima')
    quiebre = fields.Boolean('Quiebre Stock')
    rotacion = fields.Integer(string='Rotación Semanal')

    # @api.model_cr
    # def init(self):
    #     self._cr.execute("""
    #         CREATE OR REPLACE VIEW %s AS (SELECT 
    #             ROW_NUMBER() OVER() AS id,
    #             pc.id categ_id,
    #             pp.id  product_id,
    #             sl.id location_id,
    #             coalesce(sq.quantity,0) stock,
    #             coalesce(swo.product_min_qty,0) cantidad_minima,
    #             coalesce(swo.product_max_qty,0) cantidad_maxima,
    #             case when coalesce(sq.quantity,0) <=coalesce(swo.product_min_qty,0)	then true else false end quiebre, 
    #             cast(pp.rotacion as integer)	
    #             from product_product pp inner join product_template pt on pp.product_tmpl_id =pt.id
    #             inner join stock_quant sq on sq.product_id=pp.id  
    #             inner join stock_location sl on sq.location_id=sl.id   
    #             left join stock_warehouse_orderpoint swo on sq.product_id=swo.product_id and sq.location_id=swo.location_id  
    #             left join product_category pc on pt.categ_id=pc.id  
    #             where sl.usage='internal'    
    #         )
    #     """ % (
    #         self._table
    #         #self._select(), self._from(),user, self._group_by(), self._having(),

    #     ))


