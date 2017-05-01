#import instructor.translations as tr
from instructor.translations import Translations as tr
from instructor.components import Step, Row, Text,\
    NavigationCommand, PvKeypad, Image, Previous
from instructor.constants import ID_HOIST

textrow = Row(Text(40, tr.PROPER_PRODUCT_HANG.add_number(1)),
              Text(30, tr.PROPER_PRODUCT_HANG_CONFIRM.add_number(2)))

hang_twist = Step(tr.HANG_TWIST,
                  [
                      textrow,
                      Row(Image(40, "/app/images/m25t_20cm.png"),
                          PvKeypad(30, ['okay'],
                                   okay=NavigationCommand(goto=1)))
                  ],
                  nav_previous=Previous(active=False),
                  nav_id=ID_HOIST)

hang_rollo = Step(tr.HANG_RB,
                  [
                      textrow,
                      Row(Image(40, "/app/images/m25t_20cm.png"),
                          PvKeypad(30, ['okay'],
                                   okay=NavigationCommand(goto=1)))
                  ],
                  nav_previous=Previous(active=False),
                  nav_id=ID_HOIST)
