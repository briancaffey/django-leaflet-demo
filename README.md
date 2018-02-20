## Todo

Filter data
Q lookups 
Export data buttons
User pages
Author model?
Categories?
DRF?
Admin pages?
Record approval?

## About 

This project shows how to use Leaflet maps in a Django project. 

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

