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
git clone https://github.com/DiegoGMuro/Python-entrega_final-Diego-Muro.git

cd Python-entrega_final-Diego-Muro

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

El presente blog es la entrega final del curso Python, donde hemos utilizado el Framework Django. En el trabajo se aplicaron los conocimientos adquiridos en el curso, entre otros: Programacion en Python, Modelo MVT de Django, Clases, Herencias, Html, Utilizacion de formularios, CRUD, aplicacion de statics, Login, logout, creacion de usuarios, utilizacion de avatars, unit tests, utilizacion de Git y Github etc.
El mismo contiene informacion sobre una empresa distribuidora de alimentos de la Republica Argentina, la cual abastece grandes cadenas de supermercados y a mayoristas.

Las aplicaciones en las que se dividio la pagina son : 

```bash
* Clientes
* Productos
* Limites de credito
* Condiciones de pago

```

Links a videos con la pagina Web funcionando : 

```bash
https://www.loom.com/share/a97256d65cfa42808bfbb5f06ba37290

https://www.loom.com/share/62263bb5804f4ebb9eb6fa954816ad73

```

La pagina posee un " acerca de mi" donde se cuenta un poco el perfil del creador de la misma como asi tambien el objeto del blog

![image](https://user-images.githubusercontent.com/113110798/200947916-8c2ca6df-3f46-4e04-9396-cc4d76e1f210.png)

La seccion de INICIO tambien tiene un buscador de CLIENTES y PRODUCTOS, como asi tambien acceso a todas las redes sociales

![image](https://user-images.githubusercontent.com/113110798/200948168-2e60906f-2ae6-4f2f-b1f2-62d24a78bd26.png)


Cada aplicacion (CLIENTES / PRODUCTOS / LIMITES DE CREDITO / CONDICIONES DE PAGO) Contiene la informacion relevante para los usuarios y en el caso de CLIENTES tambien hay fotos y una breve resena del cliente, asi como tambien una caja de comentarios para que los usuarios vayan dejando sus valoraciones sobre el mismo.

![image](https://user-images.githubusercontent.com/113110798/200948938-bb367c78-9acd-48a1-b5f1-057e05ed5e0e.png)

![image](https://user-images.githubusercontent.com/113110798/200949005-8c258b4f-4632-4d7a-b454-2f602ffad452.png)

![image](https://user-images.githubusercontent.com/113110798/200949196-45cd4d31-c0f0-4fe4-90b8-fa49b83b0651.png)

![image](https://user-images.githubusercontent.com/113110798/200949312-ba0fcc9e-2f74-465b-b33d-fe18f9df92f4.png)




Los datos (Clientes / Productos / Condiciones de pago / Limite de credito) fueron cargados por los usuarios desde los formularios de cada app asi como tambien por el administrador en el ADMIN de Django
El blog da la posibilidad de hacer un CRUD (Create - Read - Update - Delete) a los usuarios. Pero para el caso de la app CLIENTES el Update y Delete solo los usuarios que crearon los datos pueden realizarlo. La excepcion es el ADMIN que puede accionar en toda la BBDD

Los comentarios pueden ser cargados por cualquier usuario sin distincion de perfil, pero el borrado solo lo puede hacer el autor.

![image](https://user-images.githubusercontent.com/113110798/200950154-d48806f2-18c3-4e4f-b0a0-4574b4e16269.png)

El blog permite la carga de nuevos usuarios, avatars, menu de cambio de contrasenas, etc
![image](https://user-images.githubusercontent.com/113110798/200951284-afa9b548-4c1d-49eb-9f67-e8945f2de53a.png)

Ademas desde VSC se cargaron 6 casos de unit test, los cuales se encuentran en el archivo " test.py" de cada APP

![image](https://user-images.githubusercontent.com/113110798/200951600-dfc4c6d9-c75a-4f61-aa15-729920e06308.png)




