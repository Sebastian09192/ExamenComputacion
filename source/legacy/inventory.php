<?php

\$conn = new mysqli("localhost", "root", "", "legacy_inventory");
if (\$conn->connect_error) {
    die("Error de conexión: " . \$conn->connect_error);
}
\$result = \$conn->query("SELECT * FROM products");
\$rows = array();
while(\$row = \$result->fetch_assoc()) {
    \$rows[] = \$row;
}
header('Content-Type: application/json');
echo json_encode(\$rows);

?>