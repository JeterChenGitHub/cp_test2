from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QThread
import subprocess


class Nand(QThread):
    sig_update_ui = pyqtSignal(object)

    def __init__(self):
        QThread.__init__(self)
        self.cmd = 'adb shell ./home/flex/bin/fct1-main.sh  FCT.1.2.1 '

    def run(self):
        self.sig_update_ui.emit('Nand test')
        result = subprocess.Popen(self.cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        (output, err) = result.communicate()
        return_code = result.wait()
        if return_code == 0:
            self.sig_update_ui.emit(str(output, encoding='UTF-8'))
        else:
            self.sig_update_ui.emit(str(err, encoding='UTF-8'))
        self.sig_update_ui.emit('Nand end')