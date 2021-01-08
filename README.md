# Django CRUD


[Repository Link](https://github.com/randalsallaq/django-crud)

Live [URL](https://randalsallaq.github.io/django-crud/)

## Lab: 28
## Feature Tasks and Requirements:

- Create BlogListView that extends appropriate generic view
associated url path is an `empty string`
- Create BlogDetailView that extends appropriate generic view
 associated url path is `post/<int:pk>/`
- Create BlogCreateView that extends appropriate generic view
 associated url path is `post/new/`
- Create BlogUpdateView that extends appropriate generic view
associated url path is `post/<int:pk>/edit/`
- Create BlogDeleteView that extends appropriate generic view
associated url path is `post/<int:pk>/delete/`


## Implementation:

- projected and app were created.
- A Model was created to view the `Sample` table in the Admin panel.
- Post objects were added:
    1. the idiot Review.
    2. The Picture of Dorian Gray Review
    3. Crime and Punishment Review.
- Templates were created to render the data; 
    * home template for titles.
    * details template for titles and the body of the blog.

#### For `CRUD`:
- Form method : `POST`
- Templates :
1. `create.html`
2. `update.html`
3. `delete.html`
