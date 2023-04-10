# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-jj^97-9v!_o+=5p!2cuabhnt=#2t@gr68qa(r5ehmm#*h6^nc!'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        # 'ENGINE': 'django.db.backends.mysql',
        'NAME': 'real_estate_capstone_db',
        'HOST': 'capstone-app-database',
        'USER': 'root',
        'PASSWORD': 'password',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}