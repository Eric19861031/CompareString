import  os
if __name__ == '__main__':
    from PyInstaller.__main__ import run
    opts=['compareWin.py','-w','-F']
    run(opts)