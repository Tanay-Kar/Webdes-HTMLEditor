# WebDes
A HTML editor coded in Python using the PyQt5 framework.

This is a real-time updating editor with the capabilities of displaying HTML code/files in a Chromium version 94.0. 4606 engine.

Its features include :
- Real time update
- Auto save
- Ability to display local images
- Syntax highlighting
- Multi tabbed editor

## Installation

For building on linux distros , see [this](#building-on-linux-distros)

- You have to have github and python3 or greater installed .
- Clone this repository
```bash
git clone https://github.com/Tanay-Kar/HTML-Editor.git
```
- Navigate to the folder
```bash
cd HTML-Editor
```
- Install the required packages
```bash
pip install -r requirements.txt
```

- Finally run the ```main.py``` file
```bash
python main.py
```
## Building on Linux distros
For some internal bug, the PyQt5 webengine widget may not work as expected on some linux distros. A workaround(tested on Ubuntu, Fedora and Manjaro), is provided for the time being.
The workaround is based on [this](https://stackoverflow.com/a/73874077) stackoverflow answer

Delete the previous PyQt5 packages installed using pip3
```bash
pip3 uninstall PyQt5 PyQt5-Qt5 PyQt5-sip PyQtWebEngine PyQtWebEngine-Qt5
```
Install QtWebEngine using ```apt```(or the appropriate package manager for your distro)
(```apt``` will automatically install ```PyQt5```)
```bash
sudo apt install python3-pyqt5.qtwebengine
```
Proceed with the [above](#installation) installation steps.

## Screenshots
![2022-12-22 14-04-59](https://user-images.githubusercontent.com/93914273/209092832-a4cfdcec-8a0e-4cfb-9d04-58b3193416e3.gif)



![2022-12-22 14-17-41](https://user-images.githubusercontent.com/93914273/209096110-e5c20d80-4e82-4a7f-ae6b-8d5ae1abdc4b.png)
Adding a local image requires saving the file


Light theme                |  Dark Theme
:-------------------------:|:-------------------------:
![2022-12-22 14-17-42](https://user-images.githubusercontent.com/93914273/209095313-be70ea30-e69b-4af3-aa7b-9ddcd1a927e1.png) | ![2022-12-22 14-17-41](https://user-images.githubusercontent.com/93914273/209096110-e5c20d80-4e82-4a7f-ae6b-8d5ae1abdc4b.png)


### Note
As of now , this project has been tested on several linux and windows operating systems. Voulunteers for creating a mac os build and finding bugs in the project in mac os are requested to contact me on [contact.tanaykar@gmail.com](mailto:contact.tanaykar@gmail.com)
# Conclusion
I hope that this project of mine helps you. Suggestions and features are welcome and as for bugs please inform in the github bug tracker. I will try my best to fix it.

