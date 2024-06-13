### Welcome to the repository for Task 26 "Django - Sticky Notes Application Part 2"!

This task required building a "sticky notes" app using the Django framework, making use of (and therefore understanding) its Model-View-Template (MVT) design pattern.

The app can be run through any web browser and includes the following functionality:
- Create "sticky note" records with the attributes Title, Content, Author and Colour
- View the full list of all "sticky note" records, each with a background colour based on the Colour attribute specified
- View individual "sticky note" records, with additional meta data such as the date and time created
- Click on any Author or Colour value to see a filtered list of all records by that Author or with that Colour
- Update and Delete individual "sticky note" records

The app has been built to take advantage of many benefits of the Django framewrok, such as:
- Object-relational mapping - make SQL migrations automatically, based on model classes and attributes defined, and apply these to an SQLite3 database file
- Model forms - create HTML user input forms automatically, based on a specified model class and the attributes defined for inclusion
- Render HTML pages with underlying logic written in Python, using the built-in interactions between the views, urls and template files

The app was developed within a virtual environment using using venv, and pushed to this remote repository using git. The following packages need to be installed:

Package  Version
asgiref  3.8.1
Django   5.0.6
pip      24.0
sqlparse 0.5.0
tzdata   2024.1

Finally, it includes unit tests than can be run automatically using the test function from manage.py, plus superuser admin permissions via the Django admin site.
