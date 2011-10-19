YOUR FIRST MIGRATION

1.create a new app and create your initial ‘models.py’ file for it
2. add your app to your project’s INSTALLED_APPS
3. run ‘./manage.py schemamigration main --initial’      (creates your
initial migration, note: those are two dashes hyphens before initial)
4. run ‘python manage.py migrate myapp’     (uses this initial migration to create
your app’s DB tables)



MIGRATING A CHANGED MODEL

1. modify your app’s models.py file    (e.g., add a new column somewhere)
2. run ‘python manage.py schemamigration myapp –auto’    (creates a new migration,
note: those are two dashes hyphens before auto)
3. run ‘python manage.py migrate myapp’    (applies this new migration)
