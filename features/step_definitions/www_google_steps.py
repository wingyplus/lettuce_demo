# -*- coding: utf-8 -*-
from lettuce import after, before, step, world
from splinter.browser import Browser


@before.all
def initialize_browser():
    world.browser = Browser("firefox")


@after.all
def quit_browser(total_result):
    world.browser.quit()


@step(u'Given I am on Google Search')
def given_i_am_on_google_search(step):
    world.browser.visit("http://www.google.co.th")


@step(u'When I search keyword "([^"]*)"')
def when_i_search_keyword(step, keyword):
    world.browser.find_by_id("gbqfq").fill(keyword)
    world.browser.find_by_id("gbqfb").click()


@step(u'Then I see title of first result should begin with "([^"]*)"')
def then_i_see_title_of_result_should_begin_with_keyword(step, keyword):
    result = world.browser.find_by_css("#rso a > em")
    assert result.text.startswith(keyword) is True
