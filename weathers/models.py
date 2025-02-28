from django.db import models


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField("date published")
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)


class City(BaseModel):
    name = models.CharField(max_length=50, default='', blank=True, unique=True)
    country = models.CharField(default='Lietuva', max_length=100)
    coordination_x = models.FloatField(default=0)
    coordination_y = models.FloatField(default=0)

    def __str__(self):
        return f'{self.name} in {self.country}, coordination: {self.coordination_x, self.coordination_y}'

"""
Naujas modelis Weather
id	tipas	data	
	saule		sunny, cloudy, rainy
	temperatura		
	wind		
	dregme		
"""
