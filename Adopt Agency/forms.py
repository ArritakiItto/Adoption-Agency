from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, AnyOf

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name", validators=[InputRequired()])

    species = SelectField("Species", choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')], validators=[AnyOf(['cat', 'dog', 'porcupine'])])

    photo_url = StringField("Photo URL", validators=[Optional(), URL()])

    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])

    notes = TextAreaField("Comments", validators=[Optional()])

    class EditPetForm(FlaskForm):
        """Form for editing an existing pet."""

        photo_url = StringField("Photo URL", validators=[Optional(), URL()])

        notes = TextAreaField("Comments", validators=[Optional()])

        available = BooleanField("Available?")