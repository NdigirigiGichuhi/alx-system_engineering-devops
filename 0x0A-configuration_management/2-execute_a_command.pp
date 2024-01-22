# Manifest that kills a process nameed killmenow
exec { 'killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin/',
}
