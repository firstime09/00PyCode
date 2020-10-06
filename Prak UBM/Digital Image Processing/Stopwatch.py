from tkinter import *
import time

class Stopwatch(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self._start = 0.0
        self.waktuSekarang = 0.0
        self.sedangBerjalan = False
        self.waktuString = StringVar()
        self.textStart = StringVar()
        self.textStart.set('Start')
        parent.configure(background = 'light blue')
        parent.title('StopWatch')
        self.buatTeks()
        self.buatKolom()
        self.buatTombol()
        self.posisi = 1

    def buatTeks(self):
        self.teks = Label(self, textvariable = self.waktuString,
                          font = "Verdana 19 bold", bg = 'light blue',
                          fg = 'blue')
        self.aturWaktu(self.waktuSekarang)
        self.teks.grid(row = 0, column = 0)

    def perbarui(self):
        self.waktuSekarang = time.time() - self._start
        self.aturWaktu(self.waktuSekarang)
        self._timer = self.after(50, self.perbarui)

    def aturWaktu(self, waktu):
        menit = int(waktu / 60)
        detik = int(waktu - menit*60.0)
        jam = int((waktu - menit*60 - detik)*100)
        self.waktuString.set('%02d:%02d:%02d' % (menit, detik, jam))

    def Start(self):
        if not self.sedangBerjalan and self.textStart.get() == 'Start':
            self.textStart.set('Cetak')
            self._start = time.time() - self.waktuSekarang
            self.perbarui()
            self.sedangBerjalan = True
        elif self.sedangBerjalan and self.textStart.get() == 'Cetak':
            self.kolom.insert(END, str(self.posisi)+"."+self.waktuString.get()+"<>")
            self.posisi+=1

    def pause(self):
        if self.sedangBerjalan:
            self.textStart.set('Start')
            self.after_cancel(self._timer)
            self.waktuSekarang = time.time() - self._start
            self.aturWaktu(self.waktuSekarang)
            self.sedangBerjalan = False

    def Reset(self):
        self._start = time.time()
        self.waktuSekarang = 0.0
        self.aturWaktu(self.waktuSekarang)
        self.kolom.delete('0', END)

    def buatKolom(self):
        self.kolom = Entry(bg='blue', fg='white')
        self.kolom.grid(row = 1, column = 0, columnspan = 4, pady = 4)

    def buatTombol(self):
        Button(textvariable=self.textStart, command=self.Start).grid(row=2, column=0)
        Button(text='Pause', command=self.pause).grid(row=2, column=1)
        Button(text='Reset', command=self.Reset).grid(row=2, column=2)
        Button(text='Quit', command=self.quit).grid(row=2, column=3)

def main():
    root = Tk()
    sw = Stopwatch(root)
    sw.grid(row=0, column=0, columnspan=4)
    root.mainloop()

if __name__ == '__main__':
    main()