# -*- coding: utf-8 -*-

import webbrowser

import kivy
kivy.require('{{cookiecutter.kivy_version}}')

from kivy.animation import Animation
from kivy.app import App
from kivy.clock import Clock
from kivy.logger import Logger
from kivy.properties import BoundedNumericProperty, ObjectProperty
from kivy.uix.carousel import Carousel
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar


class RefLabel(Label):
    """Simple that opens a contained url in the webbrowser."""

    def on_ref_press(self, url):
        """Callback which is being run when the user clicks on a ref in the
        label.

        :param str url: URL to be opened in the webbrowser
        """
        Logger.info("Opening '{url}' in webbrowser.".format(url=url))
        webbrowser.open(url)


class TransitionProgress(ProgressBar):
    """ProgressBar with pre-defined animations for fading in and out."""

    _in = Animation(opacity=1.0, duration=0.4)
    _out = Animation(opacity=0.0, duration=0.1)

    def fade_in(self):
        """Play the animation for changing the ProgressBar to be opaque."""
        self._in.start(self)

    def fade_out(self):
        """Play the animation to hide the ProgressBar."""
        self._out.start(self)


class {{cookiecutter.app_class_name}}(App):
    """Simple Slideshow App with a user defined title.

    Attributes:
      title (str): Window title of the application

      timer (:class:`kivy.properties.BoundedNumericProperty`):
        Helper for the slide transition of `carousel`

      carousel (:class:`kivy.uix.carousel.Carousel`):
        Widget that holds several slides about the app
    """

    title = '{{cookiecutter.app_title}}'

    timer = BoundedNumericProperty(0, min=0, max=400)
    carousel = ObjectProperty(Carousel)

    def start_timer(self, *args, **kwargs):
        """Schedule the timer update routine and fade in the progress bar."""
        Logger.debug("Starting timer")
        Clock.schedule_interval(self._update_timer, 1 / 60.0)
        self.progress_bar.fade_in()

    def stop_timer(self, *args, **kwargs):
        """Reset the timer and unschedule the update routine."""
        Logger.debug("Stopping timer")
        Clock.unschedule(self._update_timer)
        self.progress_bar.fade_out()
        self.timer = 0

    def delay_timer(self, *args, **kwargs):
        """Stop the timer but re-schedule it based on `anim_move_duration` of
        :attr:`{{cookiecutter.app_class_name}}.carousel`.
        """
        self.stop_timer()
        Clock.schedule_once(
            self.start_timer,
            self.carousel.anim_move_duration
        )

    def build(self):
        """Initialize the GUI based on the kv file and set up events.

        Returns:
          (:class:`kivy.uix.anchorlayout.AnchorLayout`): Root widget specified
            in the kv file of the app
        """
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
