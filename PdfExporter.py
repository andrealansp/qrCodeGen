from fpdf import FPDF


class PDF(FPDF):
    def recebeDados(self, nomes):
        self.nomes = nomes

    def draw_line(self):
        self.line(0.8, 0.8, 49.2, 0.8)
        self.line(0.8, 0.8, 0.8, 29.2)
        self.line(0.8, 29.2, 49.2, 29.2)
        self.line(49.2, 29.2, 49.2, 0.8)

    def add_qrcode(self):
        for i in self.nomes:
            self.add_page()
            self.draw_line()
            self.text(1, 29, i[0].upper())
            self.image(i[1], 3, 10, 10, 10, 'PNG')
            self.image(i[1], (3*6), 10, 10, 10, 'PNG')
            self.image(i[1], (3*11), 10, 10, 10, 'PNG')
