from instructor.components import Product
from instructor.connect import connect_m25s_duette
from instructor.initialise import initialise_duette

m25s_duette = Product("Roller blind", [connect_m25s_duette,
                                       initialise_duette,
                                       ])
