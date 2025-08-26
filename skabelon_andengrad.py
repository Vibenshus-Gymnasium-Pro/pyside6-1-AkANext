# [[file:Grafisk_andengradsligningsloeser.org::*Skabelon][Skabelon:1]]
import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QPushButton,
    QLineEdit,
    QDoubleSpinBox,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    # Tilføj eller fjern selv flere widgets, hvis I vil/ikke vil bruge dem. F.eks. forskellige layouts
)


def reelle_loesninger_til_andengradsligning(a, b, c):
    """Denne funktion modtager a, b og c-koefficienterne til en andengradsligning sat op på standardform som argumenter og returnerer de reelle løsninger."""
    # Overvej hvad funktionen skal returnere, naar der er hhv 0, 1 eller 2 loesninger
    # Skal funktionen returnere faktiske vaerdier, eller bare en tekststreng?
    pass


class HovedVindue(QMainWindow):
    def __init__(self):
        super().__init__()
        self.opsaetning()

    def opsaetning(self):
        self.setWindowTitle("Andengradsligningsløser")
        # Herunder skal oprette de noedvendige widgets
        # og soerge for at saette dem op i et ordentligt layout.
        # Herunder skal I saette jeres signaler og slots op
        # Hvis man har en knap, som hedder self.beregn_knap kan det se nogenlunde
        # saaledes ud
        # self.beregn_knap.clicked.connect(self.beregn)

    # Herunder er det en god idé at skrive en metode(funktion), som
    # - gemmer værdierne for a, b og c
    # - sender værdierne til funktionen reelle_loesninger_til_andengradsligning
    # - modtager svaret fra reelle_loesninger_til_andengradsligning
    # - skriver svaret ud i et eller flere felter.
    # I kan jo kalde metoden for beregn
    def beregn(self):
        pass



andengradsligningsloeser = QApplication(sys.argv)

vindue = HovedVindue()
vindue.show()

andengradsligningsloeser.exec()
# Skabelon:1 ends here