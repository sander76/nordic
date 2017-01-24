from instructor.components import Product
from instructor.connect import connect_m25s_duette
from instructor.initialise import initialise_duette

m25s_duette = Product("M25S Duette Free", [connect_m25s_duette,
                                       initialise_duette,
                                       ])

m25s_tensioned = Product("M25S Duette Tensioned",[connect_m25s_duette,
                                       initialise_duette,
                                       ])