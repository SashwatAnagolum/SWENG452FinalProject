from PyQt6.uic import compileUi

compileUi('form.ui', open('ui_form.py', 'w'), execute=False, indent=4)