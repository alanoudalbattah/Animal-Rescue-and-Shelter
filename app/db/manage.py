
#! Flask-Migrate does not support Flask-Script any more.
# https://github.com/miguelgrinberg/Flask-Migrate/issues/407


# from flask_script import Manager
# from flask_migrate import Migrate, MigrateCommand
# from app import app
# from models import db

# migrate = Migrate(app, db)
# manager = Manager(app)
# manager.add_command('db', MigrateCommand)

# if __name__ == '__main__':
#     manager.run()


# ? HOW TO USE MIGRATION in the cmd line <<< NOTE TO MY SELF :) >>>
#--> use [ flask db init ] to create a migration
#--> use [ flask db migrate ] to sync models
#--> use [ flask db upgrade ] and [ flask db downgrade ] to upgrade & downgrade versions of migrations