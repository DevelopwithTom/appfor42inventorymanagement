from django.db import models
from simple_history.models import HistoricalRecords
from django.contrib.auth.models import User

# Create your models here.









class Project(models.Model):
    project_number = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    project_name = models.CharField(max_length=255, blank=False, null=True)
    project_date = models.DateTimeField(blank=True, null=True)

    project_manager = models.ForeignKey(User)


    history = HistoricalRecords()


    class Meta:
        managed = True
        db_table = 'Project'
        ordering = ['project_number']

    def __str__(self):
        return self.project_name





class Location(models.Model):
    def __str__(self):
        return "Room %s, Section %d, Shelf %s" %(self.loc_room, self.loc_section, self.loc_shelf)

    loc_room = models.CharField(max_length=20, blank=True, null=True)
    loc_section = models.IntegerField(blank=True, null=True)
    loc_shelf = models.CharField(max_length=4, blank=True, null=True)
    loc_date = models.DateTimeField(blank=True, null=True)

    #what is loc_date for? Name it after its function rather than its type
    #'loc' prefix is unncecesery

    history = HistoricalRecords()

    class Meta:
        managed = True
        db_table = 'Location'






class Box(models.Model):
    def __str__(self):
        return "Project: %s, Content: '%s', Location: %s" %(self.project_assigned_to, self.box_contents, self.Location)


    box_store_date = models.DateTimeField(blank=True, null=True)
    box_review_date = models.DateTimeField(blank=True, null=True)
    box_contents = models.CharField(max_length=300, blank=True, null=True) #May want to change this and add a 'items' class?
    box_on_loan = models.BooleanField(default=False)
    box_return_date = models.DateTimeField(blank=True, null=True)

    project_assigned_to = models.ForeignKey('Project', null=True)
    Location = models.ForeignKey('Location', null=True)

    #Whats the purpose of on loan, return date - how does this work? Are boxes assigend to another porject for this period? Return date is ecpected or actual return date?
    #Needs database normalization, remove redundancies and contradictions
    #Read about dependancies
    #Understand the processes in the company and how the database will be used
    #Change box_contents to TextField and remove 'max_length'


    history = HistoricalRecords()


    class Meta:
        managed = True
        db_table = 'Box'




class UserQueryHistory(models.Model):
    user = models.ForeignKey(User)
    query = models.CharField(max_length=300, blank=True, null=True)
    date_searched = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'User_Query_History'

    def __str__(self):
        return "User: %s, Query: '%s', Date: %s" %(self.user, self.query, self.date_searched)
