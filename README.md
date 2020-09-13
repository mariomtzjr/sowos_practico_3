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
3. Ejecutamos el comando `docker-compose build`
4. Ejecutamos el comando `docker-compose up`
En una nueva terminal ejecutamos el siguiente comando:  
`docker-compose exec web python manage.py collectstatic --no-input --clear`  

## Creación de super usuario
Para crear un super usuario y poder ingresar al sitio de administración de la aplicación, abrimos otra ventana de terminal y nos situamos dentro del directorio *sowos_practico_3/ecommerce_project*. Estando en este directorio ejecutamos el comando:  
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

El parámetro *id* corresponde al id del objeto dentro del endpoint en cuestión, por ejemplo, si el endpoint es *http://localhost:1337/persons/editar/1*, la funcionalidad es la de editar la persona con el *identificador igual a 1* o bien, *http://localhost:1337/products/eliminar/3*, la funcionalidad es la de eliminar el producto con el *identificador igual a 3*.

## Base de datos de prueba
Dentro del repositorio, en la ruta *sowos_practico_3/ecommerce_project/var/database/*, se encuentra un archivo llamado *database.sql*, la cual tiene algunos dato de prueba, los cuales son:

#### Super usuario
- admin con password: `admin123`

#### Users:
- Francisco Martínez Jr con uuid 7a03befc-686f-47c5-b8a0-fa57da073c56
- Juan Gutierrez con uuid a641a489-c011-4e65-a5c0-b48aa11a1896
- Mario Martinez con uuid bdb5a4e5-2b7d-4d88-9296-236055f11c33

### Tokens
- 08f9c9ddf9626dc81e6ce3a94867ac614061406b para superuser admin
- 5b0876ac868f03a4f16cc151f6d2caff8926ae24 para Juan Gutierrez
- 70a434dcc91b123f4a57f59f24be0e848093794a para Mario Martinez
- 18745c571912c0f88f7fb9e532e666a79c795440 para Francisco Martinez Jr

## Postman Collection
Adicionalmente a la base de datos de prueba, el proyecto tiene una colección de postman con los requests básicos (POST, GET, PUT, DELETE) de cada endpoint existente, esta colección se encuentra en la ruta *sowos_practico_3/ecommerce_project/var/postman/*. Para descargar postman, será necesario ingrear a su [página oficial](https://www.postman.com/), crear una cuenta y [descargar postman desktop](https://www.postman.com/downloads/).

## Test de Tokens
Para probar la funcionalidad de autenticación por token, podemos emplear el siguiente comando desde una terminal o línea de comandos:  
`curl -X GET http://127.0.0.1:1337/api/persons/listar/ -H 'Authorization: Token 08f9c9ddf9626dc81e6ce3a94867ac614061406b'`  
La salida del comando anterior será como la siguiente:  
`{"persons":[{"id":2,"name":"Mario","last_name":"Martinez"},{"id":3,"name":"Juan","last_name":"Gutierrez"},{"id":9,"name":"Francisco","last_name":"Martinez V"}]}`  
Esta salida, aplicando un poco de estilo visual se vería de la siguiente forma:  
```
{
    "persons":[
        {
            "id":2,
            "name":"Mario",
            "last_name":"Martinez"
        },
        {
            "id":3,
            "name":"Juan",
            "last_name":"Gutierrez"
        },
        {
            "id":9,
            "name":"Francisco",
            "last_name":"Martinez V"
        }
    ]
}
```  
Las personas listadas son las que se encuentran en la base de datos. Si por el contrario, no enviamos el token en el encabezado de la petición, obtendremos una respuesta como la siguiente:  
comando: `curl -X GET http://127.0.0.1:1337/api/persons/listar/`  
salida:  
```
{
    "detail":"Authentication credentials were not provided."
}
```
Y cuyo estatus en la petición es un 401. Unauthorized.

Para realizar las pruebas desde Postman, será necesario cambiar el valor del token que viene en el value del key "Authorization", por "Token <alguno_de_los_tokens_existentes>" en el Headers de la petición.
