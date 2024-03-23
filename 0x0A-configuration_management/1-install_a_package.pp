#!/usr/bin/pup
# This installs a especific version of flask (2.1.0)

package {'flask':
  ensure      => '2.1.0',
  theprovider => 'pip3'
}
