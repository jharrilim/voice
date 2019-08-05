import os

if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.system(f'docker build -t rasavoice:vrec --target vrec {dir_path}{os.path.sep}..{os.path.sep}')
    os.system(f'docker build -t rasavoice:app --target app {dir_path}{os.path.sep}..{os.path.sep}')
