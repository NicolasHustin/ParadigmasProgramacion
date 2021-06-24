%HECHOS
empleado(6052401).

%es_nombre_de(x,z), donde x es el nombre de la persona y z es la cedula
es_nombre_de(Nicolas, 6052401). 
%es_apellido_de(x,z), donde x es el apellido de la persona y z la cedula
es_apellido_de(Hustin, 6052401).
%es_sueldo_de(x,z), donde x es el sueldo del empleado y z es la cedula
es_sueldo_de(15000000, 6052401).

%REGLAS
son_datos_empleado(Nombre,Apellido,Direccion,Telefono,Sueldo)
    es_nombre_de(Nombre, cedula).
    es_apellido_de(Apellido, cedula).
    es_direccion_de(Direccion, cedula).
    es_telefono_de(Telefono, cedula).
    es_sueldo_de(Sueldo, cedula).

