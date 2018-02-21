## Todo

- Filter data ✓
- Q lookups ✓
- Export data buttons
- User pages 
- Author model
- Categories
- DRF
- Admin pages
- Record approval
- PEP8 ✓

## About 

This project shows how to use Leaflet maps in a Django project. I use a simple `Book` model to illustrate different model fields and how they can be used across different parts of Django, such as views, forms, urls and templates. I will also be using additional models such as `Author`, `Publisher` and `Like` to illustrate various types of relations and how they can work together. 

### Map Data

The main goal of this project is to show how to plot items with geographical coordinates on a map using custom markers. Plotted items display additional information when clicked.

### Data Filtering

Django forms is used to make a form that users can use to filter records. Filter options include:

- Keywords contained in the title, synopsis or website. This uses Django's Q lookups
- Date filtering using `bootstrap-datepicker` plugin

Filtered records then show up on the map. Form options are persisted with the option to be quickly changed or completely reset. Summary statistics of the filtered data are also displayed. 

### DataTables

DataTables is used for tabular display of data. This allows for easy sorting and further search and filtering of the data. 

### Exporting Data

Data can be exported into a number of formats including XLS, CSV or PDF. 

### Adding Records

I use Django ModelForms to build a form that allows users to add records. Geographical coordinate data can be added directly to the form and the cooresponding map marker is updated immediately. Also, when the map in the form is clicked, the form coordinate inputs are updated with values of the clicked location's coordinates. 

### Using Q Lookups to for searching multiple fields by mulitple keywords

[idiom for searching multiple keywords](https://stackoverflow.com/questions/35126136/filter-multiple-keywords)

```python
def all_books(request):
    """
    Main view for books. request.GET parameters are used to filter books
    """
    books = Book.objects.all()
    form = QueryForm(request.GET or None)
    paramDict = request.GET
    params = paramDict.keys()
    
    # data filtering
    if any(x!='' for x in request.GET.values()):

        [...other filters...]

        # this code returns records that contain all of the keywords
        if paramDict['keywords']:
            keywords = paramDict['keywords'].split()
            for kw in keywords:
                books = books.filter(
                    Q(title__icontains=kw)
                )

        # filters records that contain any of the following keywords
        if paramDict['keywords'] != '':
            kws = paramDict['keywords'].split()
            q_lookups = [Q(title__icontains=kw) for kw in kws] + \
                        [Q(synopsis__icontains=kw) for kw in kws] + \
                        [Q(website__icontains=kw) for kw in kws]
            filters = Q()
            filters |= reduce(lambda x, y: x | y, q_lookups)
            books = books.filter(filters)
[...]
```

## Inline Radio Buttons




```html
{% for choice in form.status_ %}
    {{ choice.choice_label }}
    <span class="checkbox-inline">{{ choice.tag }}</span>
{% endfor %}
```

### AJAX Map Load 

```javascript
$.ajax({
    type: "GET",
    url: "/books/map_data",
    success: function(data){
        var books = data["data"]
        var new_lat = books[0].loc[0]
        var new_lon = books[0].loc[1]
        mymap.setView([0, 0], 2);
        populateMap(books)
    }
    });
```

