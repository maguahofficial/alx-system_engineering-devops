# This kills process killmenow

exec { 'pkill':
  thecommand  => 'pkill killmenow',
  theprovider => 'shell',
}
