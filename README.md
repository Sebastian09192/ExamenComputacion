# Proyecto Kubernetes + Legacy

## Contenido
- **source/frontend**: HTML básico para interactuar con APIs.
- **source/legacy**: Módulo Legacy en PHP con inventario.
- **deploy**: Archivos de despliegue (K8s, Nginx).
- **docs**: Documentación del proyecto.
- **evidence**: Evidencias y capturas.

## Cómo ejecutar Legacy
1. Instalar LAMP stack (Apache, PHP, MariaDB).
2. Crear la BD:
   \`\`\`sql
   CREATE DATABASE legacy_inventory;
   USE legacy_inventory;
   CREATE TABLE products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), stock INT);
   INSERT INTO products (name, stock) VALUES ('Producto A', 20), ('Producto B', 10);
   \`\`\`
3. Copiar **source/legacy/inventory.php** a \`/var/www/html/legacy/\`.
4. Acceder en: \`http://localhost/legacy/inventory.php\`.
EOF