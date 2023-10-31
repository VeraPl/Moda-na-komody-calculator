#!/usr/bin/env python

import sys

from PyQt5.QtCore import pyqtSignal, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QGridLayout,
        QMainWindow, QMessageBox, QOpenGLWidget, QScrollArea,
        QSizePolicy, QWidget)

from OpenGL.GL         import *
from OpenGL.GLU        import *


class GLWidget(QOpenGLWidget):
    xRotationChanged = pyqtSignal(int)
    yRotationChanged = pyqtSignal(int)
    zRotationChanged = pyqtSignal(int)
    def __init__(self, parent=None):
        super(GLWidget, self).__init__(parent=parent)
        self.x_rot = 0
        self.y_rot = 0
        self.z_rot = 0
        self.auto_rot = 0

        self.l = 0
        self.w = 0
        self.h = 0
        self.section = 0
        self.shelf = 0

        self.edges = ((0, 1), (0, 3), (0, 4), (1, 2), (1, 5), (2, 3), (2, 6), (3, 7), (4, 5), (4, 7), (7, 6), (6, 5))
        self.walls = ((2, 6, 7, 3), (4, 5, 6, 7), (0, 4, 7, 3), (1, 5, 6, 2), (0, 1, 2, 3), (1, 0, 4, 5))
        self.vertices = None
        self.change_values()

        self.auto_rotation = False
        timer = QTimer(self)
        timer.timeout.connect(self.advance_gears)
        timer.start(70)

    def initializeGL(self) -> None:
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_TEXTURE_2D)
        glDepthFunc(GL_LESS)
        size = self.size()
        gluPerspective(45, (size.width() / size.height()), 0.05, 50.0)
        glTranslatef(0.0, 0.0, -25)

    def draw(self):
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glBegin(GL_LINES)
        for edge in self.edges:

            for vertex in edge:
                glVertex3fv(self.vertices[vertex])
                glColor3fv((1, 1, 1))

        glEnd()

    def change_values(self):
        self.vertices = ((-self.w, -self.h, -self.l), (-self.w, self.h, -self.l), (-self.w, self.h, self.l),
                         (-self.w, -self.h, self.l), (self.w, -self.h, -self.l), (self.w, self.h, -self.l),
                         (self.w, self.h, self.l), (self.w, -self.h, self.l), (self.w / 2, self.h, self.l))

    def draw_section(self, count):
        if count:
            count += 1
            K = self.w * 2 / count
            w = []
            for i in range(1, count):
                w.append(self.w - (K * i))
            l, h = (self.l, self.h)
            for i in range(count - 1):
                vertices = ((-w[i], -h, -l), (-w[i], h, -l), (-w[i], h, l), (-w[i], -h, l))
                glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
                glBegin(GL_LINES)
                for edge in ((0, 1), (1, 2), (0, 3), (2, 3)):
                    for vertex in edge:
                        glVertex3fv(vertices[vertex])
                        glColor3fv((1, 1, 1))
                glEnd()

    def draw_shelves(self, count):
        if count:
            count += 1
            K = self.h * 2 / count
            h = []
            for i in range(1, count):
                h.append(self.h - (K * i))
            w, l = (self.w, self.l)
            for i in range(count - 1):
                vertices = ((w, h[i], -l), (-w, h[i], -l), (-w, h[i], l), (w, h[i], l))
                glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
                glBegin(GL_LINES)
                for edge in ((0, 1), (1, 2), (2, 3), (3, 0)):
                    for vertex in edge:
                        glVertex3fv(vertices[vertex])
                        glColor3fv((1,1,1))
                glEnd()

    def paintGL(self, coordinates=None) -> None:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        glRotated(self.x_rot / 16.0, 1.0, 0.0, 0.0)
        glRotated(self.y_rot / 16.0, 0.0, 1.0, 0.0)
        glRotated(self.z_rot / 16.0, 0.0, 0.0, 1.0)
        glRotated(self.auto_rot /16, 0.0, 1.0, 0.0)
        self.draw()
        self.draw_section(self.section)
        self.draw_shelves(self.shelf)
        glPopMatrix()

    def resizeGL(self, width, height):
        side = min(width, height)
        glViewport((width - side) // 2, (height - side) // 2, side, side)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glFrustum(-1.0, +1.0, -1.0, 1.0, 5.0, 60.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslated(0.0, 0.0, -40.0)

    def set_x_rotation(self, angle):
        self.normalize_angle(angle)

        if angle != self.x_rot:
            self.x_rot = angle
            self.xRotationChanged.emit(angle)
            self.update()

    def set_y_rotation(self, angle):
        self.normalize_angle(angle)

        if angle != self.y_rot:
            self.y_rot = angle
            self.yRotationChanged.emit(angle)
            self.update()

    def set_z_rotation(self, angle):
        self.normalize_angle(angle)

        if angle != self.z_rot:
            self.z_rot = angle
            self.z_rotationChanged.emit(angle)
            self.update()

    def mousePressEvent(self, event):
        self.lastPos = event.pos()

    def mouseMoveEvent(self, event):
        dx = event.x() - self.lastPos.x()
        dy = event.y() - self.lastPos.y()

        if event.buttons() & Qt.LeftButton:
            self.set_x_rotation(self.x_rot + 8 * dy)
            self.set_y_rotation(self.y_rot + 8 * dx)
        elif event.buttons() & Qt.RightButton:
            self.set_x_rotation(self.x_rot + 8 * dy)
            self.set_z_rotation(self.z_rot + 8 * dx)

        self.lastPos = event.pos()

    def x_rotation(self):
        return self.x_rot

    def y_rotation(self):
        return self.y_rot

    def z_rotation(self):
        return self.z_rot

    def normalize_angle(self, angle):
        while (angle < 0):
            angle += 360 * 16

        while (angle > 360 * 16):
            angle -= 360 * 16

    def advance_gears(self):
        if self.auto_rotation:
            self.auto_rot += 2 * 16
            self.update()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        self.glWidget = GLWidget()

        self.glWidgetArea = QScrollArea()
        self.glWidgetArea.setWidget(self.glWidget)
        self.glWidgetArea.setWidgetResizable(True)
        self.glWidgetArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.glWidgetArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.glWidgetArea.setSizePolicy(QSizePolicy.Ignored,
                QSizePolicy.Ignored)
        self.glWidgetArea.setMinimumSize(50, 50)

        centralLayout = QGridLayout()
        centralLayout.addWidget(self.glWidgetArea, 0, 0)
        centralWidget.setLayout(centralLayout)

        self.setWindowTitle("Grabber")
        self.resize(500, 350)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())