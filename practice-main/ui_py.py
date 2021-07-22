"""
Конвертация .ui-файла в .py-файл
"""

import subprocess

subprocess.run(["pyuic5", "THEORY.ui", "-o", "THEORY.py"])

