import os

ENVIRONMENT_NAME = os.environ.get('LASER_TAG_ENV', 'development')


def is_production():
    return ENVIRONMENT_NAME == 'production'


def is_development():
    return ENVIRONMENT_NAME == 'development'
