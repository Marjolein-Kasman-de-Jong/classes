# Opdracht 9-11 Geïmporteerde beheerder

from user_privileges_admin_module import Admin

new_user = Admin('donald', 'duck', 'donald@duckmail.dk', 'duckstad')
new_user.privileges.show_privileges()
