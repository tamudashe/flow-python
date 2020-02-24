from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
class  Post(models.Model):
    """
    Networking events posts
        - company: name of the company offering the internship
        - title: internship title
        - location: list of locations offering the internships
        - classification: internship targeted classification
        - deadline: time by which the application should be submited
        - application_link: allows linking to the applications on the company websites

    """
    YEAR_IN_SCHOOL_CHOICES = [
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('GR', 'Graduate'),
    ]
    CAREER_FIELDS = [
        ('Technology', 'technology'),
        ('Business', 'business'),
        ('General', 'general')
    ]

    LOCATION_STATES = (('AL', 'Alabama'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'))

    # table columns
    company_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    industry = models.CharField(max_length=200, choices=CAREER_FIELDS)
    location = models.CharField(max_length=50, choices=LOCATION_STATES)
    classification = MultiSelectField(choices=YEAR_IN_SCHOOL_CHOICES)
    deadline = models.DateField()
    application_link = models.URLField()

    def __str__(self):
        return self.title
