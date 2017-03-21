from instructor.actions.connect import connect_m25s_vvb
from instructor.actions.initialise import initialise_vvb_right,\
    initialise_vvb_left
from instructor.components import Product

m25s_vvb_left = Product(
    "M25 VVB Left",
    [connect_m25s_vvb,
    initialise_vvb_left
     ])

m25s_vvb_right = Product(
    "M25 VVB Right",
    [connect_m25s_vvb,
     initialise_vvb_right
     ])

m25s_vvb_center = Product(
    "M25 VVB Center",
    [connect_m25s_vvb,
     ])

m25s_vvb_upright_left = Product(
    "M25 VVB upright Left",
    [connect_m25s_vvb,
     ])

m25s_vvb_upright_right = Product(
    "M25 VVB upright Right",
    [connect_m25s_vvb,
     ])

m25s_vvb_upright_center = Product(
    "M25 VVB upright Center",
    [connect_m25s_vvb,
     ])
