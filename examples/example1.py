#! /usr/bin/python

import os
import sys
from PyQt4.Qt import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, "visual_graph"))

from graphics_widget import GraphicsWidget

from link import link_type as lt
from link import Link


#Exercise
if __name__ == '__main__':
    app = QApplication(sys.argv)
    gw = GraphicsWidget()
    b = gw.add_box("bob", color = 'blue', position = QPointF(-200, 0))
    b.movable(False)
    j = gw.add_box("Jane", color = 'pink', position = QPointF(200, 0))
    link = b.add_link(j)
    #link.en_bezier_connections(True)
    gw.show()
    sys.exit(app.exec_())
