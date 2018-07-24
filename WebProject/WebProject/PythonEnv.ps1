param([Parameter(Mandatory = $True)][string] $phase)

if ($phase -eq 'restore')
{
    # setup the Python virtual environment under the env folder and restore packages from requirements.txt
    py -m pip install --user virtualenv
    py -m virtualenv env
    .\env\Scripts\activate
    pip install -r requirements.txt
}
elseif ($phase -eq 'save')
{
    # Activate the virtual environment and save package to requirements.txt
    .\env\Scripts\activate
    pip freeze > requirements.txt
}
else
{
    Write-Host "Pass '-phase restore' or '-phase save' args to tell the script whether to restore/save the environment" -ForegroundColor Red
}