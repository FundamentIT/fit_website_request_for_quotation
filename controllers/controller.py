from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class firstController(http.Controller):

    #@http.route('/quotation', type='json', auth='user', website=True, csrf=False)
    @http.route('/quotation', type='json', auth='public', website=True, csrf=False)
    def get_quotation(self, **kw):
        product = kw.get('product')
        product_id = request.env['product.product'].sudo().search(
            [('id', '=', product)])
        current_user = request.env.context.get('uid')
        if not current_user:
            partner_id = self.create_new_partner(kw.get('company'),kw.get('contact'),kw.get('telephone'),kw.get('email'))
        else:
            user = request.env['res.users'].browse(current_user)
            partner_id = user.partner_id.id
        website = request.env['website'].get_current_website()
        request.env['sale.order'].sudo().create({
            'partner_id': partner_id,
            'note': kw.get('message'),
            'website_id': website.id,
            'order_line': [(0, 0, {
                'name': product_id.display_name,
                'product_id': product_id.id,
                'product_uom_qty': kw.get('qty'),
                'product_uom': product_id.uom_id.id,
                #'price_unit': 0.00,
            })],

        })

    def create_new_partner(self, company, contact, telephone, email):
        existing_partner = request.env['res.partner'].sudo().search([('email', '=', email), ('company_type', '=', 'person')]);
        if existing_partner:
            return existing_partner.id

        existing_company = request.env['res.partner'].sudo().search([('name', '=', company), ('company_type', '=', 'company')]);
        if existing_company:
            parent_company = existing_company;
        else:
            parent_company = request.env['res.partner'].sudo().create({'name': company, 'company_type': 'company'});

        new_partner = request.env['res.partner'].sudo().create({'parent_id': parent_company.id, 'name': contact, 'phone': telephone,
                                                                'email': email})
        return new_partner.id


class requestforquote(WebsiteSale):

    @http.route(['/shop/product/<model("product.template"):product>'], type='http', auth="public", website=True)
    def product(self, product, category='', search='', **kwargs):
        res = super(requestforquote, self).product(
            product, category, search, **kwargs)
        if 'quote_sent' in kwargs:
            res.qcontext['quote_sent'] = kwargs['quote_sent']
        return res
