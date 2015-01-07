# -*- coding: utf-8 -*-

"""
{{cookiecutter.repo_name}}
============================

The root of :class:`{{cookiecutter.app_class_name}}` is created from the kv file.
"""

import kivy
kivy.require('{{cookiecutter.kivy_version}}')

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.carousel import Carousel
from kivy.uix.progressbar import ProgressBar
from kivy.animation import Animation
from kivy.logger import Logger
from kivy.properties import BoundedNumericProperty, ObjectProperty

import webbrowser


class RefLabel(Label):
    """Simple that opens a contained url in the webbrowser."""

    def on_ref_press(self, url):
        Logger.info("Opening '{url}' in webbrowser.".format(url=url))
        webbrowser.open(url)


class TransitionProgress(ProgressBar):
    """ProgressBar with pre-defined animations for fading in and out."""

    _in = Animation(opacity=1.0, duration=0.4)
    _out = Animation(opacity=0.0, duration=0.1)

    def fade_in(self):
        self._in.start(self)

    def fade_out(self):
        self._out.start(self)


class {{cookiecutter.app_class_name}}(App):
    """Simple Slideshow App with a user defined title.

    It's timer property controls the speed in which slides change.
    """

    title = '{{cookiecutter.app_title}}'

    timer = BoundedNumericProperty(0, min=0, max=400)
    carousel = ObjectProperty(Carousel)

    def start_timer(self, *args, **kwargs):
        Logger.debug("Starting timer")
        Clock.schedule_interval(self._update_timer, 1 / 60.0)
        self.progress_bar.fade_in()

    def stop_timer(self, *args, **kwargs):
        Logger.debug("Stopping timer")
        Clock.unschedule(self._update_timer)
        self.progress_bar.fade_out()
        self.timer = 0

    def delay_timer(self, *args, **kwargs):
        self.stop_timer()
        Clock.schedule_once(
            self.start_timer,
            self.carousel.anim_move_duration
        )

    def build(self):
        self.carousel = self.root.ids.carousel
        self.progress_bar = self.root.ids.progress_bar
        self.progress_bar.max = self.property('timer').get_max(self)

        self.start_timer()
        self.carousel.bind(on_touch_down=self.stop_timer)
        self.carousel.bind(current_slide=self.delay_timer)
        return self.root

    def _update_timer(self, dt):
        try:
            self.timer += 1
        except ValueError:
            self.stop_timer()
            self.carousel.load_next()
            Logger.debug("Automatically loading next slide")
