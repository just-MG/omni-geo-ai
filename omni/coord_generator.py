from shapely.geometry import Point, Polygon

class Coordinate_Generator:
    def __init__(self) -> None:
        self._af_eu_au_as_oc = Polygon([(17.8142312, -16.7108124),(3.5687915, -15.8784186),(5.2337296, 7.5098281),(-34.7202624, 18.0201127),(-34.5756541, 28.3033158),(11.9787634, 52.7369096),(25.0713121, 66.280576),(5.3378161, 78.0579198),(21.0287687, 91.593076),(-0.2371702, 97.1758012),(-10.328879, 110.5247807),(-39.9448406, 114.3919682),(-31.8417886, 131.7943119),(-44.6230577, 146.7357182),(-51.0351699, 178.9735331),(-25.1448899, -178.3944095),(-27.4991034, -141.1275135),(4.0635104, -143.7624808),(-2.4377929, 156.8437522),(3.109623, 130.1932277),(21.8337346, 128.4781663),(35.9885307, 145.6619777),(61.4523219, 161.1042255),(64.4010357, 50.2450814),(71.5414773, 21.1497121),(62.1187854, 4.0344901),(62.5774865, -8.6260189),(56.34098, -11.83871),(43.6394982, -9.8577216)])

        self._americas = Polygon([(58.6972963, -138.0811578),(33.6838108, -121.3819391),(17.4242108, -106.9585073),(7.1337872, -83.5796011),(-5.3205151, -82.1733511),(-57.7487289, -76.9754794),(-56.14862, -62.9223399),(-6.6264325, -32.6879649),(8.94408, -59.6449673),(23.2733059, -58.2941697),(29.3562164, -77.6323254),(47.5953997, -50.9030204)])

        self._greenland = Polygon([(73.1062163, -58.235126),(58.916732, -49.1823916),(58.6891035, -40.7448916),(74.0017805, -50.7644229)])

        self._iceland = Polygon([(63.2837069, -26.2429385),(62.8457732, -12.7956729),(66.6622515, -11.6530947),(67.3488767, -25.3640322)])

        self._hawaii = Polygon([(18.2222455, -160.2688187),(18.6391566, -152.1828812),(23.8193139, -161.1912772),(22.4954337, -155.9952849)])
        self.poligons_continents = []
    
