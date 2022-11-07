# Entrega_final-Diego-Muro    CoderHouse2022 - Curso Python Comision 43765

# Instrucciones para ejecutar este proyecto:

- Crear Directorio del proyecto
### 1. Abrir Git Bash para `Windows` o una terminal para `Linux/Unix`.

### 2. Crear directorio de trabajo para el proyecto del curso 
```bash
cd
mkdir -p Entrega_Final/coder_projects
cd Entrega_final/coder_projects
ls 
```

- Clonar el proyecto
```bash
git clone https://github.com/DiegoGMuro/entrega_final-Diego-Muro.git

cd entrega_final-Diego-Muro

```


### 3. Crear y activar entorno virtual
(Windows)
```bash
python -m venv venv
.\venv\Scripts\activate
```

(Linux)
```bash
python3 -m venv venv
source venv/bin/activate
```
### 4. Instalar las dependencias del proyecto
```bash
pip install -r requirements.txt
```

### 5. Navegamos hacia la carpeta del proyecto `tp_final'
```bash
cd tp_final
```
### 6. Se crean las migraciones que son una "plantilla" para crear la base de datos con la que trabajará nuestro proyecto de Django
```bash
python manage.py makemigrations
```
### 7. Se ejecuta la migración para crear la base de datos con la que trabajará nuestro proyecto de Django
```bash
python manage.py migrate
```
### 8. Se crea el super usuario para nuestro proyecto de Django, **Solo si no se ha creado**
```bash
python manage.py createsuperuser
```
```bash
Ingrese `Username`, `Email address` y `Password` 
```
### 9. Se levanta el servidor de Django que expone el servicio por el localhost en el puerto 8000 por defecto `http://127.0.0.1:8000/`
```bash
python manage.py runserver
```

# Descripcion del proyecto

El presente blog brinda informacion de una empresa de Distribuidora de alimentos que provee a cadenas grandes y medianas de supermercados, asi como mayoristas y almacenes de barrio.

Las aplicaciones en las que se dividio la pagina son : 

```bash
* Clientes
* Productos
* Limites de credito
* Condiciones de pago

```

La seccion de HOME tiene el buscador de CLIENTES y PRODUCTOS

![2022-11-06 01 05 56](https://user-images.githubusercontent.com/113110798/200153769-20319121-ef5e-4db9-bdcf-943651c8e2c6.jpg)


Cada aplicacion (CLIENTES / PRODUCTOS / LIMITES DE CREDITO / CONDICIONES DE PAGO) Contiene la informacion de cada aplicacion

![image](https://user-images.githubusercontent.com/113110798/200153845-044eff32-3039-4c70-b4f5-83e9effb48be.png)

![image](https://user-images.githubusercontent.com/113110798/200153871-77a8d59e-4c78-48c9-998f-d007a7a9caf0.png)



La misma fue cargada a la BD tanto por los formularios de la pagina como por el menu ADMIN de Django

![image](https://user-images.githubusercontent.com/113110798/200153899-0be3c4a2-9e8c-4a02-b714-a184d04272fc.png)


![image](https://user-images.githubusercontent.com/113110798/198755229-0bf2e7e7-99e7-4f76-844a-c14baf9adcf9.png)

Se recomienda hacer 5 tipos de prueba

```bash
* Buscar algun cliente por el buscador
* Ingresar informacion a la BBDD en alguna de las APPs desde los formularios
* Ingresar informacion a la BBDD desde el menu ADMIN de Django
* Chequear con SQLITE desde VSC alguna de las bases de datos
```
![image](https://user-images.githubusercontent.com/113110798/198755341-6c2bb461-bbfb-4685-bbb5-3f50697bd41f.png)

```bash
* Chequear con SQLITE las bases de datos 
```
![image](https://user-images.githubusercontent.com/113110798/198755394-32c46154-c832-4f9d-a006-1c1cf14f31cf.png)
