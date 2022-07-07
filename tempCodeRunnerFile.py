    try:
        call("pip install --upgrade " + ' '.join(package), shell=True)
    except:
        pass
