from django.dispatch import Signal


badge_awarded = Signal(providing_args=["badge"])
pre_badge_takenback = Signal(providing_args=["badge_takenback"])
post_badge_takenback = Signal(providing_args=["badge_takenback"])
