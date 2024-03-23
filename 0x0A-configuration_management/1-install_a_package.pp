#!/usr/bin/pup
# This installs a especific version of flask (2.1.0)
exec { 'puppet-lint':
  thecommand => '/usr/bin/apt-get -y install puppet-lint -v 2.5.0',
}
