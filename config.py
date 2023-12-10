import os

DB_DETAILS = {
    'DEV':{
        'source_db':{
            'DB_TYPE':'MYSQL',
            'DB_HOST':'192.168.1.65',
            'DB_NAME':'sales',
            'DB_USER':os.environ.get('source_db_user'),
            'DB_PASS':os.environ.get('source_db_pass')
        },
        'target_db':{
            'DB_TYPE':'postgres',
            'DB_HOST':'192.168.1.65',
            'DB_NAME':'sales',
            'DB_USER':os.environ.get('target_db_user'),
            'DB_PASS':os.environ.get('target_db_pass')
        }
    },
    'PROD':{
        'source_db':{
            'DB_TYPE':'',
            'DB_HOST':'',
            'DB_NAME':'',
            'DB_USER':'',
            'DB_PASS':''
        },
        'target_db':{
            'DB_TYPE':'',
            'DB_HOST':'',
            'DB_NAME':'',
            'DB_USER':'',
            'DB_PASS':''
        }
    },
    'UAT':{
            'source_db':{
            'DB_TYPE':'',
            'DB_HOST':'',
            'DB_NAME':'',
            'DB_USER':'',
            'DB_PASS':''
        },
        'target_db':{
            'DB_TYPE':'',
            'DB_HOST':'',
            'DB_NAME':'',
            'DB_USER':'',
            'DB_PASS':''
        }
    }
}