# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui, uic
import sys, ui_window

class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = ui_window.Ui_Enigma()
        self.ui.setupUi(self)

        self.file = open('conf.config')
        self.spp = []
        self.symbols(0)
        self.ui.spinBox_quantity_symbol.setProperty('value', 2)

        for ex in self.file.readlines():
            self.spp.append(ex)
            #print(self.spp)

        QtCore.QObject.connect(self.ui.pushButton_save, QtCore.SIGNAL("clicked()"), self.create_file)
        QtCore.QObject.connect(self.ui.spinBox_quantity_symbol, QtCore.SIGNAL("valueChanged(int)"), self.lokomotiv)
        QtCore.QObject.connect(self.ui.comboBox_lang, QtCore.SIGNAL("currentIndexChanged(int)"), self.symbols)
        QtCore.QObject.connect(self.ui.pushButton_encrypt, QtCore.SIGNAL("clicked()"), self.encrypt)
        QtCore.QObject.connect(self.ui.pushButton_decrypt, QtCore.SIGNAL("clicked()"), self.decrypt)

    '''Quantity symbol'''
    def lokomotiv(self, value):
        value = self.ui.spinBox_quantity_symbol.value()

        self.ui.lineEdit_num_0.setMaxLength(int(value))
        self.ui.lineEdit_num_1.setMaxLength(int(value))
        self.ui.lineEdit_num_2.setMaxLength(int(value))
        self.ui.lineEdit_num_3.setMaxLength(int(value))
        self.ui.lineEdit_num_4.setMaxLength(int(value))
        self.ui.lineEdit_num_5.setMaxLength(int(value))
        self.ui.lineEdit_num_6.setMaxLength(int(value))
        self.ui.lineEdit_num_7.setMaxLength(int(value))
        self.ui.lineEdit_num_8.setMaxLength(int(value))
        self.ui.lineEdit_num_9.setMaxLength(int(value))

        self.ui.lineEdit_0.setMaxLength(int(value))
        self.ui.lineEdit_1.setMaxLength(int(value))
        self.ui.lineEdit_2.setMaxLength(int(value))
        self.ui.lineEdit_3.setMaxLength(int(value))
        self.ui.lineEdit_4.setMaxLength(int(value))
        self.ui.lineEdit_5.setMaxLength(int(value))
        self.ui.lineEdit_6.setMaxLength(int(value))
        self.ui.lineEdit_7.setMaxLength(int(value))
        self.ui.lineEdit_8.setMaxLength(int(value))
        self.ui.lineEdit_9.setMaxLength(int(value))
        self.ui.lineEdit_10.setMaxLength(int(value))
        self.ui.lineEdit_11.setMaxLength(int(value))
        self.ui.lineEdit_12.setMaxLength(int(value))
        self.ui.lineEdit_13.setMaxLength(int(value))
        self.ui.lineEdit_14.setMaxLength(int(value))
        self.ui.lineEdit_15.setMaxLength(int(value))
        self.ui.lineEdit_16.setMaxLength(int(value))
        self.ui.lineEdit_17.setMaxLength(int(value))
        self.ui.lineEdit_18.setMaxLength(int(value))
        self.ui.lineEdit_19.setMaxLength(int(value))
        self.ui.lineEdit_20.setMaxLength(int(value))
        self.ui.lineEdit_21.setMaxLength(int(value))
        self.ui.lineEdit_22.setMaxLength(int(value))
        self.ui.lineEdit_23.setMaxLength(int(value))
        self.ui.lineEdit_24.setMaxLength(int(value))
        self.ui.lineEdit_25.setMaxLength(int(value))
        self.ui.lineEdit_26.setMaxLength(int(value))
        self.ui.lineEdit_27.setMaxLength(int(value))
        self.ui.lineEdit_28.setMaxLength(int(value))
        self.ui.lineEdit_29.setMaxLength(int(value))
        self.ui.lineEdit_30.setMaxLength(int(value))
        self.ui.lineEdit_31.setMaxLength(int(value))
        self.ui.lineEdit_32.setMaxLength(int(value))

        self.ui.lineEdit_sym_0.setMaxLength(int(value))
        self.ui.lineEdit_sym_1.setMaxLength(int(value))
        self.ui.lineEdit_sym_2.setMaxLength(int(value))
        self.ui.lineEdit_sym_3.setMaxLength(int(value))
        self.ui.lineEdit_sym_4.setMaxLength(int(value))
        self.ui.lineEdit_sym_5.setMaxLength(int(value))
        self.ui.lineEdit_sym_6.setMaxLength(int(value))
        self.ui.lineEdit_sym_7.setMaxLength(int(value))
        self.ui.lineEdit_sym_8.setMaxLength(int(value))
        self.ui.lineEdit_sym_9.setMaxLength(int(value))

    '''Create file'''
    def create_file(self):
        #self.emit = QtGui.QFileDialog.getSaveFileName(parent = None)
        self.k = []
        n = [self.ui.lineEdit_num_0.text(),
             self.ui.lineEdit_num_1.text(),
             self.ui.lineEdit_num_2.text(),
             self.ui.lineEdit_num_3.text(),
             self.ui.lineEdit_num_4.text(),
             self.ui.lineEdit_num_5.text(),
             self.ui.lineEdit_num_6.text(),
             self.ui.lineEdit_num_7.text(),
             self.ui.lineEdit_num_8.text(),
             self.ui.lineEdit_num_9.text()]

        b = [self.ui.lineEdit_0.text(),self.ui.lineEdit_1.text(),self.ui.lineEdit_2.text(),self.ui.lineEdit_3.text(),
             self.ui.lineEdit_4.text(),self.ui.lineEdit_5.text(),self.ui.lineEdit_6.text(),self.ui.lineEdit_7.text(),
             self.ui.lineEdit_8.text(),self.ui.lineEdit_9.text(),self.ui.lineEdit_10.text(),self.ui.lineEdit_11.text(),
             self.ui.lineEdit_12.text(),self.ui.lineEdit_13.text(),self.ui.lineEdit_14.text(),self.ui.lineEdit_15.text(),
             self.ui.lineEdit_16.text(),self.ui.lineEdit_17.text(),self.ui.lineEdit_18.text(),self.ui.lineEdit_19.text(),
             self.ui.lineEdit_20.text(),self.ui.lineEdit_21.text(),self.ui.lineEdit_22.text(),self.ui.lineEdit_23.text(),
             self.ui.lineEdit_24.text(),self.ui.lineEdit_25.text(),self.ui.lineEdit_26.text(),self.ui.lineEdit_27.text(),
             self.ui.lineEdit_28.text(),self.ui.lineEdit_29.text(),self.ui.lineEdit_30.text(),self.ui.lineEdit_31.text(),
             self.ui.lineEdit_32.text()]

        s = [self.ui.lineEdit_sym_0.text(),self.ui.lineEdit_sym_1.text(),self.ui.lineEdit_sym_2.text(),self.ui.lineEdit_sym_3.text(),self.ui.lineEdit_sym_4.text(),
             self.ui.lineEdit_sym_5.text(),self.ui.lineEdit_sym_6.text(),self.ui.lineEdit_sym_7.text(),self.ui.lineEdit_sym_8.text(),self.ui.lineEdit_sym_9.text()]

        for bi in b:
            self.k.append(bi)
        for ni in n:
            self.k.append(ni)
        for si in s:
            self.k.append(si)

        self.SaveSetings(self.k)

    def symbols(self, option):
        option = self.ui.comboBox_lang.currentIndex()
        if option == 0:
            print('UA')
            symbol_ua = [u'а', u'б', u'в', u'г', u'ґ', u'д', u'е', u'є', u'ж', u'з', u'и', u'і', u'ї', u'й', u'к', u'л',
                         u'м', u'н', u'о', u'п', u'р', u'с', u'т', u'у', u'ф', u'х', u'ц', u'ч', u'ш', u'щ', u'ь', u'ю',
                         u'я', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '!', '?', ',', '.', ':', ';',
                         '(', ')', '@', "'", '\n']
            self.symbol = symbol_ua
        elif option == 1:
            print('EU')
            symbol_en = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                         'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                         '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '!', '?', ',', '.', ':', ';', '(', ')', '@', "'", '\n']
            self.symbol = symbol_en
        elif option == 2:
            print('RU')
            symbol_ru = []
            self.symbol = symbol_ru

    def encrypt(self):
        lst = []
        file = open('conf.config')
        text_encrypt = self.ui.textEdit_input_encrypt.toPlainText()
        if not text_encrypt:
            self.ui.textEdit_input_encrypt.setStyleSheet("color: rgb(255, 0, 255);")
            self.ui.textEdit_input_encrypt.setPlainText('Error: Введите текст!')
        else:
            for line in file.readlines():
                lst.append(line)

        '''Шифрование текста'''
        o_lst = []
        for i in text_encrypt.lower():
            for z in range(0, len(self.symbol)):
                for l in self.symbol[z]:
                    if i == l:
                        o_lst.append(lst[z])
        str_f = ''.join(o_lst).split()
        '''Конец шифрования текста'''

        '''Вывод шифрованого текста'''
        self.ui.textEdit_output_encrypt.setPlainText(''.join(str_f))
        '''Конец вывода шифрованого текста'''

    def decrypt(self):
        self.text_decrypt = self.ui.textEdit_input_decrypt.toPlainText()
        if not self.text_decrypt:
            self.ui.textEdit_input_decrypt.setStyleSheet("color: rgb(255, 0, 255);")
            self.ui.textEdit_input_decrypt.setPlainText('Error: Введите текст!')
        else:

            self.bro = ''.join(self.spp).split()
            t =[]

            for j in [self.text_decrypt.lower()[i:i+self.ui.spinBox_quantity_symbol.value()] for i in range(0, len(self.text_decrypt), self.ui.spinBox_quantity_symbol.value())]:
                for z in range(len(self.symbol)):
                    for l in self.bro[z:z+1]:
                        if j == l:
                            t.append(self.symbol[z])


            self.ui.textEdit_output_decrypt.setPlainText(''.join(t))

    ''' Save settings to file '''
    def SaveSetings(self, k):
        f = open('.config', "w", encoding="utf-8")
        for z in k:
            f.write(str("%s\n" % z))
        f.close()
        return

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())