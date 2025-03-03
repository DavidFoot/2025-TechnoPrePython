import sys

def is_venv():
    return (hasattr(sys, 'real_prefix') or
    (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))

if is_venv():
    print('Exécution dans un environnement virtuel')
else:
    print('N est pas exécuté dans un environnement virtuel')