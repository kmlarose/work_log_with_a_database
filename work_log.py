import datetime

from peewee import *

db = SqliteDatabase('work_log.db')


class Entry(Model):
    """Database model for Work Log Entries"""
    worker_name = TextField()
    task_name = TextField()
    task_time = IntegerField()
    task_notes = TextField()
    created = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


def initialize():
    """Create the database and the table if they don't exist"""
    db.connect()
    db.create_tables([Entry], safe=True)


def menu_loop():
    """Show the menu"""
    menu_choice = None

    while menu_choice != 'q':
        menu_choice = input('Enter q to quit: ').lower()

# As a user of the script, I should be able to choose whether to add a new entry or lookup previous entries.
# As a user of the script, if I choose to enter a new work log, I should be able to provide my name, a task name,
# a number of minutes spent working on it, and any additional notes I want to record.

# As a user of the script, if I choose to find a previous entry, I should be presented with four options: find by employee, find by date, find by time spent, find by search term.
# As a user of the script, if finding by employee, I should be presented with a list of employees with entries and be able to choose one to see entries from.
# As a user of the script, if finding by date, I should be presented with a list of dates with entries and be able to choose one to see entries from.
# As a user of the script, if finding by time spent, I should be allowed to enter the amount of time spent on the project and then be presented with entries containing that amount of time spent.
# As a user of the script, if finding by a search term, I should be allowed to enter a string and then be presented with entries containing that string in the task name or notes.
# As a user of the script, if finding by employee, I should be allowed to enter employee name and then be presented with entries with that employee as their creator.
# As a fellow developer, I should find at least 50% of the code covered by tests. I would use coverage.py to validate this amount of coverage.
#
# Menu has a “quit” option to exit the program.
# Records can be deleted and edited, letting user change the date, task name, time spent, and/or notes.
# Can find entries based on a ranges of dates. For example between 01/01/2016 and 12/31/2016.
# If multiple employees share a name (e.g. multiple people with the first name Beth), a list of possible matches is given.
# Records are displayed one at a time with the ability to page through records (previous/next/back).
# As a fellow developer of the script, I should see test coverage of 85% of the code or better.
# NOTE:
# To get an "Exceeds Expectations" grade for this project, you'll need to complete each of the items in this section. See the rubric in the "How You'll Be Graded" tab above for details on how you'll be graded.
# If you’re shooting for the "Exceeds Expectations" grade, it is recommended that you mention so in your submission notes.
# Passing grades are final. If you try for the "Exceeds Expectations" grade, but miss an item and receive a “Meets Expectations” grade, you won’t get a second chance. Exceptions can be made for items that have been misgraded in review.

# TODO-kml: create the database

if __name__ == '__main__':
    initialize()
    menu_loop()