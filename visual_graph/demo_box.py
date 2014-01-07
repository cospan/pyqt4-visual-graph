from PyQt4.QtCore import *
from PyQt4.QtGui import *

from box import Box
import graphics_utils as gu

class DemoBox(Box):
    """Demo Box"""

    def __init__(self,
                 scene,
                 position,
                 instance_name,
                 color,
                 parameters,
                 rect,
                 bus):

        self.bus = bus
        self.s = scene
        self.dragging = False
        super(DemoBox, self).__init__( position = position,
                                     scene = scene,
                                     name = instance_name,
                                     color = color,
                                     rect = rect,
                                     user_data = parameters)
        md = {}
        md["name"] = instance_name
        md["color"] = "color"
        md["data"] = parameters
        md["move_type"] = "move"
        self.setAcceptDrops(True)
        self.sdbg = False

    def contextMenuEvent(self, event):

        menu_items = (("&Remove", self.remove_slave),)

        menu = QMenu(self.parentWidget())
        for text, func in menu_items:
            menu.addAction(text, func)
        menu.exec_(event.screenPos())


    def remove_demo_box(self):
        self.s.remove_slave(self)

    def itemChange(self, a, b):
        #if self.sdbg: print "SLAVE: itemChange()"
        if self.isSelected():
            #if self.sdbg: print "\t%s is selected" % self.box_name
            self.s.slave_selected(self.box_name, self.bus, self.user_data)
        else:
            #if self.sdbg: print "\t%s is NOT selected" % self.box_name
            self.s.slave_deselected(self.box_name, self.bus, self.user_data)
        return super(DemoBox, self).itemChange(a, b)

    def dragMoveEvent(self, event):
        if self.dbg: print "Drag Move Event"
        super(DemoBox, self).dragMoveEvent(event)

    def mouseMoveEvent(self, event):
        if self.sdbg: print "demo_box: mouseMoveEvent: %s" % self.box_name
        if (Qt.LeftButton & event.buttons()) > 0:
            pos = event.pos()
            epos = event.buttonDownPos(Qt.LeftButton)
            l = QLineF(pos, epos)
            if (l.length() < QApplication.startDragDistance()):
            #if (l.length() < 10):
                if self.dbg: print "\tLength: %f" % l.length()
                event.accept
                return

            else:
                self.dragging = True
                self.hide()
               
                #Create and dispatch a move event
                drag = QDrag(event.widget())
                drag.start(Qt.MoveAction)
                #drag.start(Qt.MoveAction)
                
                #create an image for the drag
                size = QSize(self.start_rect.width(), self.start_rect.height())
                pixmap = QPixmap(size)
                pixmap.fill(QColor(self.color))
                painter = QPainter(pixmap)
                pen = QPen(self.style)
                pen.setColor(Qt.black)
                painter.setPen(pen)
                painter.setFont(self.text_font)
                #painter.drawText(0, 0, 100, 100, 0x24, self.box_name)

                gu.add_label_to_rect(painter, self.rect, self.box_name)
                painter.end()
                drag.setPixmap(pixmap)
                #p = QPointF(event.buttonDownScreenPos(Qt.LeftButton))
                #p = p.toPoint()
                if self.dbg: print "Position: %f, %f" % (pos.x(), pos.y())
                drag.setHotSpot(epos.toPoint())
                
                if self.sdbg: print "\tdrag started"
                drag.exec_()
                event.accept
                #self.s.invalidate(self.s.sceneRect())

        super(DemoBox, self).mouseMoveEvent(event)


    def paint(self, painter, option, widget):
        if self.dbg: print "Position: %f %f" % (self.pos().x(), self.pos().y())
        super(DemoBox, self).paint(painter, option, widget)
        
