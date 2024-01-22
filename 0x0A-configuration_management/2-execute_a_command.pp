# Manifest that kills a process nameed killmenow
exec { 'kill_my_process':
  command => 'pkill killmenow',
  path    => '/usr/bin/',
  logoutput => 'trur',
}
