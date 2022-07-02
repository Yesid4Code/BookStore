"""
This file has the configuration of the project.
"""

from distutils.command.config import config
from email.policy import default


class Config:
    pass


class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
