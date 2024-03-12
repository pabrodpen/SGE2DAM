import odoorpc
import sys
import re

# Datos de conexión a la instancia de Odoo
HOST = 'localhost'
PORT = 8069
DB = 'odooDB'
USER = 'admin'
PASSWORD = 'admin'

# Conexión a la instancia de Odoo
odoo = odoorpc.ODOO(HOST, port=PORT)
odoo.login(DB, USER, PASSWORD)

# Función para corregir los nombres de los productos
def sanitize_product_name(name):
    # Conservar solo caracteres alfanuméricos, espacios y caracteres especiales como la "ñ" y las letras con tilde
    return re.sub(r'[^\w\sáéíóúüñ]', '', name)

def generar_archivo_ventas(year, month):
    next_month = month + 1 if month < 12 else 1  # Manejo del siguiente mes
    next_year = year + 1 if month == 12 else year  # Manejo del siguiente año
    # Filtrar registros de ventas por año y mes
    sales = odoo.env['sale.order'].search_read([
        ('date_order', '>=', f'{year}-{month:02}-01'),
        ('date_order', '<', f'{next_year}-{next_month:02}-01')  # Utilizar el siguiente mes y año
    ], ['order_line'])

    print(f"Ventas encontradas para {mes_nombre(month)}: {len(sales)}")

    if sales:
        # Diccionario para almacenar la cantidad vendida de cada producto
        product_sales = {}

        # Calcular la cantidad vendida de cada producto
        for sale in sales:
            for line in sale['order_line']:
                if isinstance(line, int):  # Manejar caso donde line es un entero
                    line = odoo.env['sale.order.line'].browse(line).read(['product_id', 'product_uom_qty'])[0]
                product_ids = line.get('product_id')
                product_qty = line.get('product_uom_qty', 0)
                if isinstance(product_ids, list):
                    for product_id in product_ids:
                        if product_id and isinstance(product_id, int):
                            try:
                                product_sales[product_id] = product_sales.get(product_id, 0) + product_qty
                            except Exception as e:
                                print(f"Error al procesar producto con ID {product_id}: {e}")
                                print(f"Contenido de la variable 'line': {line}")
                else:
                    if product_ids and isinstance(product_ids, int):
                        try:
                            product_sales[product_ids] = product_sales.get(product_ids, 0) + product_qty
                        except Exception as e:
                            print(f"Error al procesar producto con ID {product_ids}: {e}")
                            print(f"Contenido de la variable 'line': {line}")

        # Ordenar productos por cantidad vendida
        sorted_products = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)

        # Escribir los resultados en el archivo
        file_name = f'{year}{mes_nombre(month)}.lst'
        print(f"Escribiendo resultados en {file_name}")
        try:
            with open(file_name, 'w', encoding='utf-8') as f:  # Utilizando UTF-8
                for product_id, qty_sold in sorted_products:
                    product = odoo.env['product.product'].browse(product_id)
                    if product:
                        product_name = sanitize_product_name(product.name)
                        f.write(f'{str(product_name)}: {qty_sold}\n')
            print("Archivo generado exitosamente.")
        except Exception as e:
            print(f"Error al escribir en el archivo {file_name}: {e}")
            raise  # Levantar la excepción para mostrarla completamente
    else:
        print(f"No hay ventas encontradas para {mes_nombre(month)}")

def mes_nombre(month):
    nombres_meses = [
        'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
        'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'
    ]
    return nombres_meses[month - 1]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 ventas.py <año>")
        sys.exit(1)

    year = int(sys.argv[1])

    for month in range(1, 13):
        generar_archivo_ventas(year, month)

    print("Archivos generados exitosamente.")
