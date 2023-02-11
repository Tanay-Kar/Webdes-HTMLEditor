import sys , os
from editor import Editor
from PyQt5.QtWidgets import QFileDialog,QMessageBox,QApplication,QTextEdit
from PyQt5.QtCore import QSettings
from PyQt5.QtGui import QIcon
from modules.Ui_main import Ui_MainWindow
import qtvscodestyle as qvsc

class Window(Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
        self.setWindowTitle("WebDes")
        self.setWindowIcon(QIcon("Resources\icon.png"))
        self.tabWidget.removeTab(0)
        self.create_tab()
        self.settings = QSettings("Tanay Kar", "WebDes")
        self.tabWidget.tabCloseRequested.connect(self.handle_tab_close)
        self.editor = self.tabWidget.currentWidget()
        self.editor = Editor()
        self.resize(1200,800)
        self.path = ""
        
        if self.settings.value("theme", type="int") == 0:   # type: ignore
            '''
            0 => Light
            1 => Dark
            '''
            self.set_theme("LIGHT")
            
        else:
        
            self.set_theme("DARK")
        
    
        # Actions
        # style = qvsc.load_stylesheet(qvsc.Theme.DARK_VS)
        # self.setStyleSheet(style)
        self.action_New.triggered.connect(self.create_tab)
        self.action_Refresh.triggered.connect(
            lambda: self.editor.webView.update())
        self.action_Dark.triggered.connect(lambda: self.set_theme("DARK"))
        self.action_Light.triggered.connect(lambda: self.set_theme("LIGHT"))
        self.action_Save.triggered.connect(self.save_file)
        self.action_Open.triggered.connect(self.open_file)
        
        self.tabWidget.currentChanged.connect(self.status_bar)
        
        #self.tabWidget.currentWidget = Editor
        
        self.tabWidget.currentWidget().textEdit.cursorPositionChanged.connect(self.status_bar)
    
    def status_bar(self):
        try:
            x = self.tabWidget.currentWidget().cursor_x
            y = self.tabWidget.currentWidget().cursor_y
            self.statusBar().showMessage(f'Ln {str(x())}, Col {str(y())}')
        except:
            pass
    def save_file(self):
        
        editor = self.tabWidget.currentWidget()
        text = editor.textEdit.toPlainText()
        if not(editor.saved):
            path,_ = QFileDialog.getSaveFileName(self, 'Save File','','HTML files (*.html *.htm *.xhtml);;Text files (*.txt);;All files (*.*)')
            filename = os.path.basename(path)

            # file = open(name,'w')
            # file.write(text)
            # file.close()
            if path == '':
                # Dialog canceled
                pass
            else:
                with open(path, 'w') as f:
                    # write text in the file
                    try:
                        f.write(text)
                        editor.save(path) 
                        editor.update()
                    except:
                        msgBox = QMessageBox()
                        msgBox.setIcon(QMessageBox.Warning)  # type: ignore
                        msgBox.setText("There was a error in saving the file \nPlease check for incompatible(non ASCII charactors).")
                        msgBox.setWindowTitle("Error")
                        msgBox.setStandardButtons(QMessageBox.Ok)
                        msgBox.exec()
                    

            self.tabWidget.setCurrentWidget(editor)
            self.tabWidget.setTabText(self.tabWidget.currentIndex(),filename)          

        else:
            self.statusBar().showMessage("Saved",5)
            

                            
    
    def open_file(self):
        #editor = self.tabWidget.currentWidget()
        #text = editor.textEdit.toPlainText()
        #print(text)
        self.create_tab()
        editor = self.tabWidget.currentWidget()
        path, _ = QFileDialog.getOpenFileName(self,"Open file", "",'HTML files (*.html *.htm *.xhtml);;Text files (*.txt);;All files (*.*)')
        filename = os.path.basename(path)

        # file = open(name,'w')
        # file.write(text)
        # file.close()
        if path == '':
            # Dialog canceled
            pass
        else:
            with open(path,'r+') as file:
                
                editor.textEdit.setPlainText(file.read())
                editor.update()
                text = file.read()
                file.write(text)
                editor.save(path) 
                editor.update()
                
        
            # write text in the file
                
        self.tabWidget.setCurrentWidget(editor)
        self.tabWidget.setTabText(self.tabWidget.currentIndex(),filename)          
        
    def handle_tab_close(self, index):
        self.tabWidget.setCurrentIndex(index)
        editor = self.tabWidget.currentWidget()
        
        saved = editor.saved
        if saved :
            if self.tabWidget.count() <= 0:
                sys.exit()
                
            else:
                self.tabWidget.removeTab(index)
        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("Do you want to save the file ?")
            msgBox.setWindowTitle("Save file")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            save_result = msgBox.exec()
            if save_result == QMessageBox.Yes:
                self.save_file()
            elif save_result == QMessageBox.No:
                if self.tabWidget.count() <= 0:
                    sys.exit()

                else:
                    self.tabWidget.removeTab(index)
            else:
                pass
    
        
    def create_tab(self):
        editor = Editor()
        i = self.tabWidget.addTab(editor, "Untitled")
        self.tabWidget.setCurrentIndex(i)
        self.tabWidget.currentWidget().textEdit.cursorPositionChanged.connect(self.status_bar)
    
    def set_theme(self, theme):
        if theme == "LIGHT":
            style = qvsc.load_stylesheet(qvsc.Theme.LIGHT_VS)
            self.toolBar.actions()[6].setVisible(False)
            self.toolBar.actions()[5].setVisible(True)
            self.settings.setValue('theme',0)
            
        elif theme == "DARK":
            style = qvsc.load_stylesheet(qvsc.Theme.DARK_VS)
            self.toolBar.actions()[6].setVisible(True)
            self.toolBar.actions()[5].setVisible(False)
            self.settings.setValue('theme',1)
        else:
            style = ''    
        self.setStyleSheet(style)



if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())
