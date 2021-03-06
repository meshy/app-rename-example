# Rename app from shop to catalogue

This repo shows how you can rename a django app.

Read through the commits to see how the following steps were completed.

Steps:

- [x] Prepare existing setup for move:
  - [x] Create an app config (set `name` and `label` to defaults).
  - [x] Add the app config to `INSTALLED_APPS`.
  - [x] On all models, explicitly set `db_table` to the current value.
  - [x] Doctor migrations so that `db_table` was "always" explicitly defined.
  - [x] Ensure no migrations are required (checks previous step).
- [x] Change app label:
  - [x] Set `label` in app config to new value (catalogue).
  - [x] Update migrations and foreign keys to reference new app label.
  - [x] Run custom SQL to fix migrations and `content_types` app.
    ```sql
    UPDATE django_migrations
       SET app = 'catalogue'
     WHERE app = 'shop';

    UPDATE django_content_type
       SET app_label = 'catalogue'
     WHERE app_label = 'shop';
    ```
  - [x] Ensure no migrations are required (checks previous step).
- [x] Rename tables:
  - [x] Remove "custom" `db_table`.
  - [x] Run `makemigrations` so django can rename the table "to the default".
- [x] Move the files:
  - [x] Rename module directory.
  - [x] Fix imports.
  - [x] Update app config's `name`.
  - [x] Update where `INSTALLED_APPS` references the app config.
- [x] Tidy up:
  - [x] Remove custom app config if it's no longer required.
  - [x] If app config gone, don't forget to also remove it from `INSTALLED_APPS`.
