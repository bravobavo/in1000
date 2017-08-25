try:
    shutil.rmtree('code')
    print('Removed old code directory')
except FileNotFoundError:
    pass
