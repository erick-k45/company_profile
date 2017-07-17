# -*- coding: utf-8 -*-
import openerp
from openerp import models, fields, api

class company_profile(models.Model):
    _name = 'company_profile.profile'

    name_c = fields.Char(string="Company Name")
    mission = fields.Text(string="Company Mission")
    view = fields.Text(string="Company View")
    values = fields.Text(string="Company Values")
    image = openerp.fields.Binary("Photo", attachment=True,
        help="This field holds the image used as photo for the employee, limited to 1024x1024px.")
    image_medium = openerp.fields.Binary("Medium-sized photo", attachment=True,
        help="Medium-sized photo of the employee. It is automatically "\
             "resized as a 128x128px image, with aspect ratio preserved. "\
             "Use this field in form views or some kanban views.")
    image_small = openerp.fields.Binary("Small-sized photo", attachment=True,
        help="Small-sized photo of the employee. It is automatically "\
             "resized as a 64x64px image, with aspect ratio preserved. "\
             "Use this field anywhere a small image is required.")

    def _get_default_image(self, cr, uid, context=None):
        image_path = get_module_resource('hr', 'static/src/img', 'default_image.png')
        return tools.image_resize_image_big(open(image_path, 'rb').read().encode('base64'))

    defaults = {
        'active': 1,
        'image': _get_default_image,
        'color': 0,
    }

