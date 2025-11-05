"""
ARCHIVO DE CONFIGURACIÓN DE BASE DE DATOS
==========================================
Este es el ÚNICO archivo que necesitas modificar para conectar a tu base de datos.
Cambia los valores a continuación con las credenciales de tu base de datos PostgreSQL.

IMPORTANTE: 
- Para Render, usa el FQDN completo (ej: dpg-xxxxx.render.com)
- Para localhost, usa: 'localhost'
- NO subas este archivo a GitHub (está en .gitignore)
"""

# Configuración de conexión a PostgreSQL
PGHOST = 'dpg-d4401tuuk2gs739ibgc0-a.virginia-postgres.render.com'  # Host de la base de datos (FQDN completo para servicios en la nube)
PGDATABASE = 'credit_educativo'                    # Nombre de la base de datos
PGUSER = 'susana'                                  # Usuario de la base de datos
PGPASSWORD = 'NcW6icU3aJPKRgp2vYBvTEwQ8ahK58px'   # Contraseña del usuario
PGPORT = '5432'                                    # Puerto (por defecto 5432 para PostgreSQL) 

