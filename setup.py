from setuptools import setup

setup(
    name="mi_paquete",
    version="1.0",
    description="Lorem",
    author= "Christian Coria",
    author_email= "desbloqueoenlinea@gmail.com",
    packages=["calculadora"]
)

#en terminal hay que correr: py setup.py sdist    ( asi se genera un instalador) 

#luego pip o pip3   salta una ayuda     .pip install dist/mi_paquete-1.1.tar.gz 
#  (osea la direccion y asi se instala para tener acceso desde cualquier carpata de python)