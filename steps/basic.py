from behave import *
from tuneinutilapp import TuneInUtilApp as App

use_step_matcher("re")


@when("I pass in a language and (?P<kind_of_genre>.*) genre")
def step_impl(context, kind_of_genre):
    """
    :type context: behave.runner.Context
    """
    print(kind_of_genre)
    context.app = App()


@then("I get a convenient list of all stations matching both language and genre")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("I pass in a country")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("I get a convenient list of all stations from that country")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass