

**Un contenedor es una partición aislada (donde se ejecutan procesos) dentro de un sistema operativo. Son similares a las máquinas virtuales en cuestiones de seguridad pero requieren menos requisitos de hw puesto que comparten parte del sistema operativo donde se ejecutan.**

**Los contenedores se definen a partir de imágenes.**

**Docker es un software q que gestiona contenedores de aplicación. Una imagen de Docker es una especie de “Sistema Operativo con aplicaciones instaladas”. Es una virtualización ligera porque los recursos se comparten entre los contenedores.**

**Cada contenedor ejecuta un sólo proceso. Es una instancia de una imagen.**

**Dockerhub es un repositorio de imágenes.**

**Componentes de Docker: Docker Engine (gestiona imágenes y contenedores) + Docker Client (gestiona Docker Engine) + Docker Registry (registra las imágenes creadas con Docker Engine, permite distribuirlas como por ejemplo Dockerhub).**

**Fichero Dockerfile contiene las instrucciones que se deben ejecutar para a partir de un sistema operativo, descargar e instalar los paquetes necesarios para crear la imagen a partir de la que ejecutaremos el contenedor. Facilita la creación y ejecución del contenedor.**

**([https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop) )**

**Ciclo de vida del contenedor:**

**crear aplicación →  crear imagen →  crear contenedor →  lanzar contenedor y distribuir a través de un registro como Dockerhub**

**Instalación:**

**sudo apt-get install docker.io**

**Paso 1: CREAR UN DOCKER CON UNA IMAGEN DE DOCKER**

**docker pull nombreImg
docker run -p 27017:27017 nombreImg--> 27017:27107 es el puerto

-d->el contenedor se ejecuta en 2ºplano
-p->concetar puerto entre el SO y el contenedor

**Para conocer los contenedores que tenemos instanciados: docker ps
Lo que sale en la terminal:
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                      NAMES
56d85a29720b        bitnami/mongodb     "/entrypoint.sh /run…"   2 minutes ago       Up 2 minutes        0.0.0.0:27017->27017/tcp   hardcore_bouman
Para conocer las imágenes descargadas: docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
bitnami/mongodb     latest              9330a1a34eb1        10 hours ago        372MB
hello-world         latest              fce289e99eb9        8 months ago        1.84kB**

TAG es la versión de la img-->se especifica en el pull-->si NO, por defecto es latest
**Management Commands:(docker + comando)
•   builder     Manage builds
•   config      Manage Docker configs
•   container   Manage containers
•   context     Manage contexts
•   engine      Manage the docker engine
•   image       Manage images
•   network     Manage networks
•   node        Manage Swarm nodes
•   plugin      Manage plugins
•   secret      Manage Docker secrets
•   service     Manage services
•   stack       Manage Docker stacks
•   swarm       Manage Swarm
•   system      Manage Docker
•   trust       Manage trust on Docker images-->similar a inspect
•   volume      Manage volumes
Commands:
•   attach      Attach local standard input, output, and error streams to a running container
•   build       Build an image from a Dockerfile
•   commit      Crear img a partir de los cambios de un contenedor
•   cp          Copy files/folders between a container and the local filesystem
•   create      Create a new container
•   diff        Muestra los cambios hechos en un contenedor desde que se ejecutó la última vez
•   events      Get real time events from the server
•   exec        Run a command in a running container
•   export      Export a container's filesystem as a tar archive
•   history     Show the history of an image
•   images      List images
•   import      Import the contents from a tarball to create a filesystem image
•   info        Display system-wide information
•   inspect     info sobre las img/Obj Docker
•   kill        matar procesos del contenedor
•   load        Load an image from a tar archive or STDIN
•   login       Log in to a Docker registry
•   logout      Log out from a Docker registry
•   logs        Fetch the logs of a container
•   pause       Pause all processes within one or more containers
•   port        List port mappings or a specific mapping for the container
•   ps          List containers
•   pull       add/descargar/traer img o repositorios
•   push        lanzar img o repositorio
•   rename      Rename a container
•   restart     Restart one or more containers
•   rm          Remove one or more containers
•   rmi         Remove one or more images
•   run         Run a command in a new container
•   save        Save one or more images to a tar archive (streamed to STDOUT by default)
•   search      Search the Docker Hub for images
•   start       Start one or more stopped containers
•   stats       Display a live stream of container(s) resource usage statistics
•   stop        Stop one or more running containers
•   tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
•   top         Display the running processes of a container
•   unpause     Unpause all processes within one or more containers
•   update      Update configuration of one or more containers
•   version     Show the Docker version information
•   wait        Block until one or more containers stop, then print their exit codes
Run 'docker COMMAND --help' for more information on a command.**

rm—>contenedor

rmi—>imagen