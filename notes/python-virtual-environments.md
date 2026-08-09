# Virtual Environments — Week 4 Wednesday

## Today's Task
Create a venv, install pytest inside it, run the Week 3 tests under it, and
document every command.

## Commands (the workflow)
    py -m venv .venv                      # create the venv folder
    .\.venv\Scripts\Activate.ps1          # activate (prompt gains (.venv) )
    pip list                              # inside venv: nearly empty (isolated!)
    pip install pytest                    # installs INTO the venv only
    python -m pytest ..\python_day_09\test_can_parser.py -v
    deactivate                            # leave the venv

## One-time fix for the activation error
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    # RemoteSigned = local scripts run, downloads must be signed
    # CurrentUser  = only my account, no admin, smallest scope (least privilege)

## Key Concepts
- A venv is a private, isolated package folder for ONE project.
- It starts empty - global packages are NOT visible inside it.
- Activation puts the venv's Scripts folder at the FRONT of PATH, so
  python/pip resolve to the venv's copies first (Tuesday's "first match wins").
- pytest reported .venv\Scripts\python.exe - proof it used the venv's Python,
  not the global 3.9 / 3.14 confusion.

## Memory-Level Understanding
py -m venv .venv    -> creates .venv with its own python.exe + empty site-packages
Activate.ps1        -> prepends .venv to PATH (activation = PATH manipulation)
pip install (active) -> lands in .venv's private site-packages
deactivate          -> removes .venv from PATH; back to global

## Automotive Relevance
Real diagnostic projects pin their exact dependencies in a venv so results are
reproducible - the same test passes on my laptop, a colleague's, and CI. No
"works on my machine" surprises from version drift.

## What I Understood Well
I understood the process of creating venv, activating it. Also permissions were restricted in my local to activate venv, changed the permissions to activate "RemoteSigned" venv. Then installing pytest inside venv and then executing tests of week 3 from this venv. And finally deactivating venv

## What Confused Me
Nothing today, just did not know my local computer has restricted venv activation due to security reseons, which is very good.

## Next Improvement
Add a requirements.txt so the exact package versions can be reinstalled anywhere.