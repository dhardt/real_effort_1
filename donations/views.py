from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class DonationDecision(Page):
    form_model = models.Player
    form_fields = ['donation']

class IntroDonation(Page):
    def vars_for_template(self):
        from allocation_survey.models import Player as TreatmentPlayer
        treatment = TreatmentPlayer.objects.get(participant=self.participant).treatment
        return {'treatment':
                treatment}
        #previous_variables = TreatmentPlayer.objects.get(participant=self.participant)

class ClassificationDecision(Page):
    form_model = models.Player
    form_fields = ['claimed_content']
    def before_next_page(self):
        self.player.calculate_payoff()
        self.player.check_claim()

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    def vars_for_template(self):
        from allocation_survey.models import Player as TreatmentPlayer
        treatment = TreatmentPlayer.objects.get(participant=self.participant).treatment
        return {'treatment':
                treatment}
    #def vars_for_template(self):
     #   from allocation_survey.models import Player as P
      #  for field in ['treatment', 'sex', 'age']:
       #     code = field+" = P.objects.get(participant=self.participant)."+field
       #     exec(code)





page_sequence = [
    IntroDonation,
    DonationDecision,
    #ResultsWaitPage,
    ClassificationDecision,
    Results
]
