
use prueba;

CREATE TABLE Leyes

(
Numero_Registro int primary key not null,
Numero_Normativa int not null,
Tipo_Normativa varchar (12) not null,
Fecha int not null,
Descripcion varchar (320) not null,
Categoria varchar (30) not null,
Jurisdiccion varchar (10) not null,
Organo_Legislativo varchar (35) not null,
Palabra_clave varchar (65) not null

);
