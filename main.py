import glob
import json
import shutil
import sys
import os
from PIL import Image
from PyQt5 import QtWidgets, uic, QtCore, QtGui


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        _ui = "./ui/UI.ui"
        uic.loadUi(_ui, self)
        self.file_list = []
        self.current_number = 0
        self.graphicsview_size = (512, 288)
        self.img_size = (0, 0)
        self.status = {"auto labeling": True, "save values": "r", "hard delete": False, "pre_class_path": "",
                       "pre_label_path": ""}
        self.class_dict = {}
        self.class_path = ""
        self.class_num = -1
        self.label_path = ""
        self.deleteAction = QtWidgets.QAction(self)
        self.init_fuc()
        self.show()

    def init_fuc(self):
        self.setting_init()
        self.ui_init()
        self.function_init()

    def function_init(self):
        # File menu
        self.actionOpenFile.triggered.connect(self.open_file_dialog)
        self.actionOpenFolder.triggered.connect(self.open_folder_dialog)
        self.actionClose.triggered.connect(self.close_func)
        self.actionNewClassFile.triggered.connect(self.new_class_file_dialog_start)
        self.actionOpenClassFile.triggered.connect(self.class_file_dialog)
        # setting menu
        self.actionAutoLabeling.toggled.connect(self.autolabeling_set)
        self.actionABS.toggled.connect(lambda x: self.savevalues_set("a"))
        self.actionREL.toggled.connect(lambda x: self.savevalues_set("r"))
        self.actionHardDelete.toggled.connect(self.harddelete_set)
        self.actionSaveSetting.triggered.connect(self.setting_save)
        #tool menu
        self.actionAddupFolder.triggered.connect(self.concatenate_dialog_start)
        self.actionMakeDataset.triggered.connect(self.make_dataset_dialog_start)
        # ListWidget
        self.fileListWidget.currentRowChanged.connect(self.index_change)
        # Button
        self.deleteButton.clicked.connect(self.delete_fuc)
        self.deleteButton.setShortcut("delete")
        self.upButton.clicked.connect(self.up_func)
        self.upButton.setShortcut("w")
        self.downButton.clicked.connect(self.down_func)
        self.downButton.setShortcut("s")
        self.classPathButton.clicked.connect(self.path_folder_dialog)
        # labelTableWidget
        self.labelTableWidget.cellDoubleClicked.connect(self.delete_cell)
        self.deleteAction.triggered.connect(self.to_delete_cell)
        self.deleteAction.setShortcut("q")
        # Text Browser
        self.filesTextEdit.textChanged.connect(self.number_change)
        # Timer
        self.timer.timeout.connect(self.update_2)

    def ui_init(self):
        self.graphicsView = newGraphicView()
        self.graphicsViewGridLayout.addWidget(self.graphicsView)
        self.save_values_group = QtWidgets.QActionGroup(self.menuSaveValues)
        self.save_values_group.addAction(self.actionABS)
        self.save_values_group.addAction(self.actionREL)
        self.save_values_group.setExclusive(True)
        self.setAcceptDrops(True)
        self.msgbox = QtWidgets.QMessageBox()

    def setting_init(self):
        if os.path.exists("./setting.json"):
            with open("./setting.json", "r") as fr:
                self.status = json.load(fr)
                self.setting_change()
        self.timer = QtCore.QTimer()
        self.timer.start(30)
        only_int = QtGui.QIntValidator()
        self.filesTextEdit.setValidator(only_int)

    def update_2(self):
        try:
            cur_size = (self.graphicsView.width(), self.graphicsView.height())
            if self.graphicsview_size != cur_size:
                self.graphicsview_size = cur_size
                self.change_window_size()
        except:
            pass

    def open_file_dialog(self):
        filter_ = "Images (*.jpg *.png)"
        file_list = QtWidgets.QFileDialog.getOpenFileNames(self, 'Select File', filter=filter_)[0]
        if not file_list:
            return
        return self.load_urls(file_list)

    def open_folder_dialog(self):
        folder_list = [QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder', )]
        if folder_list == [""]:
            return
        return self.load_urls(folder_list)

    def close_func(self):
        self.close()

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        e.accept()
        urls = e.mimeData().urls()
        return self.load_urls(urls)

    def closeEvent(self, e):
        ret = QtWidgets.QMessageBox.question(self, "Exit?", "Are You Sure?",
                                             QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
        if ret == QtWidgets.QMessageBox.Yes:
            e.accept()
        else:
            e.ignore()

    def select_class(self, id_):
        self.class_num = id_

    def up_func(self):
        if self.fileListWidget.currentRow() < len(self.file_list):
            self.fileListWidget.setCurrentRow(self.fileListWidget.currentRow() + 1)

    def down_func(self):
        if self.fileListWidget.currentRow() > 0:
            self.fileListWidget.setCurrentRow(self.fileListWidget.currentRow() - 1)

    def index_change(self, inx):
        self.save_txt_call()
        self.current_number = inx + 1
        self.filesTextEdit.setText(str(self.current_number))

    def number_change(self):
        self.button_enable()
        return self.change_file()

    def delete_fuc(self):
        if self.status["hard delete"]:
            file_name = self.file_list.pop(self.current_number - 1)
            os.remove(file_name)
        else:
            self.file_list.pop(self.current_number - 1)
        if len(self.file_list) == self.current_number:
            return self.do_list(self.current_number - 1)
        return self.do_list(self.current_number)

    def setting_save(self):
        with open("./setting.json", "w") as fw:
            fw.write(json.dumps(self.status))
        self.msg_box("Success", "Setting is Saved!", "info")

    def setting_change(self):
        self.actionAutoLabeling.setChecked(self.status["auto labeling"])
        if self.status["save values"] == "r":
            self.actionABS.setChecked(False)
            self.actionREL.setChecked(True)
        else:
            self.actionABS.setChecked(True)
            self.actionREL.setChecked(False)
        self.actionHardDelete.setChecked(self.status["hard delete"])
        try:
            self.class_path = self.status["pre_class_path"]
            self.set_class_table(self.class_path)
            self.label_path = self.status["pre_label_path"]
            self.labelPathLineEdit.setText(self.label_path)
        except:
            pass

    def autolabeling_set(self):
        self.status["auto labeling"] = self.actionAutoLabeling.isChecked()

    def savevalues_set(self, key):
        self.status["save values"] = key

    def harddelete_set(self):
        self.status["hard delete"] = self.actionHardDelete.isChecked()

    def button_enable(self):
        if self.current_number == 1:
            self.downButton.setEnabled(False)
        elif self.current_number == len(self.file_list):
            self.upButton.setEnabled(False)
        else:
            self.downButton.setEnabled(True)
            self.upButton.setEnabled(True)

    def load_urls(self, urls):
        file_list = []
        # 다수의 파일일 경우
        if len(urls) > 1:
            for url in urls:
                if isinstance(url, QtCore.QUrl):
                    url = url.toLocalFile()
                if self.check_file(url):
                    file_list.append(url)
                else:
                    explored_list = self.explore_folder(url)
                    file_list.extend(explored_list)
        elif len(urls) == 1:
            if isinstance(urls[0], QtCore.QUrl):
                url = urls[0].toLocalFile()
            else:
                url = urls[0]
            if ".json" in url:
                return self.set_class_table(url)
            if self.check_file(url):
                file_list.append(url)
            else:
                explored_list = self.explore_folder(url)
                file_list.extend(explored_list)
        if len(file_list) == 0:
            self.msg_box("Error", "No Image Files", "warning")
            return
        else:
            self.file_list = file_list
            return self.do_list()

    def check_file(self, url):
        if os.path.isfile(url):
            return True
        elif os.path.isdir(url):
            return False

    def explore_folder(self, url):
        file_list = []
        for ext in ("*.jpg", "*.png"):
            path = os.path.join(url, f"**/{ext}")
            tmp_list = glob.glob(path, recursive=True)
            file_list.extend(tmp_list)
        return file_list

    def msg_box(self, title="title", txt="", icon="info", buttons=["ok"]):
        if "info" in icon:
            icon = QtWidgets.QMessageBox.Information
        elif "warn" in icon:
            icon = QtWidgets.QMessageBox.Warning
        self.msgbox.setIcon(icon)
        self.msgbox.setWindowTitle(title)
        if buttons != ["ok"]:
            if isinstance(buttons, str):
                msg_button = self.button_func(buttons)
                self.msgbox.addButton(msg_button)
            elif isinstance(buttons, list) or isinstance(buttons, tuple):
                for button in buttons:
                    msg_button = self.button_func(button)
                    self.msgbox.addButton(msg_button)
        else:
            self.msgbox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.msgbox.setText(txt)
        ret = self.msgbox.exec_()
        return ret

    def button_func(self, button):
        button = button.lower()
        if "ok" in button:
            return QtWidgets.QMessageBox.Ok
        elif "yes" in button:
            return QtWidgets.QMessageBox.Yes
        elif "no" in button:
            return QtWidgets.QMessageBox.No
        elif "cancel" in button:
            return QtWidgets.QMessageBox.Cancel
        elif "close" in button:
            return QtWidgets.QMessageBox.Close
        elif button == "save":
            return QtWidgets.QMessageBox.Save
        elif button == "saveall":
            return QtWidgets.QMessageBox.SaveAll
        return None

    def do_list(self, num=1):
        self.fileListWidget.clear()
        if len(self.file_list) == 0:
            scene = QtWidgets.QGraphicsScene()
            self.graphicsView.setScene(scene)
            return self.msg_box("Error", "No Files", "info")
        for fn in self.file_list:
            file_name = fn.split("\\")[-1]
            file_name = file_name.split("/")[-1]
            self.fileListWidget.addItem(file_name)
        self.list_in_init(num)

    def list_in_init(self, num):
        self.filesLabel.setText(str(len(self.file_list)))
        self.current_number = num
        self.filesTextEdit.setText(str(self.current_number))
        self.fileListWidget.setModelColumn(self.current_number - 1)
        self.filesTextEdit.setEnabled(True)
        self.upButton.setEnabled(True)
        self.deleteButton.setEnabled(True)
        # self.label_path_func()
        
    def path_folder_dialog(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder', )
        if folder == "":
            return
        return self.path_folder_func(folder)

    def path_folder_func(self, folder_name):
        self.label_path = folder_name
        self.status["pre_label_path"] = self.label_path
        self.labelPathLineEdit.setText(self.label_path)

    def set_class_table(self, path):
        with open(path, "r") as fr:
            tmp_dict = json.load(fr)
        if not tmp_dict:
            self.msg_box("Error", "No Have Data", "warning")
            return
        for v in tmp_dict.values():
            if not isinstance(v, int):
                self.msg_box("Error", "Invalid file.", "warning")
                return
        self.class_dict = tmp_dict
        n = 0
        self.classTableWidget.clearContents()
        self.classTableWidget.setRowCount(len(self.class_dict))
        self.class_group = QtWidgets.QButtonGroup()
        self.class_group.setExclusive(True)
        self.class_group.idClicked.connect(self.select_class)
        for i, j in self.class_dict.items():
            setattr(self, f"bs{n}", QtWidgets.QRadioButton())
            self.class_group.addButton(getattr(self, f"bs{n}"))
            self.class_group.setId(getattr(self, f"bs{n}"), n)
            self.classTableWidget.setCellWidget(n, 0, getattr(self, f"bs{n}"))
            self.classTableWidget.setItem(n, 1, QtWidgets.QTableWidgetItem(i))
            self.classTableWidget.setItem(n, 2, QtWidgets.QTableWidgetItem("{:04d}".format(j)))
            if n < 9:
                getattr(self, f"bs{n}").setShortcut(QtGui.QKeySequence(f"{n+1}"))
            n += 1
        getattr(self, f"bs{0}").click()
        self.class_path = path
        self.status["pre_class_path"] = self.class_path

    def class_file_dialog(self):
        filter_ = "(*.json)"
        file_name = QtWidgets.QFileDialog.getOpenFileName(self, 'Select File', filter=filter_)[0]
        if not file_name:
            return
        return self.set_class_table(file_name)

    def change_file(self):
        num = self.current_number - 1
        if len(self.file_list) <= num:
            self.img_size = (0, 0)
            return self.msg_box("Error", "Length Over", "warning")
        elif len(self.file_list) == 0:
            return
        self.fileListWidget.setCurrentRow(num)
        current_file_name = self.file_list[num]
        img = QtGui.QImage(current_file_name)
        pix = QtGui.QPixmap.fromImage(img)
        self.img_size = (pix.width(), pix.height())
        pix = pix.scaled(self.graphicsview_size[0], self.graphicsview_size[1])
        self.pic = QtWidgets.QGraphicsPixmapItem()
        self.pic.setPixmap(pix)
        self.graphicsView.sc = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.graphicsView.sc)
        self.graphicsView.sc.addItem(self.pic)
        self.graphicsView.fitInView(self.pic)
        self.graphicsView.initialize()
        # self.graphicsView.make_crossline()
        self.txt_is_exists(current_file_name)

    def change_window_size(self):
        pix = self.pic.pixmap().scaled(self.graphicsview_size[0], self.graphicsview_size[1])
        self.pic.setPixmap(pix)

    def save_txt_call(self):
        if self.labelPathLineEdit.text() == "":
            return self.msg_box("Error", "txt file path not specified.", "warning")
        if not self.status["auto labeling"]:
            ret = self.msg_box("Save?", "Do you want to create a txt file in the specified storage location?", "info",
                               ["yes", "no"])
            if ret == QtWidgets.QMessageBox.Yes:
                self.table_save_do()
            else:
                return
        else:
            self.table_save_do()

    def txt_is_exists(self, current_file_name):
        current_file_name = current_file_name.replace("/", "\\")
        current_file_name = current_file_name.split("\\")[-1:]
        path = os.path.join(self.labelPathLineEdit.text(), current_file_name[0][:-3] + "txt")
        if os.path.exists(path):
            with open(path, "r") as fr:
                box_list = fr.read().splitlines()
            for box in box_list:
                data = box.split(" ")
                self.graphicsView.load_txt(data)

    def table_save_do(self):
        num = self.current_number - 1
        current_file_name = self.file_list[num].replace("/", "\\")
        current_file_name = current_file_name.split("\\")[-1:]
        path = os.path.join(self.labelPathLineEdit.text(),  current_file_name[0][:-3] + "txt")
        count = self.labelTableWidget.rowCount()
        with open(path, "w") as fw:
            for i in range(count):
                label = int(self.labelTableWidget.item(i, 1).text())
                x = self.labelTableWidget.item(i, 2).text()
                y = self.labelTableWidget.item(i, 3).text()
                x_to = self.labelTableWidget.item(i, 4).text()
                y_to = self.labelTableWidget.item(i, 5).text()
                if i != count - 1:
                    line = f"{label} {x} {y} {x_to} {y_to}\n"
                else:
                    line = f"{label} {x} {y} {x_to} {y_to}"
                fw.writelines(line)

    def delete_cell(self, row, column):
        self.graphicsView.delete_box(row)
        self.labelTableWidget.removeRow(row)

    def to_delete_cell(self):
        row = self.labelTableWidget.currentRow()
        self.delete_cell(row, 0)

    def concatenate_dialog_start(self):
        start_dialog = Concatenate()
        start_dialog.exec_()

    def new_class_file_dialog_start(self):
        start_dialog = NewClassFileDialog()
        start_dialog.exec_()

    def make_dataset_dialog_start(self):
        start_dialog = MakeDataset()
        start_dialog.exec_()


class Concatenate(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        _ui = "./ui/FC.ui"
        uic.loadUi(_ui, self)
        self.file_list = []
        self.class_path = ""
        self.class_dict = {}
        self.init_fuc()
        self.show()

    def init_fuc(self):
        self.setAcceptDrops(True)
        self.function_init()
        self.setting_init()

    def function_init(self):
        self.findButton.clicked.connect(self.folderDialog)
        self.findFileButton.clicked.connect(self.open_file_dialog)
        self.findFolderButton.clicked.connect(self.open_folder_dialog)
        self.doButton.clicked.connect(self.do)
        self.cancelButton.clicked.connect(self.close)

    def setting_init(self):
        if main.class_path != "":
            self.class_path = main.class_path
            with open(self.class_path, "r") as fr:
                self.class_dict = json.load(fr)
                self.classNumberLineEdit.setText(str(len(self.class_dict)))

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        e.accept()
        urls = e.mimeData().urls()
        return self.load_file(urls)

    def folderDialog(self):
        folder_list = [QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder', )]
        return self.set_path(folder_list[0])

    def set_path(self, folder_name):
        self.pathLineEdit.setText(folder_name)

    def open_file_dialog(self):
        filter_ = "Images (*.jpg *.png)"
        file_list = QtWidgets.QFileDialog.getOpenFileNames(self, 'Select File', filter=filter_)[0]
        if not file_list:
            return
        return self.load_file(file_list)

    def open_folder_dialog(self):
        folder_list = [QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder', )]
        if folder_list == [""]:
            return
        return self.load_file(folder_list)

    def load_file(self, urls):
        file_list = []
        # 다수의 파일일 경우
        if len(urls) > 1:
            for url in urls:
                if isinstance(url, QtCore.QUrl):
                    url = url.toLocalFile()
                if self.check_file(url):
                    file_list.append(url)
                else:
                    explored_list = self.explore_folder(url)
                    file_list.extend(explored_list)
        elif len(urls) == 1:
            if isinstance(urls[0], QtCore.QUrl):
                url = urls[0].toLocalFile()
            else:
                url = urls[0]
            if self.check_file(url):
                file_list.append(url)
            else:
                explored_list = self.explore_folder(url)
                file_list.extend(explored_list)
        if len(file_list) == 0:
            main.msg_box("Error", "No Image Files", "warning")
            return
        else:
            self.file_list = file_list
            return self.path_text()

    def check_file(self, url):
        if os.path.isfile(url):
            return True
        elif os.path.isdir(url):
            return False

    def explore_folder(self, url):
        file_list = []
        for ext in ("*.jpg", "*.png"):
            path = os.path.join(url, f"**/{ext}")
            tmp_list = glob.glob(path, recursive=True)
            file_list.extend(tmp_list)
        return file_list

    def path_text(self):
        txt = ""
        for fn in self.file_list:
            txt = txt + f"\"{fn}\", "
        self.filesLineEdit.setText(txt[:-2])
        self.doButton.setEnabled(True)

    def do(self):
        if self.classLineEdit.text() == "":
            return main.msg_box("Error", "Class Name Doesn't Input ", "warning")
        if self.pathLineEdit.text() == "":
            return main.msg_box("Error", "Path Doesn't Input", "warning")
        class_name = self.classLineEdit.text()
        class_num = len(self.class_dict)
        self.class_dict[class_name] = class_num
        to_go_path = self.pathLineEdit.text()
        if os.path.exists(to_go_path):
            n = len(glob.glob(os.path.join(to_go_path, "{:04d}".format(class_num), "*")))
        else:
            n = 0
        for fn in self.file_list:
            new_name = class_name + "_" + "{:07d}.jpg".format(n)
            if not os.path.exists(os.path.join(to_go_path, "{:04d}".format(class_num))):
                os.mkdir(os.path.join(to_go_path, "{:04d}".format(class_num)))
            shutil.copy(fn, os.path.join(to_go_path, "{:04d}".format(class_num), new_name))
            n += 1
        with open(self.class_path, "w") as fw:
            json_data = json.dumps(self.class_dict)
            fw.write(json_data)
        main.set_class_table(self.class_path)
        main.msg_box("Done!", "Concat Complete!", "info")
        self.close()


class NewClassFileDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        _ui = "./ui/NCF.ui"
        uic.loadUi(_ui, self)
        self.class_path = ""
        self.class_dict = {}
        self.init_fuc()
        self.show()

    def init_fuc(self):
        self.ui_init()
        self.function_init()

    def ui_init(self):
        current_exe_path = os.path.abspath(__file__).split("\\")[:-1]
        current_exe_path = "\\".join(current_exe_path)
        current_exe_path = os.path.join(current_exe_path, "class")
        self.pathLineEdit.setText(current_exe_path)

    def function_init(self):
        self.nameLineEdit.textChanged.connect(self.check_item)
        self.classLineEdit.textChanged.connect(self.check_add)
        self.classLineEdit.returnPressed.connect(self.add_button_clicked)
        # self.listWidget.itemDoubleClicked.connect(lambda x: self.listWidget.editItem(x))
        self.searchButton.clicked.connect(self.open_folder_dialog)
        self.addButton.clicked.connect(self.add_button_clicked)
        self.addButton.setShortcut("insert")
        self.deleteButton.clicked.connect(self.delete_button_clicked)
        self.makeFileButton.clicked.connect(self.make_file_button_clicked)
        self.cancelButton.clicked.connect(self.close)
        self.cancelButton.setShortcut("esc")

    def check_add(self, txt):
        if txt == "":
            self.addButton.setEnabled(False)
        else:
            self.addButton.setEnabled(True)

    def add_button_clicked(self):
        class_name = self.classLineEdit.text()
        if class_name == "":
            return
        self.listWidget.addItem(class_name)
        self.listWidget.setCurrentRow(self.listWidget.count() - 1)
        self.check_item()

    def delete_button_clicked(self):
        row = self.listWidget.currentRow()
        item = self.listWidget.takeItem(row)
        del item
        self.check_item()

    def make_file_button_clicked(self):
        file_name = self.nameLineEdit.text()
        if not (".json" in file_name):
            file_name = file_name + ".json"
        path = os.path.join(self.pathLineEdit.text(), file_name)
        class_dict = {}
        count = self.listWidget.count()
        class_num = 0
        for i in range(count):
            class_name = self.listWidget.item(i).text()
            class_dict[class_name] = class_num
            class_num += 1
        with open(path, "w") as fw:
            fw.write(json.dumps(class_dict))
        main.msg_box("Done!", "Done!", "info")
        self.close()

    def check_item(self):
        if self.listWidget.count() > 0:
            self.deleteButton.setEnabled(True)
            if self.nameLineEdit.text() != "":
                self.makeFileButton.setEnabled(True)
        else:
            self.deleteButton.setEnabled(False)
            self.makeFileButton.setEnabled(False)

    def open_folder_dialog(self):
        folder_list = [QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder', )]
        if folder_list == [""]:
            return
        return self.pathLineEdit.setText(folder_list[0])


class newGraphicView(QtWidgets.QGraphicsView):
    def __init__(self):
        super().__init__()
        self.setMinimumWidth(512)
        self.setMinimumHeight(288)
        self.setMouseTracking(True)
        self.sc = self.scene()
        self.rect_draw = []
        self.id_ = {}
        self.current_pen_thick = 2
        self.current_color_num = 0
        self.pen_color = [QtCore.Qt.red, QtCore.Qt.blue, QtCore.Qt.green, QtCore.Qt.yellow, QtCore.Qt.black,
                          QtCore.Qt.darkRed, QtCore.Qt.darkBlue, QtCore.Qt.darkGreen, QtCore.Qt.darkYellow,
                          QtCore.Qt.darkGray]
        self.start = QtCore.QPointF()
        self.end = QtCore.QPointF()
        self.boxing = True
        self.img_in = False

    def mousePressEvent(self, e):
        if not self.img_in:
            pass
        elif e.button() == QtCore.Qt.LeftButton and self.boxing:
            self.start = self.mapToScene(e.pos())
            self.end = self.mapToScene(e.pos())
            self.boxing = False
        elif e.button() == QtCore.Qt.LeftButton and (not self.boxing):
            rect = QtCore.QRectF(self.start, self.end)
            pre_item = self.rect_draw[0]
            self.sc.removeItem(pre_item)
            del pre_item
            self.rect_draw.clear()
            self.boxing_data_table_in(rect)
            self.boxing = True

    def mouseMoveEvent(self, e):
        mode = main.status["save values"]
        img_size = main.img_size
        view_size = (main.graphicsView.width(), main.graphicsView.height())
        point = e.pos()
        if mode == "a":
            if (img_size[0] == 0) or (img_size[0] == 0):
                txt = "X: {}, Y: {}".format(e.x(), e.y())
            else:
                x = round((point.x() / view_size[0]) * img_size[0])
                y = round((point.y() / view_size[1]) * img_size[1])
                txt = "X: {}, Y: {}".format(x, y)
        else:
            if (img_size[0] == 0) or (img_size[0] == 0):
                x = point.x() / view_size[0]
                y = point.y() / view_size[1]
                txt = "X: {:.5f}, Y: {:.5f}".format(x, y)
            else:
                x = round((point.x() / view_size[0]), 5)
                y = round((point.y() / view_size[1]), 5)
                txt = "X: {:.5f}, Y: {:.5f}".format(x, y)
        main.statusbar.showMessage(txt)
        # mouse_point = self.mapToScene(e.pos())
        # self.x_line.setLine(0, mouse_point.y(), self.x_line.x2(), mouse_point.y())
        # self.y_line.setLine(mouse_point.x(), 0, mouse_point.x(), self.y_line.y2())
        if not self.boxing:
            self.end = self.mapToScene(e.pos())
            rect = QtCore.QRectF(self.start, self.end)
            if len(self.rect_draw) > 0:
                r = self.rect_draw.pop(0)
                self.sc.removeItem(r)
                del r
            self.rect_draw.append(self.sc.addRect(rect, QtGui.QPen(self.pen_color[self.current_color_num],
                                                                   self.current_pen_thick)))
        if len(main.file_list) > 0:
            self.sc.update()

    def boxing_data_table_in(self, rect):
        x, y, x_to, y_to = rect.x(), rect.y(), rect.x() + rect.width(), rect.y() + rect.height()
        if x > x_to:
            tmp = x
            x = x_to
            x_to = tmp
        if y > y_to:
            tmp = y
            y = y_to
            y_to = tmp
        if main.class_num == -1:
            main.msg_box("Error", "No Have Class Data", "warning")
            del rect
        else:
            self.id_[len(self.id_) + 1] = self.sc.addRect(rect, QtGui.QPen(self.pen_color[self.current_color_num],
                                                                           self.current_pen_thick))
            self.color_num_func()
            self.write_cell(x, y, x_to, y_to)

    def write_cell(self, x, y, x_to, y_to):
        x, x_to = x / self.sc.width(), x_to / self.sc.width()
        y, y_to = y / self.sc.height(), y_to / self.sc.height()
        cell_count = main.labelTableWidget.rowCount()
        main.labelTableWidget.setRowCount(cell_count + 1)
        label = main.classTableWidget.item(main.class_num, 2).text()
        main.labelTableWidget.setItem(cell_count, 0, QtWidgets.QTableWidgetItem(str(cell_count + 1)))
        main.labelTableWidget.setItem(cell_count, 1, QtWidgets.QTableWidgetItem(label))
        if main.status["save values"] == "a":
            main.labelTableWidget.setItem(cell_count, 2, QtWidgets.QTableWidgetItem(str(round(x * main.img_size[0]))))
            main.labelTableWidget.setItem(cell_count, 3, QtWidgets.QTableWidgetItem(str(round(y * main.img_size[1]))))
            main.labelTableWidget.setItem(cell_count, 4, QtWidgets.QTableWidgetItem(str(round(x_to * main.img_size[0]))))
            main.labelTableWidget.setItem(cell_count, 5, QtWidgets.QTableWidgetItem(str(round(y_to * main.img_size[1]))))
        else:
            main.labelTableWidget.setItem(cell_count, 2, QtWidgets.QTableWidgetItem(str(round(x, 5))))
            main.labelTableWidget.setItem(cell_count, 3, QtWidgets.QTableWidgetItem(str(round(y, 5))))
            main.labelTableWidget.setItem(cell_count, 4, QtWidgets.QTableWidgetItem(str(round(x_to, 5))))
            main.labelTableWidget.setItem(cell_count, 5, QtWidgets.QTableWidgetItem(str(round(y_to, 5))))

    def color_num_func(self):
        self.current_color_num += 1
        if self.current_color_num > 9:
            self.current_color_num = 0

    def initialize(self):
        self.id_ = {}
        self.current_color_num = 0
        self.img_in = True
        main.labelTableWidget.clearContents()
        main.labelTableWidget.setRowCount(0)

    def delete_box(self, row):
        del_id = int(main.labelTableWidget.item(row, 0).text())
        del_item = self.id_[del_id]
        self.sc.removeItem(del_item)
        del del_item
        del(self.id_[del_id])
        self.sc.update()

    def load_txt(self, data):
        label, x, y, x_to, y_to = data
        cell_count = main.labelTableWidget.rowCount()
        main.labelTableWidget.setRowCount(cell_count + 1)
        main.labelTableWidget.setItem(cell_count, 0, QtWidgets.QTableWidgetItem(str(cell_count + 1)))
        main.labelTableWidget.setItem(cell_count, 1, QtWidgets.QTableWidgetItem(label))
        main.labelTableWidget.setItem(cell_count, 2, QtWidgets.QTableWidgetItem(x))
        main.labelTableWidget.setItem(cell_count, 3, QtWidgets.QTableWidgetItem(y))
        main.labelTableWidget.setItem(cell_count, 4, QtWidgets.QTableWidgetItem(x_to))
        main.labelTableWidget.setItem(cell_count, 5, QtWidgets.QTableWidgetItem(y_to))
        if "." in x:
            width, height = (main.graphicsView.width(), main.graphicsView.height())
            x, x_to, y, y_to = round(float(x) * width), round((float(x_to) - float(x)) * width), \
                               round(float(y) * height), round((float(y_to) - float(y)) * height)
            rect = QtCore.QRectF(x, y, x_to, y_to)
            self.id_[len(self.id_) + 1] = self.sc.addRect(rect, QtGui.QPen(self.pen_color[self.current_color_num],
                                                                           self.current_pen_thick))
            self.color_num_func()
        else:
            width, height = (main.graphicsView.width(), main.graphicsView.height())
            img_w, img_h = main.img_size
            x, y, x_to, y_to = int(x) / img_w, int(y) / img_h, int(x_to) / img_w, int(y_to) / img_h
            x, x_to, y, y_to = round(float(x) * width), round((float(x_to) - float(x)) * width), \
                               round(float(y) * height), round((float(y_to) - float(y)) * height)
            rect = QtCore.QRectF(x, y, x_to, y_to)
            self.id_[len(self.id_) + 1] = self.sc.addRect(rect, QtGui.QPen(self.pen_color[self.current_color_num],
                                                                           self.current_pen_thick))
            self.color_num_func()

    def make_crossline(self):
        width, height = (main.graphicsView.width(), main.graphicsView.height())
        self.x_line = QtCore.QLineF(0, 0, width, 0)
        self.y_line = QtCore.QLineF(0, 0, 0, height)
        self.sc.addLine(self.x_line, QtGui.QPen(QtCore.Qt.black, 2))
        self.sc.addLine(self.y_line, QtGui.QPen(QtCore.Qt.black, 2))


class MakeDataset(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        _ui = "./ui/MD.ui"
        uic.loadUi(_ui, self)
        self.rel = True
        self.file_list = []
        self.init_fuc()
        self.show()

    def init_fuc(self):
        self.setting_init()
        self.function_init()

    def setting_init(self):
        if not os.path.exists("./dataset"):
            os.mkdir("./dataset")

    def function_init(self):
        self.labelLineEdit.textChanged.connect(self.check_path)
        self.labelSearchButton.clicked.connect(self.label_folder_dialog)
        self.imageLineEdit.textChanged.connect(self.check_path)
        self.imageSearchButton.clicked.connect(self.image_folder_dialog)
        self.doButton.clicked.connect(self.do_button_clicked)
        self.cancelButton.clicked.connect(self.close)
        self.cancelButton.setShortcut("esc")

    def do_button_clicked(self):
        self.rel = self.check_radio_button()
        image_path = self.imageLineEdit.text()
        label_name = image_path.split("/")[-1]
        label_path = self.labelLineEdit.text()
        dataset_folder_path = os.path.join(".", "dataset", label_name)
        if not os.path.exists(dataset_folder_path):
            os.mkdir(dataset_folder_path)
        if not os.path.exists(os.path.join(dataset_folder_path, "images")):
            os.mkdir(os.path.join(dataset_folder_path, "images"))
        if not os.path.exists(os.path.join(dataset_folder_path, "labels")):
            os.mkdir(os.path.join(dataset_folder_path, "labels"))
        self.file_list = glob.glob(os.path.join(label_path, "*.txt"))
        if len(self.file_list) == 0:
            main.msg_box("Error", "Wrong Path", "warning")
        self.progressBar.setMaximum(len(self.file_list))
        n = 0
        for fn in self.file_list:
            self.file_transform_func(fn, image_path, dataset_folder_path)
            n += 1
            self.progressBar.setValue(n)
        main.msg_box("Done!", "Done!", "info")

    def check_radio_button(self):
        if self.absRadioButton.isChecked():
            return False
        else:
            return True

    def file_transform_func(self, label_file_path, image_path, new_path):
        file_name = label_file_path.split("\\")[-1][:-3]
        img_file_path = os.path.join(image_path, file_name + "jpg")
        if not os.path.exists(img_file_path):
            return
        file_size = Image.open(img_file_path).size
        with open(label_file_path, "r") as fr:
            label_list = fr.read().splitlines()
        if len(label_list) == 0:
            return
        if self.check_file_is_label(label_list[0]):
            with open(os.path.join(new_path, "labels", file_name + "txt"), "w") as fw:
                new_labels = self.doing_labeling(label_list, file_size)
                fw.write(new_labels)
                shutil.copy(img_file_path, os.path.join(new_path, "images", file_name + "jpg"))
        else:
            return

    def doing_labeling(self, label_list, size):
        all_label = ""
        for line in label_list:
            if not (self.abs_or_rel_check(line)) and self.rel:
                data = line.split(" ")
                x = int(data[1]) / size[0]
                y = int(data[2]) / size[1]
                x_to = int(data[3]) / size[0]
                y_to = int(data[4]) / size[1]
                new_data = f"{data[0]} {x} {y} {x_to} {y_to}\n"
                all_label = all_label + new_data
            elif self.abs_or_rel_check(line) and not self.rel:
                data = line.split(" ")
                data = self.check_over_size(data, size)
                x = float(data[1]) * size[0]
                y = float(data[2]) * size[1]
                x_to = float(data[3]) * size[0]
                y_to = float(data[4]) * size[1]
                new_data = f"{data[0]} {x} {y} {x_to} {y_to}\n"
                all_label = all_label + new_data
            else:
                all_label = all_label + line + "\n"
        return all_label[:-2]

    def check_over_size(self, data, size):
        if data[1] < 0:
            data[1] = 0
        if data[3] < 0:
            data[2] = 0
        if data[3] > size[0]:
            data[3] = size[0]
        if data[4] > size[1]:
            data[4] = size[1]
        return data

    def check_file_is_label(self, label):
        label_code = label.split(" ")
        if len(label_code) == 5:
            try:
                int(label_code[0])
                return True
            except:
                return False
        else:
            return False

    def abs_or_rel_check(self, line):
        if "." in line:
            return True
        else:
            return False

    def check_path(self):
        if self.imageLineEdit.text() != "" and self.labelLineEdit.text() != "":
            self.doButton.setEnabled(True)
        else:
            self.doButton.setEnabled(False)

    def image_folder_dialog(self):
        folder_list = [QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder', )]
        if folder_list == [""]:
            return
        return self.imageLineEdit.setText(folder_list[0])

    def label_folder_dialog(self):
        folder_list = [QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder', )]
        if folder_list == [""]:
            return
        return self.labelLineEdit.setText(folder_list[0])


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())
