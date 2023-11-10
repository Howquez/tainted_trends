from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'questionnaire'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    completed_survey = models.BooleanField(doc="indicates whether a participant has completed the survey.",
                                           initial=False,
                                           blank=True)

    # Open Text Fields
    perception = models.LongStringField(
        doc="Please describe as detailed as you can: What were the first thoughts and feelings towards the brand KFC that came to your mind when you were scrolling through the feed?",
        lable="Please describe as detailed as you can: What were the first thoughts and feelings towards the brand KFC that came to your mind when you were scrolling through the feed?",
        blank=False)

    # Trustworthiness Bruner et al 2019 p. 471
    # Using the items below, please describe Estrava.
    trust_1 = models.IntegerField(
        doc="Dishonest",
        label="Dishonest",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False)

    trust_2 = models.IntegerField(
        doc="Insincere",
        label="Insincere",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False)

    trust_3 = models.IntegerField(
        doc="Manipulative",
        label="Manipulative",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False)

    trust_4 = models.IntegerField(
        doc="Not trustworthy",
        label="Not trustworthy",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False)

    # Diet
    KFC_food = models.IntegerField(
        doc="To what extent do you enjoy food from KFC? (1 = Strongly Dislike, 7 = Strongly Like)",
        label="To what extent do you enjoy food from KFC? (1 = Strongly Dislike, 7 = Strongly Like)",
        widget=widgets.RadioSelectHorizontal,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False)

    KFC_brand = models.IntegerField(
        doc="To what extent do you like the brand KFC? (1 = Strongly Dislike, 7 = Strongly Like)",
        label="To what extent do you like the brand KFC? (1 = Strongly Dislike, 7 = Strongly Like)",
        widget=widgets.RadioSelectHorizontal,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False)

    meatless = models.StringField(
        doc="Do you currently eat a vegetarian or vegan diet (one with no meat, i.e., without beef, pork, chicken, turkey, fish, shellfish, or other meats)?",
        label="Do you currently eat a vegetarian or vegan diet (one with no meat, i.e., without beef, pork, chicken, turkey, fish, shellfish, or other meats)?",
        choices=["Yes", "No"],
        blank=False
    )

    fast_food = models.StringField(
        doc="Do you enjoy fast food?",
        label="Do you enjoy fast food?",
        choices=["Yes", "No"],
        blank=False)

    ff_frequency = models.StringField(
        doc="How often do you eat fast food?",
        label="How often do you eat fast food?",
        widget=widgets.RadioSelect,
        choices=["Everyday",
                 "Once a week",
                 "Once a month",
                 "Not very often",
                 "Never"],
        blank=False)

    # Covariates
    age = models.IntegerField(label="Please enter your age",
                              min=18,
                              max=99)

    gender = models.StringField(
        label="Please select your gender.",
        choices=[
            [1, "Female"],
            [2, "Male"],
            [3, "Other"],
            [4, "Prefer not to say"],
        ]
    )

    education = models.IntegerField(
        label="What is the highest level of education you achieved?",
        choices=[
            [1, "Some high school"],
            [2, "High school diploma or G.E.D."],
            [3, "Some college"],
            [4, "Associate's degree"],
            [5, "Bachelor's degree"],
            [6, "Master's degree"],
            [7, "Other"],
            [8, "Doctorate"],
        ]
    )

    genAI = models.StringField(
        doc="Did you use ChatGPT or any other generative AI to fill out the open text fields? (Note: we will not reject your submission, if you did. We need the information to assess our overall data quality.)",
        label="Did you  use ChatGPT or any other generative AI to fill out the open text fields? (Note: we will not reject your submission, if you did. We need the information to assess our overall data quality.)",
        widget=widgets.RadioSelect,
        choices=["Yes", "No"],
        blank=False)

    # Usability Butler et al 2023 p. 16
    # Consider the feed from a usability perspective. The feed felt...
    usability_1 = models.IntegerField(
        doc="Easy vs. Confusing",
        label="Easy",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False)

    usability_2 = models.IntegerField(
        doc="Engaging vs. Boring",
        label="Easy",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False)

    usability_3 = models.IntegerField(
        doc="Realistic vs. Unnatural",
        label="Easy",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False)

    usability_otf = models.LongStringField(
        doc="Did you encounter any problems while browsing the feed? Do you have any comments?",
        lable="Did you encounter any problems while browsing the feed? Do you have any comments?",
        blank=True)



# PAGES
class A_Questionnaire(Page):
    form_model = "player"
    form_fields = ["perception"]

class B_Questionnaire(Page):
    form_model = "player"
    form_fields = ["trust_1", "trust_2", "trust_3", "trust_4"]

class C_Questionnaire(Page):
    form_model = "player"
    form_fields = ["KFC_food", "KFC_brand",  "meatless", "fast_food", "ff_frequency"]

class D_Questionnaire(Page):
    form_model = "player"
    form_fields = ["age", "gender", "education", "genAI"]

class E_Questionnaire(Page):
    form_model = "player"
    form_fields = ["usability_1", "usability_2", "usability_3", "usability_otf"]

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.finished = True
        player.completed_survey = player.participant.finished

class F_Debrief(Page):
    pass


page_sequence = [A_Questionnaire, B_Questionnaire, C_Questionnaire, D_Questionnaire, E_Questionnaire, F_Debrief]
