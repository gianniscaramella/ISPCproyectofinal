
use prueba;

CREATE TABLE Leyes

(
Numero_Registro int primary key not null,
Numero_Normativa int not null,
Tipo_Normativa varchar (10) not null,
Apellidos varchar (35) not null,
Fecha int not null,
Descripcion varchar (40),
Direccion varchar (50),
Categoria varchar (35) not null,
Jurrisdiccion varchar (35) not null,
Organo_Legislativo varchar (35) not null,
Palabra_clave varchar (35) not null

);