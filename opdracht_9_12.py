# Opdracht 9-12 Meerdere modules

from admin_module import Admin

another_new_user = Admin('mickey', 'mouse', 'mickey@mousemail.dk', 'duckstad')
another_new_user.privileges.show_privileges()