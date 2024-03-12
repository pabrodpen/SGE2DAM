<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulario y Listado de Ventas</title>
    <style>
        /* Estilos para el contenedor principal */
        body, html {
            height: 100%;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        /* Estilos para la imagen */
        img {
            width: 100%;
            height: 30%;
        }

        /* Estilos para el contenedor del contenido principal */
        .contenido-container {
            width: 100%;
            max-width: 800px;
            padding: 30px;
        }

        /* Estilos para la tabla */
        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
        }

        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: left;
        }

        th {
            background-color: #f2f2f2;
        }

        /* Estilos para el texto de la fecha de generación */
        .fecha-generacion {
            margin-top: 20px;
            text-align: center;
            font-weight: bold;
            font-style: italic;
        }
    </style>
</head>
<body>
    <!-- Encabezado -->
    <img src="odoo_imagen.jpg" alt="Imagen de la compañía">

    <!-- Contenido principal -->
    <div class="contenido-container">
        <!-- Formulario -->
        <h2>Ingresa el rango de fechas</h2>
        <form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="POST">
            <label for="dia_inicio">Día de inicio:</label>
            <select name="dia_inicio" id="dia_inicio">
                <?php
                // Generar opciones para los días del mes
                for ($dia = 1; $dia <= 31; $dia++) {
                    echo "<option value='$dia'>$dia</option>";
                }
                ?>
            </select>
            <label for="mes_inicio">Mes de inicio:</label>
            <select name="mes_inicio" id="mes_inicio">
                <?php
                // Generar opciones para los meses del año
                $meses = array("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre");
                foreach ($meses as $numero_mes => $nombre_mes) {
                    $numero_mes++; // Ajustar el índice de 0 a 1
                    echo "<option value='$numero_mes'>$nombre_mes</option>";
                }
                ?>
            </select>
            <label for="anio_inicio">Año de inicio:</label>
            <select name="anio_inicio" id="anio_inicio">
                <?php
                // Generar opciones para los años
                $anio_actual = date('Y');
                for ($anio = $anio_actual - 10; $anio <= $anio_actual; $anio++) {
                    echo "<option value='$anio'>$anio</option>";
                }
                ?>
            </select>
            <br><br>
            <label for="dia_fin">Día de fin:</label>
            <select name="dia_fin" id="dia_fin">
                <?php
                // Generar opciones para los días del mes
                for ($dia = 1; $dia <= 31; $dia++) {
                    echo "<option value='$dia'>$dia</option>";
                }
                ?>
            </select>
            <label for="mes_fin">Mes de fin:</label>
            <select name="mes_fin" id="mes_fin">
                <?php
                // Generar opciones para los meses del año
                foreach ($meses as $numero_mes => $nombre_mes) {
                    $numero_mes++; // Ajustar el índice de 0 a 1
                    echo "<option value='$numero_mes'>$nombre_mes</option>";
                }
                ?>
            </select>
            <label for="anio_fin">Año de fin:</label>
            <select name="anio_fin" id="anio_fin">
                <?php
                // Generar opciones para los años
                $anio_actual = date('Y');
                for ($anio = $anio_actual - 10; $anio <= $anio_actual; $anio++) {
                    echo "<option value='$anio'>$anio</option>";
                }
                ?>
            </select>
            <br><br>
            <!-- Botón para buscar-->
            <button type="submit">Buscar</button>
        </form>

        <!-- Tabla de ventas -->
       <?php
// Si se han enviado los datos del formulario
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Conexión a la base de datos de Odoo
    $host = "localhost";
    $port = "5432";
    $dbname = "odooDB";
    $user = "odoo";
    $password = "odoo";

    $conn = pg_connect("host=$host port=$port dbname=$dbname user=$user password=$password");

    if (!$conn) {
        die("Error de conexión: " . pg_last_error());
    }

    // Obtener las fechas de inicio y fin del formulario
    $dia_inicio = $_POST['dia_inicio'];
    $mes_inicio = $_POST['mes_inicio'];
    $anio_inicio = $_POST['anio_inicio'];
    $dia_fin = $_POST['dia_fin'];
    $mes_fin = $_POST['mes_fin'];
    $anio_fin = $_POST['anio_fin'];

    // Construir las fechas de inicio y fin para el rango de fechas
    $fecha_inicio = "$anio_inicio-$mes_inicio-$dia_inicio";
    $fecha_fin = "$anio_fin-$mes_fin-$dia_fin";

    // Consulta para obtener los productos vendidos en el rango de fechas
    $sql = "SELECT pt.name AS product_name, ROUND(SUM(sol.product_uom_qty)) AS cantidad_vendida
            FROM sale_order_line AS sol
            INNER JOIN product_product AS pp ON sol.product_id = pp.id
            INNER JOIN product_template AS pt ON pp.product_tmpl_id = pt.id
            INNER JOIN sale_order AS so ON sol.order_id = so.id
            WHERE so.date_order BETWEEN '$fecha_inicio' AND '$fecha_fin'
            GROUP BY pt.name
            ORDER BY cantidad_vendida DESC";

    $result = pg_query($conn, $sql);

    // Mostrar el listado de ventas
    echo "<h2>Listado de Ventas para el período entre $fecha_inicio y $fecha_fin</h2>";
    echo "<table border='1'>";
    echo "<tr><th>Producto</th><th>Cantidad Vendida</th></tr>";
    if (pg_num_rows($result) > 0) {
        while ($row = pg_fetch_assoc($result)) {
            echo "<tr><td>" . $row["product_name"] . "</td><td>" . $row["cantidad_vendida"] . "</td></tr>";
        }
    } else {
        // Caso: No se encontraron ventas en el rango de fechas seleccionado.
        echo "<tr><td colspan='2'>No se encontraron ventas en el rango de fechas seleccionado.</td></tr>";
    }
    echo "</table>";

    // Mostrar la fecha de generación
    echo "<p class=\"fecha-generacion\">Fecha de generación: " . date("d-m-Y") . "</p>";

    pg_close($conn);
}
?>


        <!-- Fecha de generación -->
        <p class="fecha-generacion">Fecha de generación: <?php echo date("d-m-Y"); ?></p>
    </div>
</body>
</html>

