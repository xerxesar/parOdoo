##############################################################################
#
#    Copyright (C) 2015  ADHOC SA  (http://www.adhoc.com.ar)
#    All Rights Reserved.
#
#
##############################################################################
{
    'name': 'Persian Calendar',
    'version': "17.0.1.0.0",
    'category': 'Utils',
    'summary': 
        """
            Persian Calendar Support.
        """,
    'author': 'parOdoo team.',
    'license': 'AGPL-3',
    'images': [
    ],
    'depends': ['web'
    ],
    "assets": {
        "web.assets_common": [
            (
                "replace",
                "web/static/lib/moment/moment.js",
                "po_persian_calendar/static/src/js/moment-jalaali.js",
            ),
            "web/static/src/js/core/time.js",
            "web/static/lib/tempusdominus/tempusdominus.js",
        ]
    },
    'data': [
        'views/templates.xml',
        'views/UserPreferences_Views.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
