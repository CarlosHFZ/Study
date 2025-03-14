# QApplication e QPushButton de PySide6.QtWidgets
# QApplication -> O Widget principal da aplicação
# QPushButton -> Um botão
# PySide6.QtWidgets -> Onde estão os widgets do PySide6
import sys
from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)

####

buttom1 = QPushButton('Texto do botão')
buttom1.setStyleSheet('font-size: 40px;')
buttom1.show()  # Adionar o widget na hieararquia e exibe a janela

buttom2 = QPushButton('Texto do botão')
buttom2.show()

app.exec()  # O loop da aplicação
