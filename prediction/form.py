from django import forms

class PredictionForm(forms.Form):
    BHK_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]

    BATH_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]

    LOCATION_CHOICES = [
        ('', 'Choose a Location'),
        ('Electronic City', 'Electronic City'),
        ('Rajaji Nagar', 'Rajaji Nagar'),
        # Add more locations as needed
    ]

    Squareft = forms.CharField(label='Area (Square Feet)', max_length=100, initial='1000', widget=forms.TextInput(attrs={'class': 'form-control'}))
    uiBHK = forms.ChoiceField(label='BHK', choices=BHK_CHOICES, widget=forms.RadioSelect, initial='2')
    uiBathrooms = forms.ChoiceField(label='Bath', choices=BATH_CHOICES, widget=forms.RadioSelect, initial='2')
    uiLocations = forms.ChoiceField(label='Location', choices=LOCATION_CHOICES , widget=forms.Select(attrs={'class': 'form-control'}))