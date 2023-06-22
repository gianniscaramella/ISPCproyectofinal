
use prueba;

CREATE TABLE Leyes

(
Numero_Registro int primary key not null,
Numero_Normativa int not null,
Tipo_Normativa varchar (10) not null,
Apellidos varchar (10) not null,
Fecha int not null,
Descripcion varchar (20) not null,
Direccion varchar (20) not null,
Categoria varchar (25) not null,
Jurrisdiccion varchar (20) not null,
Organo_Legislativo varchar (35) not null,
Palabra_clave varchar (35) not null

);
