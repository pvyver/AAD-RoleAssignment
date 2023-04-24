# coding: utf-8

import subprocess
import re

ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')

def callTheAPI():

  URI="https://graph.microsoft.com/v1.0/directoryRoles/roleTemplateId=62e90394-69f5-4237-9190-012177145e10/members/$ref" 

  BODY=  {"@odata.id": "https://graph.microsoft.com/v1.0/directoryObjects/23755f28-0cf4-46e5-9b51-773cbb13814b"}

  assignGlobalAdminCommand='az rest --method POST --uri '+URI+' --header Content-Type=application/json --body "'+str(BODY)+'"'

  proc = subprocess.Popen(assignGlobalAdminCommand,cwd=None, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
  while True:
    line = proc.stdout.readline()
    if line:
      thetext=ansi_escape.sub('', line.decode('utf-8').rstrip('\r|\n'))
      print(thetext)
    else:
      break

callTheAPI()