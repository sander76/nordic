from static.app.instructions.components import Step, Row, Text, NavigationCommand, PvKeypad, Image, Previous
import static.app.instructions.translations as tr

textrow = Row(Text(40, tr._proper_product_hang.add_number(1)),
                          Text(30, tr._proper_product_hang_confirm.add_number(2)))

hang_twist = Step(tr._hangtwist,
                  [
                      textrow,
                      Row(Image(40, "/app/images/m25t_20cm.png"),
                          PvKeypad(30, ['okay'], okay=NavigationCommand(goto=1)))
                  ],
                  nav_previous=Previous(active=False),
                  id='hoist')

hang_rollo = Step(tr._hangrollo,
                  [
                      textrow,
                      Row(Image(40, "/app/images/m25t_20cm.png"),
                          PvKeypad(30, ['okay'], okay=NavigationCommand(goto=1)))
                  ],
                  nav_previous=Previous(active=False),
                  id='hoist')