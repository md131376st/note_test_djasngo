from django.test import TestCase
from web.apps.main_app.forms import AddVasHelpForm



class FormTestCase(TestCase):

    def test_form_valid_data(self):
        # kanape
        vas_pk = Vas.objects.get(id=6).pk
        # FORM fields
        form = AddVasHelpForm()
        #in memory save
        form = form.save(commit=False)
       #save in db
        form.save()

        self.assertEqual(form.top_text, 'test-kanape')

    def test_form_no_data(self):
        #cheak with empty form
        form = AddVasHelpForm()

        self.assertFalse(form.is_valid())
