import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QFontMetricsF
if __name__ != "__main__":
    # For import scenarios 
    from modules.Ui_editor import Ui_Form 
else: 
    # For individual test scenarios
    from Ui_editor import Ui_Form
    
    
class Editor(Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.textEdit.textChanged.connect(self.update)
        self.zoom = self.webView.zoomFactor()
        self.saved = False
        self.path = str()
        self.cursor_x, self.cursor_y = lambda: self.textEdit.textCursor().columnNumber(),lambda: self.textEdit.textCursor().blockNumber()
        font = self.textEdit.font()
        fontMetrics = QFontMetricsF(font)
        spaceWidth = fontMetrics.width(' ')
        self.textEdit.setTabStopDistance(spaceWidth * 4)
        print('______INITIALIZED EDITOR_______')


    def update(self):
        if self.saved :
            self.save_text()
            self.webView.load(QUrl.fromLocalFile(self.path))          
        else:
            text = self.textEdit.toPlainText()
            self.webView.setHtml(text)  
        self.cursor_x = lambda: self.textEdit.textCursor().columnNumber()
        self.cursor_y = lambda: self.textEdit.textCursor().blockNumber()
        #self.textEdit.cursorPositionChanged.connect(lambda: print(self.cursor_x(),self.cursor_y()))
        
    def save(self,path):
        self.saved = True
        self.path = path
        print(self.path , self.saved)
    
    def save_text(self):
        text = self.textEdit.toPlainText()
        with open(self.path, 'r+') as f:
                # write text in the file
                f.write(text)
                #print('saved')
    
             

if __name__ == "__main__":
    from Ui_editor import Ui_Form        
    app = QApplication([])
    widget = Editor()
    widget.show()
    sys.exit(app.exec())
    
    
