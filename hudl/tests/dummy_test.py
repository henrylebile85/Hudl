

import pytest

@pytest.mark.dummy
@pytest.mark.usefixtures('init_driver')
class TestDummy:
    def test_dummy_func(self):
        try:
            self.driver.get('https://www.hudl.com/')
            print('I am a dummy test line 1')
            print('I am a dummy test line 2')



        finally:
            # Ensure the browser gets closed even if the test is paused in the debugger
            self.driver.quit()
