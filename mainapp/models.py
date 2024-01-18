from django.db import models

class SiteSection(models.Model):
    name = models.CharField(max_length=255)
    url_name = models.CharField(max_length=255)
    url_path = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class StatisticContent(models.Model):
    name = models.CharField(max_length=255)
    html_table_path = models.FileField(upload_to='html_tables')
    graph_image_path = models.FileField(upload_to='graph_images')

    def __str__(self):
        return self.name


class Section(models.Model):
    content = models.ForeignKey(StatisticContent, on_delete=models.CASCADE)
    site_section = models.ForeignKey(SiteSection, on_delete=models.CASCADE)

    def __str__(self):
        return self.site_section.name + " " + self.content.name
