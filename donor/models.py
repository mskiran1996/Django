from django.db import models
from datetime import *
from django.contrib.contenttypes.models import ContentType

PROFILE_TYPES = (('Individual', 'Individual'), ('Organisation', 'Organisation'))

MASTER_TYPES = (('Title', 'Title'), ('Contact Source', 'Contact Source'), \
                ('Preference For Communication', 'Preference For Communication'), \
                ('Contact Type', 'Contact Type'),('Programme Preference', 'Programme Preference'), \
                ('Tax Exemption', 'Tax Exemption'), ('Gift', 'Gift'),\
                ('Mode of Engagement','Mode of Engagement')
                )

GENDER_TYPES = (('Male', 'Male'), ('Female', 'Female'))

COMMUNICATION_CATEGORIES = (('Primary', 'Primary'), ('Secondary', 'Secondary'))

class Base(models.Model):
    active = models.IntegerField(default = 2)
    created_on=models.DateTimeField('Created_on',default = datetime.now())
    modified_on=models.DateTimeField('Modified_on',auto_now = True)

    class Meta:
        abstract = True


class Master_Data(Base):
    master_type = models.CharField(max_length=100, choices = MASTER_TYPES)
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return "%s - %s" %(self.master_type, self.name)


class Profile(Base):
    profile_type = models.ForeignKey(Master_Data, related_name = "profile_type")
    prefix = models.ForeignKey(Master_Data, blank=True, null=True, related_name = "prefix")
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    contact_source = models.ManyToManyField(Master_Data, blank=True, null=True, related_name = "contact_source")
    contact_type = models.ForeignKey(Master_Data, blank=True, null=True, related_name = "contact_type")
    gender = models.CharField(max_length=100, blank = True, null = True, choices = GENDER_TYPES)
    dob = models.DateField(blank = True, null = True)
    pan_number = models.CharField(max_length=100, blank=True, null=True)
    program_preference = models.ManyToManyField(Master_Data, blank=True, null=True, related_name = "program_preference")
    keywords = models.ManyToManyField(Master_Data, blank=True, null=True, related_name = "keywords")

    def __unicode__(self):
        return "%s - %s" %(self.profile_type.name, self.first_name)


class Communication(Base):
    communication_perference = models.ForeignKey(Master_Data, related_name = "communication_perference")
    communication_detail = models.CharField(max_length=100, blank=True, null=True)
    default = models.BooleanField(default = True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()

    def __unicode__(self):
        return "%s - %s" %(self.communication_perference.name, self.communication_detail)

