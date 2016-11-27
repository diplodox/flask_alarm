import os

parc = {}


# Tous les peripheriques connus
machines = dict()
machines['freebox_player']='192.168.0.25'
machines['pi_2'] = '192.168.0.23'
machines['pi_3'] = '192.168.0.28'
machines['port_olivier']='192.168.0.33'
machines['port_cath']='192.168.0.39'
machines['diplodox'] = '192.168.0.16'
machines['tablette_oli'] = '192.168.0.19'
#machines['pc_chambre'] = '192.168.0.15'
#machines['tablette_cath'] = '192.168.0.'

# remplir dict() parc
def assign_state(t):
  state = os.system("ping -c 1 $1 > /dev/null " + t[1])
  if state == 0:
    parc[t[0], t[1]]='UP'
  else:
    parc[t[0], t[1]]='DOWN'



def return_parc():
  for key, val in machines.items():
    #print("La machine {} a l adresse IP : {}".format(key, val))
    #print 'Check status for {}'.format(key)
    assign_state([key, val])

#print ('_'*10, 'Return PARCC')


#return_parc()

#print ('_'*10)


#for key, val in parc.items():
#  print("La machine {} est {}".format(key, val))


#print 'machine[port_olivier] : ', machines['port_olivier']
#print 'state ordi linux diplo : ', parc['diplodox', '192.168.0.16']

