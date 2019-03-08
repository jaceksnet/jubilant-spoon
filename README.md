# Adjust home task

I've used Django and Django Rest Framework for this exercise.

After installing requirements from ```requirements.txt``` file,
run ```./manage.py migrate``` 
and load sample data through ```./manage.py load_sample_data```
run development server by ```./manage.py runserver```

## 1 filter by time range

to filter by date, use date_to, date_from request parameters with date in 'yyyy-mm-dd' format

## 2 group by

to group by use ```group_by``` request parameter, use it multiple times to group by several fields

## 3 sorting

to sort by field, use ```order_by``` request parameter, 
to sort in descending order use "-" sign before the name of the field you want to sort by


## example requests

GET /metrics/?date_to=2017-06-01&group_by=channel&group_by=country&order_by=-clicks

GET /metrics/?date_to=2017-06-01&date_from=2017-05-01&group_by=date&order_by=date

GET /metrics/?date_to=2017-06-01&date_from=2017-06-01&group_by=os&order_by=-revenue