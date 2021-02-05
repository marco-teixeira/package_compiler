[Read this page in English]()

Descrição 
=================================

 

Este pacote tem por finalidade copiar um pacote ROS para um destino definido pelo usuário. Os códigos em python do pacote são compilados para o formato “pyc”. O objetivo é ocultar o código do pacote, quando for desejado pelo desenvolvedor.  

 

Configuração do sistema utilizado 
--------------------------------

* Ubuntu 18.04.4 (http://releases.ubuntu.com/18.04.4/) 
* ROS Melodic (http://wiki.ros.org/melodic/Installation/Ubuntu) 


 
Parâmetros:
----------------------------------
1. **pkg_name**
   - Tipo: String
   - Valor padrão: "package_compiler"
   - Descrição: Nome do pacote existente no seu src, a ser compilado e movido. Por padrão, está o nome deste pacote. 

2. **dir_dest**
   - Tipo: String
   - Valor padrão: ""
   - Descrição: Local de destino a ser instalado o pacote compilado. Deve ser informado o caminho completo! Caso não seja informado nenhum caminho, será colocado em uma pasta de nome "compiled" dentro do pacote, no src. 



Instalando:
--------------------------------
```
$ cd ~/catkin_ws/src/
$ git https://github.com/marco-teixeira/package_compiler.git
$ cd ~/catkin_ws
$ catkin_make
```


Executando: 
-------------------------------

```
rosrun package_compiler compile.py _pkg_name:="" _dir_dest:=""
roslaunch package_compiler compile_python_pkg.launch
```







