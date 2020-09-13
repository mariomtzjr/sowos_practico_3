# sowos_practico_3

## Requerimientos
- Docker v19.03.12
- Django==2.2.1
- redis==2.10.3
- gunicorn
- djangorestframework
- psycopg2-binary

## Set up
1. Clonar el repositorio
2. En la terminal ejecutamos `cd sowos_practico_3/ecommerce_project`
3. Ejecutar `docker-compose exec web python manage.py collectstatic --no-input --clear`
3. Ejecutamos el comando `docker-compose build`
4. Ejecutamos el comando `docker-compose up`

## Creación de super usuario
Para crear un super usuario y podemos ingresar al sitio de administración de la aplicación, abrimos otra ventana de terminal y nos situamos dentro del directorio *sowos_practico_3/ecommerce_project*. Estando en este directorio ejecutamos el comando:  
`docker-compose exec web python manage.py createsuperuser`  
Seguir instrucciones.

## Sitio de administración
- URL: http://localhost:1337/admin

## Endpoints
- /persons/
- /customers/
- /purchases/
- /products/
- /purchase-products/
- /categories/

Cada uno de los endpoint listados tiene las siguientes funcionalidades
- crear/
- listar/
- editar/id
- eliminar/id

El parámetro *id* corresponde al id del endpoint donde se encuentre, por ejemplo, si el endpoint es *http://localhost:1337/persons/editar/1*, la funcionalidad es la de editar la persona con el *identificador igual a 1* o bien, *http://localhost:1337/products/eliminar/3*, la funcionalidad es la de eliminar el producto con el *identificador igual a 3*.
