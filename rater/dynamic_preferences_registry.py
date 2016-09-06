# blog/dynamic_preferences_registry.py

from dynamic_preferences.types import StringPreference, ChoicePreference, IntegerPreference, Section
from dynamic_preferences.registries import global_preferences_registry

preferences_section = Section('rater')


@global_preferences_registry.register
class RatingScale(ChoicePreference):
    section = preferences_section
    name = 'rating_scale'
    choices = [('continuous_scale', 'continuous scale'), ('single_choice', 'single choice')]
    default = 'continuous_scale'
    help_text = 'rating representation'


@global_preferences_registry.register
class RatingQuestion(StringPreference):
    section = preferences_section
    name = 'rating_question'
    default = 'How much of the meaning of the human translation is also expressed in the machine translation?'
    help_text = "question for human raters"


@global_preferences_registry.register
class SingleChoiceOptions(StringPreference):
    section = preferences_section
    name = 'single_choice_options'
    default = 'None;Little;Much;Most;All'
    help_text = 'options for single choice selection'


@global_preferences_registry.register
class ContinuousScaleMin(IntegerPreference):
    section = preferences_section
    name = 'continuous_scale_min'
    default = 0
    help_text = 'minimum value in the continuous scale'


@global_preferences_registry.register
class ContinuousScaleMax(IntegerPreference):
    section = preferences_section
    name = 'continuous_scale_max'
    default = 100
    help_text = 'maximum value in the continuous scale'


@global_preferences_registry.register
class ContinuousScaleMinLabel(StringPreference):
    section = preferences_section
    name = 'continuous_scale_min_label'
    default = 'Strongly Disagree'
    help_text = 'minimum value label in the continuous scale'


@global_preferences_registry.register
class HelpText(StringPreference):
    section = preferences_section
    name = 'help_text'
    default = '''In this evaluation task you will assess the quality of Chinese-English machine translations of one hundred sentences. Instead of the original Chinese sentences, professional human translations will be used as benchmark for evaluation. Specifically, you will be asked how much of the meaning of the human translation is expressed in the machine translation. <br /><br />
Your email will only be used as an identifier for this particular task and will be discarded as soon as we collect the data.<br /><br />
If you have to leave off evaluating and get back to the task later, you can log in again using your email and you will return to the sentence where you left off.'''
    help_text = 'introductory text to be displayed on hte first page'


@global_preferences_registry.register
class ContinuousScaleMaxLabel(StringPreference):
    section = preferences_section
    name = 'continuous_scale_max_label'
    default = 'Strongly Agree'
    help_text = 'maximum value label in the continuous scale'


@global_preferences_registry.register
class NumberOfButches(IntegerPreference):
    section = preferences_section
    name = 'number_of_batches'
    default = 1
    help_text = 'number of batches rated segments are divided into'


@global_preferences_registry.register
class NumberOfRatersPerButches(IntegerPreference):
    section = preferences_section
    name = 'number_of_raters_per_batch'
    default = 5
    help_text = 'number of raters who should fully rater all the segments in batch to consider it rated'
