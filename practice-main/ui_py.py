"""
Конвертация .ui-файла в .py-файл
"""

import subprocess

subprocess.run(["pyuic5", "calculatorDialog.ui", "-o", "calculatorDialog.py"])

