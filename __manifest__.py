# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Maple Pre-Install',
    'category': 'Maple-Vertical',
    'version': '1.0',
    'author': "Portall Solution inc.",
    'website': "portall.ca",
    'summary': 'Pre install for Maple Modules.',
    'description':
        """
Pre-install to allow saving config just before install
================================================

This module provides only dependecies.
        """,
    'depends': [
        'auto_backup',
        'base',
#        'base_phone',        
        'base_location',        
        'contacts',
        'document',
        'fleet',
        'hr',
        'mrp',
        'partner_identification',
        'purchase',
        'sale',
        'stock_calendar',
        'stock_picking_wave',
        'web_favicon',
    ],
    'data': [
    ],
    'qweb': [
#        "static/src/xml/*.xml",
    ],
#    'bootstrap': True,  # load translations for login screen
    'installable': True,
    'application': True,
    'auto_install': False,
}

