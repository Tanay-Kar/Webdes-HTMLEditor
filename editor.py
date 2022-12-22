import sys
from modules.Ui_editor import Ui_Form
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl


class Editor(Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.textEdit.textChanged.connect(self.update)
        self.zoom = self.webView.zoomFactor()
        self.saved = False
        self.path = str()
        self.cursor_x, self.cursor_y = lambda: self.textEdit.textCursor().columnNumber(),lambda: self.textEdit.textCursor().blockNumber()
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
    app = QApplication([])
    widget = Editor()
    widget.show()
    sys.exit(app.exec())
    
    
