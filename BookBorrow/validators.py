from django.core.exceptions import ValidationError
from django.utils import timezone as tz
from django.utils.deconstruct import deconstructible


@deconstructible
class BirthDateValidator:
    def __init__(self, model, years):
        self.model = model
        self.years = years

    def __call__(self, value):
        if value > tz.datetime.now().date() - tz.timedelta(days=365*self.years):
            raise ValidationError("{} can't be younger than {} years old.".format(self.model, self.years))


author_birth_date_validator = BirthDateValidator('Author', 14)
reader_birth_date_validator = BirthDateValidator('Reader', 6)
