# -*- coding: utf-8 -*-


def test_switch_language(app):
    test_label = app.carousel.slides[1].children[1]

    english_text = (
        "This app uses Kivy, a Python Framework for NUI Development."
    )
    assert test_label.text == english_text

    app.on_config_change(app.config, 'user_settings', 'language', 'de')

    german_text = (
        "Diese App benutzt Kivy, ein Python Framework zur NUI Entwicklung."
    )
    assert test_label.text == german_text
