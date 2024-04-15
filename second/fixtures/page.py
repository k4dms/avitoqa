import pytest
from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright


@pytest.fixture(scope='class')
def browser(request) -> Page:
    playwright = sync_playwright().start()
    browser = get_chrome_browser(playwright, request)
    context = get_context(browser, request, 'local')
    page_data = context.new_page()
    yield page_data
    for context in browser.contexts:
        context.close()
    browser.close()
    playwright.stop()


def get_chrome_browser(playwright, request) -> Browser:
    return playwright.chromium.launch(
        headless=False,
        slow_mo=200,
        args=['--start-maximized']
    )


def get_context(browser, request, start) -> BrowserContext:

    context = browser.new_context(
        no_viewport=True,
        locale='ru-RU'
    )
    context.set_default_timeout(
        timeout=60000
    )
    return context

