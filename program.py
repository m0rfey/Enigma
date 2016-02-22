# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui, uic
import os, sys, ui_window

class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = ui_window.Ui_Enigma()
        self.ui.setupUi(self)

        self.directory =os.path.dirname('config/')
        self.name_file ='.config'

        self.file = open(self.directory +'/'+ self.name_file)
        self.spp = []

        default_lang = 0
        default_len = 2

        self.lokomotiv(default_len)

        self.option = default_lang
        self.symbols(default_lang)
        self.ui.spinBox_quantity_symbol.setProperty('value', 0)
        for ex in self.file.readlines():
            self.spp.append(ex)

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
            if not bi:
                pass
            else:
                self.k.append(bi)
        for ni in n:
            if not ni:
                pass
            else:
                self.k.append(ni)
        for si in s:
            if not si:
                pass
            else:
                self.k.append(si)

        self.SaveSetings(self.k)

    def symbols(self, option):
        self.option = self.ui.comboBox_lang.currentIndex()

        if self.option == 0:
            self.name_lan= 'ua'
            print('UA')
            symbol_ua = ['а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л',
                         'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю',
                         'я', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '!', '?', ',', '.', ':', ';',
                         '(', ')', '@', "'", '\n']
            self.symbol = symbol_ua

            self.ui.lineEdit_26.setDisabled(False)
            self.ui.lineEdit_27.setDisabled(False)
            self.ui.lineEdit_28.setDisabled(False)
            self.ui.lineEdit_29.setDisabled(False)
            self.ui.lineEdit_30.setDisabled(False)
            self.ui.lineEdit_31.setDisabled(False)
            self.ui.lineEdit_32.setDisabled(False)

            self.ui.label_0.setText((symbol_ua[0]+':').upper()),self.ui.label_1.setText((symbol_ua[1]+':').upper())
            self.ui.label_2.setText((symbol_ua[2]+':').upper()),self.ui.label_3.setText((symbol_ua[3]+':').upper())
            self.ui.label_4.setText((symbol_ua[4]+':').upper()),self.ui.label_5.setText((symbol_ua[5]+':').upper())
            self.ui.label_6.setText((symbol_ua[6]+':').upper()),self.ui.label_7.setText((symbol_ua[7]+':').upper())
            self.ui.label_8.setText((symbol_ua[8]+':').upper()),self.ui.label_9.setText((symbol_ua[9]+':').upper())
            self.ui.label_10.setText((symbol_ua[10]+':').upper()),self.ui.label_11.setText((symbol_ua[11]+':').upper())
            self.ui.label_12.setText((symbol_ua[12]+':').upper()),self.ui.label_13.setText((symbol_ua[13]+':').upper())
            self.ui.label_14.setText((symbol_ua[14]+':').upper()),self.ui.label_15.setText((symbol_ua[15]+':').upper())
            self.ui.label_16.setText((symbol_ua[16]+':').upper()),self.ui.label_17.setText((symbol_ua[17]+':').upper())
            self.ui.label_18.setText((symbol_ua[18]+':').upper()),self.ui.label_19.setText((symbol_ua[19]+':').upper())
            self.ui.label_20.setText((symbol_ua[20]+':').upper()), self.ui.label_21.setText((symbol_ua[21]+':').upper())
            self.ui.label_22.setText((symbol_ua[22]+':').upper()),self.ui.label_23.setText((symbol_ua[23]+':').upper())
            self.ui.label_24.setText((symbol_ua[24]+':').upper()),self.ui.label_25.setText((symbol_ua[25]+':').upper())
            self.ui.label_26.setText((symbol_ua[26]+':').upper()),self.ui.label_27.setText((symbol_ua[27]+':').upper())
            self.ui.label_28.setText((symbol_ua[28]+':').upper()),self.ui.label_29.setText((symbol_ua[29]+':').upper())
            self.ui.label_30.setText((symbol_ua[30]+':').upper()),self.ui.label_31.setText((symbol_ua[31]+':').upper())
            self.ui.label_32.setText((symbol_ua[32]+':').upper()),self.ui.label_num_0.setText(symbol_ua[33]+':')
            self.ui.label_num_1.setText(symbol_ua[34]+':'),self.ui.label_num_2.setText(symbol_ua[35]+':')
            self.ui.label_num_3.setText(symbol_ua[36]+':'),self.ui.label_num_4.setText(symbol_ua[37]+':')
            self.ui.label_num_5.setText(symbol_ua[38]+':'),self.ui.label_num_6.setText(symbol_ua[39]+':')
            self.ui.label_num_7.setText(symbol_ua[40]+':'),self.ui.label_num_8.setText(symbol_ua[41]+':')
            self.ui.label_num_9.setText(symbol_ua[42]+':'),self.ui.label_sym_0.setText(symbol_ua[43]+':')
            self.ui.label_sym_1.setText(symbol_ua[44]+':'),self.ui.label_sym_2.setText(symbol_ua[45]+':')
            self.ui.label_sym_3.setText(symbol_ua[46]+':'),self.ui.label_sym_4.setText(symbol_ua[47]+':')
            self.ui.label_sym_5.setText(symbol_ua[48]+':'),self.ui.label_sym_6.setText(symbol_ua[49]+':')
            self.ui.label_sym_7.setText(symbol_ua[50]+':'),self.ui.label_sym_8.setText(symbol_ua[51]+':')
            self.ui.label_sym_9.setText(symbol_ua[52]+':'),self.ui.label_sym_10.setText(symbol_ua[53]+':')
            self.ui.label_sym_11.setText('/n:')

        elif self.option == 1:
            self.name_lan = 'en'
            print('EU')
            symbol_en = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                         'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                         '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '!', '?', ',', '.', ':', ';', '(', ')', '@', "'", '\n']
            self.symbol = symbol_en

            self.ui.label_26.setText(''),self.ui.label_27.setText('')
            self.ui.label_28.setText(''),self.ui.label_29.setText('')
            self.ui.label_30.setText(''),self.ui.label_31.setText('')
            self.ui.label_32.setText(''),self.ui.lineEdit_26.setDisabled(True)
            self.ui.lineEdit_27.setDisabled(True),self.ui.lineEdit_28.setDisabled(True)
            self.ui.lineEdit_29.setDisabled(True),self.ui.lineEdit_30.setDisabled(True)
            self.ui.lineEdit_31.setDisabled(True),self.ui.lineEdit_32.setDisabled(True)

            self.ui.label_0.setText((symbol_en[0]+':').upper()),self.ui.label_1.setText((symbol_en[1]+':').upper())
            self.ui.label_2.setText((symbol_en[2]+':').upper()),self.ui.label_3.setText((symbol_en[3]+':').upper())
            self.ui.label_4.setText((symbol_en[4]+':').upper()),self.ui.label_5.setText((symbol_en[5]+':').upper())
            self.ui.label_6.setText((symbol_en[6]+':').upper()),self.ui.label_7.setText((symbol_en[7]+':').upper())
            self.ui.label_8.setText((symbol_en[8]+':').upper()),self.ui.label_9.setText((symbol_en[9]+':').upper())
            self.ui.label_10.setText((symbol_en[10]+':').upper()),self.ui.label_11.setText((symbol_en[11]+':').upper())
            self.ui.label_12.setText((symbol_en[12]+':').upper()),self.ui.label_13.setText((symbol_en[13]+':').upper())
            self.ui.label_14.setText((symbol_en[14]+':').upper()),self.ui.label_15.setText((symbol_en[15]+':').upper())
            self.ui.label_16.setText((symbol_en[16]+':').upper()),self.ui.label_17.setText((symbol_en[17]+':').upper())
            self.ui.label_18.setText((symbol_en[18]+':').upper()),self.ui.label_19.setText((symbol_en[19]+':').upper())
            self.ui.label_20.setText((symbol_en[20]+':').upper()),self.ui.label_21.setText((symbol_en[21]+':').upper())
            self.ui.label_22.setText((symbol_en[22]+':').upper()),self.ui.label_23.setText((symbol_en[23]+':').upper())
            self.ui.label_24.setText((symbol_en[24]+':').upper()),self.ui.label_25.setText((symbol_en[25]+':').upper())
            self.ui.label_num_0.setText(symbol_en[26]+':'),self.ui.label_num_1.setText(symbol_en[27]+':')
            self.ui.label_num_2.setText(symbol_en[28]+':'),self.ui.label_num_3.setText(symbol_en[29]+':')
            self.ui.label_num_4.setText(symbol_en[30]+':'),self.ui.label_num_5.setText(symbol_en[31]+':')
            self.ui.label_num_6.setText(symbol_en[32]+':'),self.ui.label_num_7.setText(symbol_en[33]+':')
            self.ui.label_num_8.setText(symbol_en[34]+':'),self.ui.label_num_9.setText(symbol_en[35]+':')
            self.ui.label_sym_0.setText(symbol_en[36]+':'),self.ui.label_sym_1.setText(symbol_en[37]+':')
            self.ui.label_sym_2.setText(symbol_en[38]+':'),self.ui.label_sym_3.setText(symbol_en[39]+':')
            self.ui.label_sym_4.setText(symbol_en[40]+':'),self.ui.label_sym_5.setText(symbol_en[41]+':')
            self.ui.label_sym_6.setText(symbol_en[42]+':'),self.ui.label_sym_7.setText(symbol_en[43]+':')
            self.ui.label_sym_8.setText(symbol_en[44]+':'),self.ui.label_sym_9.setText(symbol_en[45]+':')
            self.ui.label_sym_10.setText(symbol_en[46]+':'),self.ui.label_sym_11.setText('/n:')

        elif self.option == 2:
            self.name_lan = 'ru'
            print('RU')
            symbol_ru = []
            self.symbol = symbol_ru

    def encrypt(self):
        lst = []
        file = open(self.directory +'/'+self.name_lan+ self.name_file)
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
        if self.option == 0:
            f = open(self.directory +'/'+ 'ua' + self.name_file, "w")#, encoding="utf-8")
            for z in k:
                f.write(str("%s\n" % z))
            f.close()
        elif self.option == 1:
            f = open(self.directory +'/'+ 'en' + self.name_file, "w")#, encoding="utf-8")
            for z in k:
                f.write(str("%s\n" % z))
            f.close()
        elif self.option == 2:
            f = open(self.directory +'/'+ 'ru' + self.name_file, "w")#, encoding="utf-8")
            for z in k:
                f.write(str("%s\n" % z))
            f.close()
        return

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())