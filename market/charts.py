from django_google_charts import charts
from .models import transactions

class StepChart(charts.Chart):
    chart_slug = 'steps_chart'
    columns = (
        ('datetime', "timestamp"),
        ('number', "Stockprice"),
    )

    def get_data(self):
	value=transactions.objects.values_list('timestamp', 'stockprice')
	print value
        return value
