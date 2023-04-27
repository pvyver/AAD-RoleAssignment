import subprocess
import re

ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')

def callTheAPI():
  URI="https://graph.microsoft.com/beta/roleManagement/directory/roleAssignments"

  USER_PRINCIPAL_OBJECT_ID="66bb642f-3dae-4619-b584-1c91ade9aede"
  DIRECTORY_ROLE_TEMPLATE_ID="62e90394-69f5-4237-9190-012177145e10"

  BODY={}
  BODY['principalId']=USER_PRINCIPAL_OBJECT_ID
  BODY['roleDefinitionId']=DIRECTORY_ROLE_TEMPLATE_ID
  BODY['directoryScopeId']="/"

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