import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QInputDialog, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5.QtGui import QPalette, QColor, QFont, QPainter
from PyQt5.QtCore import Qt


class StockMinderWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Configura el tema oscuro
        self.table = None
        dark_palette = QPalette()
        dark_palette.setColor(QPalette.Window, QColor('#bbdea7'))
        dark_palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
        dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Text, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
        dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))

        # Configura el título de la ventana en la esquina superior izquierda
        self.title_label = QLabel('StockMinder', self)
        self.title_label.move(10, 10)
        self.title_label.setStyleSheet("color: rgb(0, 0, 0)")
        self.title_label.setFont(QFont("Arial", 12, QFont.Bold))

        # Crea el botón pulsador
        self.button_label = QLabel('Agregar\nproductos', self)
        self.button_label.move(5, 50)
        self.button_label.setStyleSheet(
            "background-color: #bbdea7; color: rgb('255, 255, 255'); padding: 5px; border-radius: 5px; cursor: pointer;"
        )
        self.button_label.setFont(QFont("Arial", 10, QFont.Bold))
        self.button_label.setAlignment(Qt.AlignCenter)
        self.button_label.setFixedWidth(110)
        self.button_label.mousePressEvent = self.on_button_clicked

        self.setWindowTitle('StockMinder')
        self.setGeometry(400, 400, 1200, 800)
        self.setPalette(dark_palette)
        self.setAutoFillBackground(True)

    def on_button_clicked(self, event):
        # Mostrar cuadro de diálogo para agregar nombre de producto
        product_name, ok = QInputDialog.getText(self, "Agregar Producto", "Nombre del Producto:")
        if ok and product_name:
            print("Nombre del producto:", product_name)

        product_price, ok = QInputDialog.getText(self, "Agregar Producto", "Precio:")
        if ok and product_name:
            print("Precio del Producto:", product_price)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)  # Elimina el borde blanco

        painter.setBrush(QColor('#8fbe7e'))
        painter.drawRoundedRect(0, -10, self.width() - 1080, 900, 10, 10)

        painter.setBrush(QColor('#639d54'))
        painter.drawRoundedRect(0, -10, self.width() - 1080, 50, 10, 10)

        # Crea un layout vertical
        layout = QVBoxLayout()

        # Crea la tabla
        self.table = QTableWidget(9, 6)
        self.table.setHorizontalHeaderLabels(['Id', 'Artículo', 'Precio', 'Unidades', 'Ingreso', 'Peso'])
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)  # Deshabilita la edición de celdas
        self.table.setSelectionBehavior(QTableWidget.SelectRows)  # Seleccionar filas completas
        self.table.setStyleSheet(
            "QHeaderView::section { background-color: #639d54; color: white; }")  # Estilo del encabezado
        self.table.setFont(QFont("Arial", 10))

        # Rellenar la tabla con datos de ejemplo
        for row in range(9):
            for col in range(6):
                item = QTableWidgetItem(f'Dato {row + 1}-{col + 1}')
                self.table.setItem(row, col, item)

        # Agrega la tabla al layout
        layout.addWidget(self.table)

        # Establece el margen izquierdo del layout para mover la tabla hacia la derecha
        layout.setContentsMargins(150, 20, 433, 100)

        # Establece el layout en el widget principal
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = StockMinderWindow()
    window.show()
    sys.exit(app.exec())
