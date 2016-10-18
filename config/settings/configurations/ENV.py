""" environ settings """
import environ

BASE_DIR = environ.Path(__file__) - 4
ENV_VAR = environ.Env()
