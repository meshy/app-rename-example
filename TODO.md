# Rename app from shop to catalogue

Steps:

- [ ] Prepare existing setup for move:
  - [ ] Create an app config (set `name` and `label` to defaults).
  - [ ] Add the app config to `INSTALLED_APPS`.
  - [ ] On all models, explicitly set `db_table` to the current value.
  - [ ] Doctor migrations so that `db_table` was "always" explicitly defined.
  - [ ] Ensure no migrations are required (checks previous step).
- [ ] Change app label:
  - [ ] Set `label` in app config to new value (catalogue).
  - [ ] Update migrations and foreign keys to reference new app label.
  - [ ] Run custom SQL to fix migrations and `content_types` app.
    ```sql
    UPDATE django_migrations
       SET app = 'catalogue'
     WHERE app = 'shop';

    UPDATE django_content_type
       SET app_label = 'catalogue'
     WHERE app_label = 'shop';
    ```
  - [ ] Ensure no migrations are required (checks previous step).
- [ ] Rename tables:
  - [ ] Remove "custom" `db_table`.
  - [ ] Run `makemigrations` so django can rename the table "to the default".
- [ ] Move the files:
  - [ ] Rename module directory.
  - [ ] Fix imports.
  - [ ] Update app config's `name`.
  - [ ] Update where `INSTALLED_APPS` references the app config.
- [ ] Tidy up:
  - [ ] Remove custom app config if it's no longer required.
  - [ ] If app config gone, don't forget to also remove it from `INSTALLED_APPS`.