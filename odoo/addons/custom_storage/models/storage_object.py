from odoo import models, fields, api

class StorageLocation(models.Model):
    _name = 'storage.location'
    _description = 'Lugar de Almacenamiento'
    _parent_name = "parent_id"
    _parent_store = True
    _rec_name = 'complete_name'
    _order = 'complete_name'

    name = fields.Char(string="Nombre", required=True)
    complete_name = fields.Char('Nombre Completo', compute='_compute_complete_name', store=True)
    parent_id = fields.Many2one('storage.location', string='Lugar Padre', ondelete='cascade')
    child_ids = fields.One2many('storage.location', 'parent_id', string='Sub-lugares')
    parent_path = fields.Char(index=True)
    
    # Relación con objetos para el conteo
    object_ids = fields.One2many('custom_storage.object', 'location_id', string="Objetos")
    object_count = fields.Integer(string="Cantidad de Objetos", compute='_compute_object_count')

    @api.depends('name', 'parent_id.complete_name')
    def _compute_complete_name(self):
        for loc in self:
            if loc.parent_id:
                loc.complete_name = f"{loc.parent_id.complete_name} / {loc.name}"
            else:
                loc.complete_name = loc.name

    def _compute_object_count(self):
        for loc in self:
            loc.object_count = len(loc.object_ids)

class StorageObject(models.Model):
    _name = 'custom_storage.object'
    _description = 'Objeto'

    name = fields.Char(string="Nombre del Objeto", required=True)
    location_id = fields.Many2one('storage.location', string="Lugar", required=True)
    quantity = fields.Integer(string="Cantidad", default=1)
    state = fields.Selection([
        ('new', 'Nuevo'),
        ('good', 'Bueno'),
        ('regular', 'Regular'),
        ('bad', 'Malo')
    ], string="Estado", default='good', required=True)
    user_id = fields.Many2one('res.users', string="Propietario", default=lambda self: self.env.user)