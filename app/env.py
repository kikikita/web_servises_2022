from os import environ
from alembic import context
from app.models import posts, users

# Alembic Config объект предоставляет доступ
# к переменным из файла alembic.ini
config = context.config

section = config.config_ini_section
config.set_section_option(section, "DB_USER", environ.get("DB_USER"))
config.set_section_option(section, "DB_PASS", environ.get("DB_PASS"))
config.set_section_option(section, "DB_NAME", environ.get("DB_NAME"))
config.set_section_option(section, "DB_HOST", environ.get("DB_HOST"))

fileConfig(config.config_file_name)

target_metadata = [users.metadata, posts.metadata]