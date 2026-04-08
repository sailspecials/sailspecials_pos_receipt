{
    'name': 'Sailspecials POS Receipt',
    'version': '17.0.1.0.1',
    'summary': 'Custom POS receipt layout for Sailspecials',
    'category': 'Point of Sale',
    'depends': ['point_of_sale'],
    'assets': {
        'point_of_sale._assets_pos': [
            'sailspecials_pos_receipt/static/src/app/receipt/order_receipt.xml',
            'sailspecials_pos_receipt/static/src/css/receipt.css',
        ],
    },
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
}
