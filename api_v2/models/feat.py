"""The model for a feat."""
from django.db import models
from .abstracts import HasName, HasDescription, HasPrerequisite, Benefit
from .document import FromDocument


class FeatBenefit(Benefit):
    """This is the model for an individual benefit of a feat."""

    desc = models.TextField(
        help_text='Text of the individual feat benefit.')

    feat = models.ForeignKey('Feat', on_delete=models.CASCADE)


class Feat(HasName, HasDescription, HasPrerequisite, FromDocument):
    """
    This is the model for a feat.

    A feat represents a talent or an area of expertise that
    gives a character special capabilities. It embodies
    training, experience, and abilities beyond what a
    class provides.
    """

    @property
    def benefits(self):
        """Returns the set of benefits that are related to this feat."""
        return self.featbenefit_set

    class Meta:
        """To assist with the UI layer."""

        verbose_name_plural = "feats"
