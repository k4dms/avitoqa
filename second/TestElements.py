import pytest

EcoBlock = "//*[contains(concat(' ', @class, ' '), ' desktop-impact-items-F7T6E ')]"


@pytest.mark.smoke
class TestElements:
    def test_zero_state(self, browser):
        test_data = '''
        {
                    "result": {
                        "blocks": {
                            "personalImpact": {
                                "data": {
                                    "co2": 0,
                                    "energy": 0,
                                    "materials": 0,
                                    "pineYears": 0,
                                    "water": 0
                                }
                            }
                        },
                        "isAuthorized": true
                    },
                       "status": "ok"
                }
        '''
        browser.goto('https://www.avito.ru/avito-care/eco-impact', wait_until='domcontentloaded')
        browser.route("**/web/1/charity/ecoImpact/init",
                      lambda route: route.fulfill(status=200, body=test_data))
        browser.locator(EcoBlock).screenshot(path="output/Testcase1.png")

    def test_round_to_kilo(self, browser):
        test_data = '''{
            "result": {
                "blocks": {
                    "personalImpact": {
                        "data": {
                            "co2": 999
                            ,
                            "energy": 999,
                            "materials": 14,
                            "pineYears": 56,
                            "water": 999
                        }
                    }
                },
                "isAuthorized": true
            },
            "status": "ok"
        }'''
        browser.goto('https://www.avito.ru/avito-care/eco-impact', wait_until='domcontentloaded')
        browser.route("**/web/1/charity/ecoImpact/init",
                      lambda route: route.fulfill(body=test_data, headers={"content-type": "application/json"}, ))
        browser.locator(EcoBlock).screenshot(path="output/Testcase2.png")

    def test_one_tonn(self, browser):
        test_data = '''{
            "result": {
                "blocks": {
                    "personalImpact": {
                        "data": {
                            "co2": 1000,
                            "energy": 1000,
                            "materials": 14,
                            "pineYears": 56,
                            "water": 1000
                        }
                    }
                },
                "isAuthorized": true
            },
            "status": "ok"
        }'''
        browser.goto('https://www.avito.ru/avito-care/eco-impact', wait_until='domcontentloaded')
        browser.route("**/web/1/charity/ecoImpact/init",
                      lambda route: route.fulfill(body=test_data))
        browser.locator(EcoBlock).screenshot(path="output/Testcase3.png")

    def test_round_to_million(self, browser):
        test_data = '''{
                    "result": {
                        "blocks": {
                            "personalImpact": {
                                "data": {
                                    "co2": 999999,
                                    "energy": 999999,
                                    "materials": 14,
                                    "pineYears": 56,
                                    "water": 999999
                                }
                            }
                        },
                        "isAuthorized": true
                    },
                    "status": "ok"
                }'''
        browser.goto('https://www.avito.ru/avito-care/eco-impact', wait_until='domcontentloaded')
        browser.route("**/web/1/charity/ecoImpact/init",
                      lambda route: route.fulfill(body=test_data))
        browser.locator(EcoBlock).screenshot(path="output/Testcase4.png")

    def test_one_million(self, browser):
        test_data = '''{
                           "result": {
                               "blocks": {
                                   "personalImpact": {
                                       "data": {
                                           "co2": 1000000,
                                           "energy": 1000000,
                                           "materials": 14,
                                           "pineYears": 56,
                                           "water": 1000000
                                       }
                                   }
                               },
                               "isAuthorized": true
                           },
                           "status": "ok"
                       }'''
        browser.goto('https://www.avito.ru/avito-care/eco-impact', wait_until='domcontentloaded')
        browser.route("**/web/1/charity/ecoImpact/init",
                      lambda route: route.fulfill(body=test_data))
        browser.locator(EcoBlock).screenshot(path="output/Testcase5.png")

    def test_round_to_billion(self, browser):
        test_data = '''{
                    "result": {
                        "blocks": {
                            "personalImpact": {
                                "data": {
                                    "co2": 999999999,
                                    "energy": 999999999,
                                    "materials": 14,
                                    "pineYears": 56,
                                    "water": 999999999
                                }
                            }
                        },
                        "isAuthorized": true
                    },
                    "status": "ok"
                }'''
        browser.goto('https://www.avito.ru/avito-care/eco-impact', wait_until='domcontentloaded')
        browser.route("**/web/1/charity/ecoImpact/init",
                      lambda route: route.fulfill(body=test_data))
        browser.locator(EcoBlock).screenshot(path="output/Testcase6.png")

    def test_one_billion(self, browser):
        test_data = '''{
                    "result": {
                        "blocks": {
                            "personalImpact": {
                                "data": {
                                    "co2": 1000000000,
                                    "energy": 1000000000,
                                    "materials": 14,
                                    "pineYears": 56,
                                    "water": 1000000000
                                }
                            }
                        },
                        "isAuthorized": true
                    },
                    "status": "ok"
                }'''
        browser.goto('https://www.avito.ru/avito-care/eco-impact', wait_until='domcontentloaded')
        browser.route("**/web/1/charity/ecoImpact/init",
                      lambda route: route.fulfill(body=test_data))
        browser.locator(EcoBlock).screenshot(path="output/Testcase7.png")

    def test_round_to_trillion(self, browser):
        test_data = '''{
                    "result": {
                        "blocks": {
                            "personalImpact": {
                                "data": {
                                    "co2": 999999999999,
                                    "energy": 999999999999,
                                    "materials": 14,
                                    "pineYears": 56,
                                    "water": 999999999999
                                }
                            }
                        },
                        "isAuthorized": true
                    },
                    "status": "ok"
                }'''
        browser.goto('https://www.avito.ru/avito-care/eco-impact', wait_until='domcontentloaded')
        browser.route("**/web/1/charity/ecoImpact/init",
                      lambda route: route.fulfill(body=test_data))
        browser.locator(EcoBlock).screenshot(path="output/Testcase8.png")

    def test_trillion(self, browser):
        test_data = '''{
                    "result": {
                        "blocks": {
                            "personalImpact": {
                                "data": {
                                    "co2": 1000000000000,
                                    "energy": 1000000000000,
                                    "materials": 14,
                                    "pineYears": 56,
                                    "water": 1000000000000
                                }
                            }
                        },
                        "isAuthorized": true
                    },
                    "status": "ok"
                }'''
        browser.goto('https://www.avito.ru/avito-care/eco-impact', wait_until='domcontentloaded')
        browser.route("**/web/1/charity/ecoImpact/init",
                      lambda route: route.fulfill(body=test_data))
        browser.locator(EcoBlock).screenshot(path="output/Testcase9.png")

    def test_with_huge_number(self, browser):
        test_data = '''{
                    "result": {
                        "blocks": {
                            "personalImpact": {
                                "data": {
                                    "co2": 1000000000000000,
                                    "energy": 1000000000000000,
                                    "materials": 14,
                                    "pineYears": 56,
                                    "water": 1000000000000000
                                }
                            }
                        },
                        "isAuthorized": true
                    },
                    "status": "ok"
                }'''
        browser.goto('https://www.avito.ru/avito-care/eco-impact', wait_until='domcontentloaded')
        browser.route("**/web/1/charity/ecoImpact/init",
                      lambda route: route.fulfill(body=test_data))
        browser.locator(EcoBlock).screenshot(path="output/Testcase10.png")
