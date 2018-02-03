from django.db.migrations.recorder import MigrationRecorder


def get_color(migration_name):
    if is_migration_applied(migration_name):
        return "blue"
    return "green"


def is_migration_applied(migration_name):
    return MigrationRecorder.Migration.objects.filter(
        name__exact=migration_name).exists()
