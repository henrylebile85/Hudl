

import os


def get_base_url():

    supported_env = ['dev', 'test', 'stag', 'beta_prod', 'prod']

    env = os.environ.get('ENV', 'prod')
    # I replaced None with prod as a default value.
    # For the purpose of this Hudl exercise, we would be using only prod

    if not env:
        raise Exception("The environment variable 'ENV' must be set." )

    env = env.lower()
    if env not in supported_env:
        raise Exception(f'Provided browser {env} is not one of the supported.'
                        f'Supported are: {supported_env}')


    if env.lower() == 'test':
        return 'https://www.test.hudl.com' # site not real, just an example

    if env.lower() == 'stag':
        return 'https://www.stag.hudl.com' # site not real, just an example

    if env.lower() == 'beta_prod':
        return 'https://www.beta_prod.hudl.com' # site not real, just an example

    if env.lower() == 'prod':
        return 'https://www.hudl.com' # real site

    if env.lower() == 'dev':
        return 'https://www.local.hudl.com' # site not real, just an example




# Note
# All other environments are for illustration purposes only
# There is no need to set the environment variable
