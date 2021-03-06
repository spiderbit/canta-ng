#! /usr/bin/python -O
# -*- coding: utf-8 -*-
#
#    CANTA - A free entertaining educational software for singing
#    Copyright (C) 2007  S. Huchler, A. Kattner, F. Lopez
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os

class LabelList():
    def __init__(self, parent, widget_properties):
        # self.anchoring = widget_properties['anchoring']


        # self.font_to_sing = widget_properties['font']['lyrics']['to_sing']['obj']
        # self.color_to_sing = widget_properties['font']['lyrics']['to_sing']['color']

        # self.font_special = widget_properties['font']['lyrics']['special']['obj']
        # self.color_special = widget_properties['font']['lyrics']['special']['color']

        # self.font_active = widget_properties['font']['lyrics']['active']['obj']
        # self.color_active = widget_properties['font']['lyrics']['active']['color']

        # self.font_done = widget_properties['font']['lyrics']['done']['obj']
        # self.color_done = widget_properties['font']['lyrics']['done']['color']

        # if self.anchoring == 'bottom':
        #     self.anchors = pudding.ANCHOR_BOTTOM \
        #         | pudding.ANCHOR_LEFT
        # elif self == 'top':
        #     self.anchors = pudding.ANCHOR_TOP
        self.children = []
        pass

    def _delete(self, pos):
        self.children[pos].label = ''


    def _delete_all(self):
        # for i in range(len(self.children)):
        #     self._delete(i)
        # del self.children[0:]
        pass


    def add_line(self, segments):
        for i in range(len(segments)):
            self.children.append('x')
            # pudding.control.SimpleLabel(self,
            #         label=segments[i].text,
            #         font=self.font_to_sing,
            #         top=self.top,
            #         left=0)

            # self.children[-1].color = self.color_to_sing

            # if segments[i].special:
            #     self.children[-1].color = self.color_special
            #     #self.children[-1].font = self.font_special

            # if segments[i].freestyle:
            #     self.children[-1].color = self.color_special
            #     #self.children[-1].font = self.font_special
            pass

    def _show_line(self, segments):
        print ("label_list: show line")
        self.add_line(segments)
        # if self.children[-1].right > 400:
        #     self.font_to_sing.width = 5
        #     print (self.children[-1].right)
        #     print ("to wide: ", self.width)


    def _activate_note(self, pos):
        print ("activate_note")
        #self.children[pos].color = self.color_active
        #self.children[pos].font = self.font_active


    def _de_activate_note(self, pos):
        #self.children[pos].color = self.color_done
        #self.children[pos].font = self.font_done
        print ("deactivate_note")

    def _end(self):
        self.visible = 0


def main():
    pass

if __name__ == '__main__': main()
