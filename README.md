# BackEnd_LQN

### Instrucciones

Los paquetes de python instalados se encuentran en el archivo requirements.txt, direccion web por defecto	[http://127.0.0.1:8000/](http://127.0.0.1:8000/), direccion de admin [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin).

Datos de inicio de sesion para cuenta de admin
- Usuario: root
- Contraseña: toor

### Modelo de la base de datos
Clase para almacenar los personajes
```
class  Personaje(models.Model):
nombre = models.CharField(max_length=120)
	class  Meta:
		ordering =  ('nombre',)
	def  __str__(self):
		return self.nombre
```
Clase para almacenar los planetas
```
class  Planeta(models.Model):
	nombre = models.CharField(max_length=120)
	class  Meta:
		ordering =  ('nombre',)
	def  __str__(self):
		return self.nombre
```
Clase para almacenar las películas
```
class  Pelicula(models.Model):
	titulo = models.CharField(max_length=120)
	texto_apertura = models.TextField()
	director = models.CharField(max_length=120)
	productores = models.CharField(max_length=120)
	personaje = models.ManyToManyField(Personaje)
	planeta = models.ManyToManyField(Planeta)
	class  Meta:
		ordering =  ('titulo',)
	def  __str__(self):
		return self.titulo
```
### Query de ejemplo

Estas se pueden realizar en la direccion [http://127.0.0.1:8000/graphql](http://127.0.0.1:8000/graphql)

Listar todos los personajes
```
query {
  allPersonajes{
    edges{
      node{
       nombre
        peliculaSet{
          edges{
            node{
              titulo
              textoApertura
              director
              productores
              planeta {
                edges {
                  node {
                   	nombre
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
```
Listar todos las peliculas en las que aparece **Anakin Skywalker**
```
query {
  allPersonajes(nombre_Icontains: "Anakin Skywalker"){
    edges{
      node{
       nombre
        peliculaSet{
          edges{
            node{
              titulo
              textoApertura
              director
              productores
              planeta {
                edges {
                  node {
                   	nombre
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
```
