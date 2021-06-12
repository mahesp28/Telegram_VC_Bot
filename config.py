HEROKU = True  # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku & Docker.
if HEROKU:
    from os import environ
    from dotenv import load_dotenv
    
    load_dotenv()  # take environment variables from .env.
    API_ID = int(environ["c58583b14d98761ae6c39189d1fa67a5"])
    API_HASH = environ["1413525"]
    SESSION_STRING = environ["1BVtsOKYBu8XD0QgRQyYtmOwlm80qztb1jGQsnhjhi99omGDur43N8MVY1M0RDzceMrLSdHgxIG4wDEb6tdujYOOH79QDtdLU-nOb8FvJaqvi-NwH4py1ffp3Eizl0iPXkz0YD0BVDYNg6NyKTmJGxdZ2UrPL2R2Ts_NiExBBI77lIFk8CYbrT-5HO_Rh_pprEvenZ5FECiMi07R_4-loMu4e2ZS25uU757IX9pU92xlV9ijOTGPb37FoRSfXRZFHwHGd5M90zh0G-P4l_NRODszev1hXUhNZ1g0pGXGqW1uxTvgqaMkh92D9u8-dMKPspy-fxCIordgRXXa7THa0HJleqOpw-f4="]  # Check Readme for session
    ARQ_API_KEY = environ["EVNDYS-WNTXJR-WFOVTR-DQVZFH-ARQ"]

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 14371
    API_HASH = "e46b6c854d2bf58a0"
    ARQ_API_KEY = "Get this from @ARQRobot"
# don't make changes below this line
ARQ_API = "https://thearq.tech"
