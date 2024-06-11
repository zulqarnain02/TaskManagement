from django.db import models

class Task(models.Model):
    taskid = models.AutoField(db_column='TaskID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=100, blank=True, null=True)
    assignto = models.CharField(db_column='AssignTo', max_length=40, blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
    duedate = models.DateField(db_column='dueDate', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=9, blank=True, null=True)
    description = models.CharField(db_column='Description', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'task'  # Use the existing table name
